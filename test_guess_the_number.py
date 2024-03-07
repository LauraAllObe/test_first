import unittest
from unittest.mock import patch
from guess_the_number import guess_the_number

class test_guess_the_number(unittest.TestCase):
  def test_non_integer(self):
    self.assertEqual(guess_the_number(1.5,1),"Invalid input: must be an integer")
  def test_lower_bound(self):
    self.assertEqual(guess_the_number(-100,1), "Invalid input: must be a positive number")
  def test_upper_bound(self):
    self.assertEqual(guess_the_number(1000000,1), "Invalid input: must be a number <=10000")
  def test_out_of_range(self):
    self.assertEqual(guess_the_number(100,1000), "Invalid input: the guess must be within the range")
  @patch('random.randint')
  def test_correct_guess(self, mock_randint):
    mock_randint.return_value = 5
    self.assertEqual(guess_the_number(100,5), "CONGRATULATIONS!! YOU GUESSED CORRECT!")
  @patch('random.randint')
  def test_incorrect_guess(self, mock_randint):
    mock_randint.return_value = 10
    self.assertEqual(guess_the_number(100,5), "womp womp.")
  
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
