import random

def guess_the_number(number, guess):
    if not isinstance(number, int) or not isinstance(guess, int):
        return "Invalid input: must be an integer"
    if number <= 0 or guess <= 0:
        return "Invalid input: must be a positive number"
    if number > 10000:
        return "Invalid input: must be a number <=10000"
    if guess == number:
        return "CONGRATULATIONS!! YOU GUESSED CORRECT!"
    if guess < 1 or guess > 10000:
        return "Invalid input: the guess is out of range"
    return "womp womp."

def main():
    min_limit = int(input("Enter the minimum range limit (between 1 and 10000): "))
    max_limit = int(input("Enter the maximum range limit (between 1 and 10000): "))
    if min_limit < 1 or min_limit > 10000 or max_limit < 1 or max_limit > 10000:
        print("Invalid range limit. Exiting...")
        return
    range_limit = max_limit - min_limit + 1
    number_to_guess = random.randint(min_limit, max_limit)
    user_guess = int(input(f"Guess the number between {min_limit} and {max_limit}: "))
    print(guess_the_number(number_to_guess, user_guess))

if __name__ == "__main__":
    main()

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
