import random

def guess_the_number(range_limit, guess):
    if not isinstance(range_limit, int) or not isinstance(guess, int):
        return "Invalid input: must be an integer"
    if range_limit <= 0:
        return "Invalid input: must be a positive number"
    if range_limit > 10000:
        return "Invalid input: must be a number <=10000"
    if guess <= 0:
        return "Invalid input: must be a positive number"
    if guess > range_limit:
        return "Invalid input: the guess must be within the range"
    
    number_to_guess = random.randint(1, range_limit)
    
    if guess == number_to_guess:
        return "CONGRATULATIONS!! YOU GUESSED CORRECT!"
    else:
        return "womp womp."