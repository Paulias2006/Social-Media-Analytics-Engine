from __future__ import annotations

from analytics import run_analytics
from config import DB_PATH, OUTPUT_DIR, load_settings
from csv_utils import write_csv
from dashboard import build_dashboard
from data_generation import generate_posts
from database import create_database


def main() -> None:
    settings = load_settings()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    posts = generate_posts(settings)
    create_database(DB_PATH, posts)
    outputs = run_analytics(DB_PATH)

    write_csv(OUTPUT_DIR / "social_posts.csv", posts)
    write_csv(OUTPUT_DIR / "platform_summary.csv", outputs["platform_summary"])
    write_csv(OUTPUT_DIR / "topic_summary.csv", outputs["topic_summary"])
    write_csv(OUTPUT_DIR / "sentiment_summary.csv", outputs["sentiment_summary"])
    build_dashboard(
        OUTPUT_DIR / "dashboard.html",
        posts,
        outputs["platform_summary"],
        outputs["topic_summary"],
        outputs["sentiment_summary"],
    )

    print("Social media analytics project generated successfully.")


if __name__ == "__main__":
    main()
