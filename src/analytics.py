from __future__ import annotations

from pathlib import Path

from database import query_dicts


PLATFORM_SQL = """
SELECT
    platform,
    COUNT(*) AS posts,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement_rate,
    ROUND(SUM(reach), 0) AS total_reach,
    ROUND(AVG(CASE WHEN sentiment_label = 'Positive' THEN 1.0 ELSE 0 END) * 100, 2) AS positive_share_pct
FROM posts
GROUP BY platform
ORDER BY avg_engagement_rate DESC
"""

TOPIC_SQL = """
SELECT
    topic,
    COUNT(*) AS posts,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement_rate,
    ROUND(SUM(likes + comments + shares + saves), 0) AS total_engagements
FROM posts
GROUP BY topic
ORDER BY total_engagements DESC
"""

SENTIMENT_SQL = """
SELECT
    sentiment_label,
    COUNT(*) AS posts,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement_rate,
    ROUND(AVG(reach), 2) AS avg_reach
FROM posts
GROUP BY sentiment_label
ORDER BY posts DESC
"""


def run_analytics(db_path: Path) -> dict[str, list[dict[str, object]]]:
    return {
        "platform_summary": query_dicts(db_path, PLATFORM_SQL),
        "topic_summary": query_dicts(db_path, TOPIC_SQL),
        "sentiment_summary": query_dicts(db_path, SENTIMENT_SQL),
    }
