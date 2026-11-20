import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from score_content import score_content


class ScoreContentTests(unittest.TestCase):
    def setUp(self):
        self.payload = {"title": "test", "dimensions": {
            "hook_strength": 10, "audience_relevance": 10, "novelty": 10,
            "emotional_resonance": 10, "retention_design": 10,
            "share_save_value": 10, "visual_clarity": 10,
            "platform_fit": 10, "credibility": 10, "cta_fit": 10,
        }}

    def test_maximum_score(self):
        result = score_content(self.payload)
        self.assertEqual(result["score"], 100.0)
        self.assertEqual(result["label"], "strong test candidate")

    def test_zero_score(self):
        for key in self.payload["dimensions"]:
            self.payload["dimensions"][key] = 0
        self.assertEqual(score_content(self.payload)["score"], 0.0)

    def test_missing_dimension_rejected(self):
        del self.payload["dimensions"]["hook_strength"]
        with self.assertRaisesRegex(ValueError, "Missing dimensions"):
            score_content(self.payload)

    def test_out_of_range_rejected(self):
        self.payload["dimensions"]["hook_strength"] = 11
        with self.assertRaisesRegex(ValueError, "between 0 and 10"):
            score_content(self.payload)

    def test_boolean_rejected(self):
        self.payload["dimensions"]["hook_strength"] = True
        with self.assertRaises(ValueError):
            score_content(self.payload)


if __name__ == "__main__":
    unittest.main()
