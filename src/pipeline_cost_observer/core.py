"""Core workflow for Pipeline Cost Observer by Red@."""

PROJECT_NAME = "Pipeline Cost Observer"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
