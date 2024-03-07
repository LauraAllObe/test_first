import random

def guess_the_number(range_limit):
    if not isinstance(range_limit, int) or range_limit <= 0 or range_limit > 10000:
        return "Invalid input: range must be a positive integer <= 10000"
    
    number_to_guess = random.randint(1, range_limit)
    user_guess = int(input(f"Guess the number between 1 and {range_limit}: "))
    
    if user_guess < 1 or user_guess > range_limit:
        return "Invalid input: the guess must be within the range"
    
    if user_guess == number_to_guess:
        return "CONGRATULATIONS!! YOU GUESSED CORRECT!"
    else:
        return "womp womp."

range_limit = int(input("Enter the range limit (between 1 and 10000): "))
print(guess_the_number(range_limit))

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
