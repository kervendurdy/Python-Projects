import random

def guess_number(difficulty):
  """
  This function creates the guessing game logic.

  Args:
    difficulty: An integer representing the difficulty level (1: easy, 2: medium, 3: hard).

  Returns:
    None
  """

  # Set the guessing range based on difficulty
  if difficulty == 1:
    lower_bound = 1
    upper_bound = 10
  elif difficulty == 2:
    lower_bound = 1
    upper_bound = 100
  else:
    lower_bound = 1
    upper_bound = 1000

  # Generate a random number within the chosen range
  number = random.randint(lower_bound, upper_bound)

  # Initialize guess to -1 (invalid value) for the loop
  guess = -1

  # Game loop continues until the user guesses the correct number
  while guess != number:
    try:
      # Get user input and convert it to an integer
      guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))

      # Check if guess is within range
      if guess < lower_bound or guess > upper_bound:
        print(f"Invalid guess. Please enter a number between {lower_bound} and {upper_bound}.")
        continue

      # Provide feedback based on the guess
      if guess < number:
        print("Too low, try again!")
      elif guess > number:
        print("Too high, try again!")
    except ValueError:
      print("Invalid input. Please enter a valid number.")

  # User guessed correctly! Congratulate them.
  print(f"Congratulations! You guessed the number {number} correctly.")

if __name__ == "__main__":
  # Get difficulty level from user
  while True:
    try:
      difficulty = int(input("Choose difficulty level (1: Easy, 2: Medium, 3: Hard): "))
      if difficulty not in (1, 2, 3):
        print("Invalid difficulty level. Please choose 1, 2, or 3.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a number (1, 2, or 3).")

  # Start the game
  guess_number(difficulty)
