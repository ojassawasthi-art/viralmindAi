# Installation

## Requirements
- Python 3.10+ only if you want to run the optional scoring utility.
- An AI host that can accept skill instructions or system prompts.
- Optional search/API credentials for live research (not required for the core skill).

## Local validation

```bash
python -m unittest discover -s tests -v
python scripts/score_content.py examples/sample_content.json
```

## Use as a skill bundle

Start with `skills/viralmind-core/SKILL.md`. Include the specialist skill folders that match the task. Preserve folder names and relative links when packaging. Platform-specific installation differs; see `integrations/`.
