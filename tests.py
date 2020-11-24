"""Test bot."""

import unittest

from bot import bot
from web import app


class BotTests(unittest.TestCase):
    """A set of discord bot tests."""

    def test_commands(self):
        """Test bot commands."""
        self.assertEqual(bool(bot.command("ping")), True)
        self.assertEqual(bool(bot.command("parrot")), True)


class WebTests(unittest.TestCase):
    """A seto of web service test."""

    def setUp(self):
        """Set up test configuration."""
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    def tearDown(self):
        """Tear down test."""
        pass

    def test_main_page(self):
        """Test main page."""
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
