"""Core application module."""


def health():
    """Return health status."""
    return {"status": "ok"}


def process(data: str) -> dict:
    """Process input data."""
    return {"result": data.upper(), "length": len(data)}
