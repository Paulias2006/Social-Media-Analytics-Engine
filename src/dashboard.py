from __future__ import annotations

import html
from pathlib import Path


def build_dashboard(path: Path, posts: list[dict[str, object]], platform_rows: list[dict[str, object]], topic_rows: list[dict[str, object]], sentiment_rows: list[dict[str, object]]) -> None:
    total_posts = len(posts)
    total_reach = sum(int(row["reach"]) for row in posts)
    avg_engagement = sum(float(row["engagement_rate"]) for row in posts) / total_posts
    positive_share = sum(1 for row in posts if row["sentiment_label"] == "Positive") / total_posts * 100

    cards = [
        ("Posts analyzed", f"{total_posts:,}"),
        ("Total reach", f"{total_reach:,}"),
        ("Avg engagement", f"{avg_engagement:.2f}%"),
        ("Positive sentiment", f"{positive_share:.1f}%"),
    ]
    card_html = "".join(f"<article><span>{label}</span><strong>{value}</strong></article>" for label, value in cards)

    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Social Media Analytics Engine</title>
  <style>
    body {{ margin: 0; font-family: Arial, sans-serif; background: #f7f8fb; color: #1c2230; }}
    header {{ background: #20283d; color: white; padding: 34px 44px; }}
    header p {{ color: #dfe5f5; max-width: 900px; line-height: 1.55; }}
    main {{ padding: 28px 44px 48px; }}
    .kpis {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 14px; }}
    .kpis article, .panel {{ background: white; border: 1px solid #dfe4ee; border-radius: 8px; padding: 18px; }}
    .kpis span {{ display: block; color: #596275; margin-bottom: 8px; }}
    .kpis strong {{ font-size: 26px; }}
    .layout {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 18px; margin-top: 18px; }}
    .bar-row {{ display: grid; grid-template-columns: 120px 1fr 76px; align-items: center; gap: 10px; margin: 12px 0; }}
    .bar {{ height: 13px; background: #edf1f6; border-radius: 999px; overflow: hidden; }}
    .bar div {{ height: 100%; background: #4e72d0; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th, td {{ border-bottom: 1px solid #e3e8f1; padding: 9px; text-align: left; font-size: 14px; }}
  </style>
</head>
<body>
  <header>
    <h1>Social Media Analytics Engine</h1>
    <p>Engagement, sentiment, platform, and topic analytics transformed into clean CSV outputs, SQL-ready tables, and a client-ready dashboard.</p>
  </header>
  <main>
    <section class="kpis">{card_html}</section>
    <section class="layout">
      {bar_chart("Engagement by Platform", platform_rows, "platform", "avg_engagement_rate", "%")}
      {bar_chart("Engagement by Topic", topic_rows, "topic", "total_engagements")}
      {table("Sentiment Summary", sentiment_rows)}
    </section>
  </main>
</body>
</html>
"""
    path.write_text(page, encoding="utf-8")


def bar_chart(title: str, rows: list[dict[str, object]], label_key: str, value_key: str, suffix: str = "") -> str:
    max_value = max(float(row[value_key]) for row in rows) or 1
    bars = []
    for row in rows:
        value = float(row[value_key])
        width = value / max_value * 100
        bars.append(
            "<div class='bar-row'>"
            f"<span>{html.escape(str(row[label_key]))}</span>"
            f"<div class='bar'><div style='width:{width:.1f}%'></div></div>"
            f"<strong>{value:.2f}{suffix}</strong>"
            "</div>"
        )
    return f"<section class='panel'><h2>{html.escape(title)}</h2>{''.join(bars)}</section>"


def table(title: str, rows: list[dict[str, object]]) -> str:
    headers = list(rows[0].keys())
    head = "".join(f"<th>{html.escape(header)}</th>" for header in headers)
    body = "".join("<tr>" + "".join(f"<td>{html.escape(str(row[header]))}</td>" for header in headers) + "</tr>" for row in rows)
    return f"<section class='panel'><h2>{html.escape(title)}</h2><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></section>"
