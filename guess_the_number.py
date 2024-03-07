import random

def guess_the_number(range_limit, guess):
    if not isinstance(range_limit, int) or not isinstance(guess, int):
        return "Invalid input: range and guess must be integers"
    if range_limit <= 0 or range_limit > 10000:
        return "Invalid input: range must be a positive integer <= 10000"
    if guess <= 0:
        return "Invalid input: guess must be a positive integer"
    if guess > range_limit:
        return "Invalid input: guess must be within the range"
    
    number_to_guess = random.randint(1, range_limit)
    
    if guess == number_to_guess:
        return "CONGRATULATIONS!! YOU GUESSED CORRECT!"
    else:
        return "womp womp."



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
