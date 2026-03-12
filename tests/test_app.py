import pytest
from src.app import health, process, validate, batch_process


def test_health_default():
    """Test health with default verbose=False."""
    result = health()
    assert result == {"status": "ok"}
    assert "version" not in result


def test_health_verbose():
    """Test health with verbose=True."""
    result = health(verbose=True)
    assert result == {"status": "ok", "version": "2.0.0"}


def test_process_no_normalize():
    """Test process with normalize=False."""
    result = process("  hello  ", normalize=False)
    assert result == {"result": "  HELLO  ", "length": 9}


def test_process_normalize():
    """Test process with normalize=True (default)."""
    result = process("  hello  ")
    assert result == {"result": "HELLO", "length": 5}


def test_process_empty_string():
    """Test process with empty string."""
    result = process("")
    assert result == {"result": "", "length": 0}


def test_process_whitespace_only():
    """Test process with whitespace-only string."""
    result = process("   \t  ")
    assert result == {"result": "", "length": 0}


def test_validate_empty():
    """Test validate with empty string."""
    result = validate("")
    assert result == {"is_valid": False, "errors": ["Data must not be empty"]}


def test_validate_non_empty():
    """Test validate with non-empty string."""
    result = validate("abc")
    assert result == {"is_valid": True, "errors": []}


def test_validate_strict_short():
    """Test validate with strict=True and short data."""
    result = validate("abc", strict=True)
    assert result == {"is_valid": False, "errors": ["Data too short for strict mode"]}


def test_validate_strict_long():
    """Test validate with strict=True and long enough data."""
    result = validate("abcde", strict=True)
    assert result == {"is_valid": True, "errors": []}


def test_validate_strict_empty():
    """Test validate with strict=True and empty string (both errors)."""
    result = validate("", strict=True)
    assert result == {
        "is_valid": False,
        "errors": ["Data must not be empty", "Data too short for strict mode"]
    }


def test_batch_process_empty_list():
    """Test batch_process with empty list."""
    result = batch_process([])
    assert result == []


def test_batch_process_single_item():
    """Test batch_process with single item."""
    result = batch_process(["hello"])
    assert result == [{"result": "HELLO", "length": 5}]


def test_batch_process_multiple_items():
    """Test batch_process with multiple items."""
    result = batch_process(["a", "b c", "  d  "])
    assert result == [
        {"result": "A", "length": 1},
        {"result": "B C", "length": 3},
        {"result": "D", "length": 1}
    ]


def test_batch_process_with_whitespace():
    """Test batch_process preserves whitespace when normalize=False in process."""
    # Note: batch_process always uses process with default normalize=True
    # This test verifies that behavior
    result = batch_process(["  x  "])
    assert result == [{"result": "X", "length": 1}]