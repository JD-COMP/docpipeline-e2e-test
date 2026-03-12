"""Core application module."""


def health(verbose: bool = False):
    """Return health status."""
    result = {"status": "ok"}
    if verbose:
        result["version"] = "2.0.0"
    return result


def process(data: str, normalize: bool = True) -> dict:
    """Process input data."""
    if normalize:
        data = data.strip()
    return {"result": data.upper(), "length": len(data)}


def validate(data: str, strict: bool = False) -> dict:
    """Validate input data.

    Args:
        data: Input string to validate.
        strict: If True, enforce minimum length.

    Returns:
        Dict with is_valid and errors.
    """
    errors = []
    if not data:
        errors.append("Data must not be empty")
    if strict and len(data) < 5:
        errors.append("Data too short for strict mode")
    return {"is_valid": len(errors) == 0, "errors": errors}


def batch_process(items: list[str]) -> list[dict]:
    """Process multiple items in batch."""
    return [process(item) for item in items]
