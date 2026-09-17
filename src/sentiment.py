from __future__ import annotations


POSITIVE_WORDS = {
    "growth",
    "trusted",
    "clear",
    "fast",
    "useful",
    "secure",
    "simple",
    "profitable",
    "strong",
    "easy",
    "great",
    "smart",
}

NEGATIVE_WORDS = {
    "slow",
    "confusing",
    "expensive",
    "risky",
    "late",
    "weak",
    "hard",
    "bad",
    "unstable",
    "problem",
    "loss",
    "poor",
}


def score_text(text: str) -> tuple[int, str]:
    tokens = [token.strip(".,!?;:").lower() for token in text.split()]
    score = sum(1 for token in tokens if token in POSITIVE_WORDS) - sum(1 for token in tokens if token in NEGATIVE_WORDS)
    if score > 0:
        return score, "Positive"
    if score < 0:
        return score, "Negative"
    return score, "Neutral"
