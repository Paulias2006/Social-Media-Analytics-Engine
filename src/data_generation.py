from __future__ import annotations

import random
from datetime import date, timedelta

from sentiment import score_text


POSITIVE_PHRASES = [
    "fast mobile money growth",
    "clear financial education",
    "simple dashboard insights",
    "trusted customer service",
    "smart data analytics",
]

NEGATIVE_PHRASES = [
    "slow support problem",
    "expensive campaign loss",
    "confusing user journey",
    "risky payment delay",
    "weak engagement result",
]

NEUTRAL_PHRASES = [
    "new campaign update",
    "weekly market note",
    "product feature overview",
    "customer feedback summary",
    "brand awareness post",
]


def generate_posts(settings: dict) -> list[dict[str, object]]:
    random.seed(settings["random_seed"])
    start = date(2026, 1, 1)
    rows: list[dict[str, object]] = []

    for post_id in range(1, settings["post_count"] + 1):
        platform = random.choice(settings["platforms"])
        topic = random.choice(settings["topics"])
        content_type = random.choice(settings["content_types"])
        published_date = start + timedelta(days=random.randint(0, 260))
        phrase = random.choices(
            POSITIVE_PHRASES + NEGATIVE_PHRASES + NEUTRAL_PHRASES,
            weights=[1.4] * len(POSITIVE_PHRASES) + [0.8] * len(NEGATIVE_PHRASES) + [1.0] * len(NEUTRAL_PHRASES),
        )[0]
        text = f"{phrase} for {topic} #{topic.replace(' ', '')}"
        sentiment_score, sentiment_label = score_text(text)

        base_reach = {
            "TikTok": 1600,
            "Instagram": 1300,
            "LinkedIn": 900,
            "Facebook": 800,
            "X": 700,
        }[platform]
        type_multiplier = {"video": 1.5, "short": 1.35, "carousel": 1.2, "image": 1.0, "text": 0.75}[content_type]
        sentiment_multiplier = {"Positive": 1.18, "Neutral": 1.0, "Negative": 0.82}[sentiment_label]
        reach = max(80, int(random.gauss(base_reach * type_multiplier * sentiment_multiplier, 180)))
        likes = int(reach * random.uniform(0.025, 0.09) * sentiment_multiplier)
        comments = int(reach * random.uniform(0.004, 0.025))
        shares = int(reach * random.uniform(0.003, 0.02) * type_multiplier)
        saves = int(reach * random.uniform(0.002, 0.018))
        engagement_rate = round((likes + comments + shares + saves) / reach * 100, 2)

        rows.append(
            {
                "post_id": post_id,
                "published_date": published_date.isoformat(),
                "platform": platform,
                "topic": topic,
                "content_type": content_type,
                "text": text,
                "sentiment_score": sentiment_score,
                "sentiment_label": sentiment_label,
                "reach": reach,
                "likes": likes,
                "comments": comments,
                "shares": shares,
                "saves": saves,
                "engagement_rate": engagement_rate,
            }
        )
    return rows
