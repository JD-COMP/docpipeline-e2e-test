"""Authentication module."""

import hashlib
import hmac
import time

TOKEN_EXPIRY = 3600


def create_token(user_id: str, secret: str) -> str:
    """Create a signed authentication token."""
    timestamp = str(int(time.time()))
    payload = f"{user_id}:{timestamp}"
    sig = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return f"{payload}:{sig}"


def verify_token(token: str, secret: str) -> dict:
    """Verify and decode an authentication token."""
    try:
        user_id, timestamp, signature = token.rsplit(":", 2)
        expected = hmac.new(
            secret.encode(), f"{user_id}:{timestamp}".encode(), hashlib.sha256
        ).hexdigest()
        is_valid = hmac.compare_digest(signature, expected)
        is_expired = (time.time() - int(timestamp)) > TOKEN_EXPIRY
        return {"user_id": user_id, "is_valid": is_valid and not is_expired}
    except (ValueError, TypeError):
        return {"user_id": "", "is_valid": False}
