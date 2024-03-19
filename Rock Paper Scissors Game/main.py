import random


def play_rock_paper_scissors(user_score, computer_score):
    """
  Plays a round of Rock-Paper-Scissors against the computer and updates the scores.

  Args:
      user_score: The current user score.
      computer_score: The current computer score.

  Returns:
      tuple: A tuple containing the updated user score and computer score.
  """

    # Available options for the computer
    options = ["rock", "paper", "scissors"]

    # Get user input
    user_choice = input("Choose rock, paper, or scissors (r/p/s): ").lower()

    # Validate user input
    if user_choice not in ("r", "p", "s"):
        print("Invalid input. Please enter r, p, or s.")
        return user_score, computer_score

    # Convert user input to full word representation
    user_choice = ["rock", "paper", "scissors"][["r", "p", "s"].index(user_choice)]

    # Get computer's random choice
    computer_choice = random.choice(options)

    # Determine winner and update scores
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    # Reveal choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Return updated scores
    return user_score, computer_score


def play_three_rounds():
    """
  Plays three rounds of Rock-Paper-Scissors against the computer.

  Returns:
    None
  """

    user_score = 0
    computer_score = 0

    for i in range(3):
        print(f"\nRound {i + 1}")
        user_score, computer_score = play_rock_paper_scissors(user_score, computer_score)  # Pass current scores

    # Print final scores
    print(f"\nFinal Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    if user_score > computer_score:
        print("You win the game!")
    elif user_score < computer_score:
        print("You lose the game.")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    play_three_rounds()
