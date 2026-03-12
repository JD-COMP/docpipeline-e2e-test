import unittest
from src.config import APP_NAME, APP_VERSION, DEBUG, MAX_BATCH_SIZE


class TestConfig(unittest.TestCase):
    """Test application configuration constants."""

    def test_app_name_equals_expected_value(self):
        """APP_NAME should be 'e2e-test-app'."""
        self.assertEqual(APP_NAME, "e2e-test-app")

    def test_app_version_equals_expected_value(self):
        """APP_VERSION should be '2.0.0'."""
        self.assertEqual(APP_VERSION, "2.0.0")

    def test_debug_equals_false(self):
        """DEBUG should be False."""
        self.assertFalse(DEBUG)

    def test_max_batch_size_equals_500(self):
        """MAX_BATCH_SIZE should be 500."""
        self.assertEqual(MAX_BATCH_SIZE, 500)


if __name__ == "__main__":
    unittest.main()