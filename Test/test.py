import unittest
from io import StringIO
from unittest.mock import patch
from Sample.sample import Board

class TestBoardMethods(unittest.TestCase):
    def setUp(self):
        self.board = Board((10, 10))
    def test_init(self):
        self.assertEqual(self.board.board_width, 10)
        self.assertEqual(self.board.board_height, 10)
        self.assertFalse(self.board.is_running)

    def test_play_quit(self):
        with patch('builtins.input', return_value='quit'):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.board.play()
                self.assertFalse(self.board.is_running)
                self.assertIn("Board is running...", fake_out.getvalue())
    def test_play_unknown_input(self):
        with patch('builtins.input', side_effect=['unknown', 'quit']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.board.play()
                self.assertIn("Unknown", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
