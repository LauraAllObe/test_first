import random

def guess_the_number(number, guess):
    if not isinstance(number, int) or not isinstance(guess, int):
        return "Invalid input: must be an integer"
    if number <= 0 or guess <= 0:
        return "Invalid input: must be a positive number"
    if number > 10000:
        return "Invalid input: must be a number <=10000"
    if guess < 1 or guess > number:
        return "Invalid input: the guess must be within the range"
    if guess == number:
        return "CONGRATULATIONS!! YOU GUESSED CORRECT!"
    return "womp womp."

def main():
    range_limit = int(input("Enter the range limit (between 1 and 10000): "))
    if range_limit < 1 or range_limit > 10000:
        print("Invalid range limit. Exiting...")
        return
    number_to_guess = random.randint(1, range_limit)
    user_guess = int(input(f"Guess the number between 1 and {range_limit}: "))
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
