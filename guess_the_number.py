import random

def guess_the_number(range,guess):
  """
  please read:
  use random.randint(1, range) for random number please (so the mock in the unit test works)
  returns (to be compatible with unit tests):
  guess_the_number(1.5,1) should return "Invalid input: must be an integer"
  guess_the_number(-100,1) should return "Invalid input: must be a positive number"
  guess_the_number(1000000,1) should return "Invalid input: must be a number <=10000"
  guess_the_number(100,1000) should return "Invalid input: the guess must be within the range"
  guess_the_number(100,5) should return "CONGRATULATIONS!! YOU GUESSED CORRECT!"
  guess_the_number(100,5) should return "womp womp."
  """
