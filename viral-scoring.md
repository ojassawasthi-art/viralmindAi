# Viral potential scoring

The included CLI computes a transparent 0–100 weighted content-readiness heuristic from ten 0–10 ratings.

| Dimension | Weight |
|---|---:|
| Hook strength | 14% |
| Audience relevance | 14% |
| Retention design | 12% |
| Novelty | 10% |
| Emotional resonance | 10% |
| Share/save value | 10% |
| Visual clarity | 8% |
| Platform fit | 8% |
| Credibility | 8% |
| CTA fit | 6% |

Formula: `sum(dimension_rating / 10 * dimension_weight) * 100`.

The tool expects each dimension as a 0–10 number. The weights are initial expert heuristics, not empirical truths. Tune them by format and objective only after collecting enough representative campaign data. Do not translate the score into “X% chance of going viral.”

## Calibration roadmap

1. Store pre-publication scores and the rubric version.
2. Collect comparable outcome data after fixed windows (for example, 7 days) with platform, audience size and format metadata.
3. Normalize outcomes against the account's baseline and comparable content.
4. Test whether scores rank outcomes better than a baseline heuristic.
5. Report sample size, uncertainty and drift; revise weights only with documented evaluation.
