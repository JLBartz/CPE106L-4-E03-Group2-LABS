import unittest
import os
from oxo_data import saveGame, restoreGame, _getPath

class TestOXOData(unittest.TestCase):
    def setUp(self):
        """Set up test environment: clean up existing game file if present."""
        self.game_file_path = os.path.join(_getPath(), "oxogame.dat")
        if os.path.exists(self.game_file_path):
            os.remove(self.game_file_path)

    def tearDown(self):
        """Clean up test environment: remove game file after test."""
        if os.path.exists(self.game_file_path):
            os.remove(self.game_file_path)

    def test_save_and_restore_game(self):
        """Test that saveGame and restoreGame work correctly."""
        game_data = list("XOXOXOXOX")  # Sample game board data
        saveGame(game_data)  # Save the game
        restored_game = restoreGame()  # Restore the game

        # Check if the restored game matches the saved game
        self.assertEqual(restored_game, game_data, "Restored game does not match saved game!")

    def test_save_creates_file(self):
        """Test that saveGame creates the game file."""
        game_data = list("XO XO XO ")  # Another sample game board data
        saveGame(game_data)

        # Check if the file exists
        self.assertTrue(os.path.exists(self.game_file_path), "Game file was not created!")

    def test_restore_empty_file(self):
        """Test restoreGame behavior with an empty file."""
        # Create an empty game file
        open(self.game_file_path, 'w').close()

        # Restore the game and check if it returns an empty list
        restored_game = restoreGame()
        self.assertEqual(restored_game, [], "Restored game from an empty file should be an empty list!")

    def test_restore_file_not_found(self):
        """Test restoreGame raises FileNotFoundError if no game file exists."""
        with self.assertRaises(FileNotFoundError, msg="restoreGame did not raise FileNotFoundError for missing file!"):
            restoreGame()

if __name__ == "__main__":
    unittest.main()
