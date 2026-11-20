#!/usr/bin/env python3
"""Transparent heuristic scoring for a content concept. Not a virality probability."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any

WEIGHTS = {
    "hook_strength": 0.14,
    "audience_relevance": 0.14,
    "novelty": 0.10,
    "emotional_resonance": 0.10,
    "retention_design": 0.12,
    "share_save_value": 0.10,
    "visual_clarity": 0.08,
    "platform_fit": 0.08,
    "credibility": 0.08,
    "cta_fit": 0.06,
}


def score_content(payload: dict[str, Any]) -> dict[str, Any]:
    """Score integer dimension values from 0 to 10, weighted to 0-100."""
    dimensions = payload.get("dimensions")
    if not isinstance(dimensions, dict):
        raise ValueError("'dimensions' must be an object containing 0-10 ratings")
    missing = [key for key in WEIGHTS if key not in dimensions]
    extra = [key for key in dimensions if key not in WEIGHTS]
    if missing:
        raise ValueError("Missing dimensions: " + ", ".join(missing))
    if extra:
        raise ValueError("Unknown dimensions: " + ", ".join(extra))
    normalized: dict[str, float] = {}
    for key, value in dimensions.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 10:
            raise ValueError(f"{key} must be a number between 0 and 10")
        normalized[key] = round(float(value), 2)
    score = sum(normalized[k] * 10 * weight for k, weight in WEIGHTS.items())
    ranked = sorted(normalized.items(), key=lambda item: item[1])
    return {
        "title": payload.get("title", "Untitled concept"),
        "score": round(score, 1),
        "label": "strong test candidate" if score >= 80 else "promising; improve weakest dimensions" if score >= 65 else "needs revision before testing",
        "dimensions": normalized,
        "weights": WEIGHTS,
        "lowest_dimensions": [k for k, _ in ranked[:3]],
        "interpretation": "A prioritization heuristic, not a probability of going viral or a performance guarantee.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Path to JSON input")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        print(json.dumps(score_content(payload), indent=2))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
