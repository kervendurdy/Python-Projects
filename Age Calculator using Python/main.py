from datetime import date


def calculate_age(birth_date_str):
    """
  Calculates age in years given a birth date string in YYYY-MM-DD format.

  Args:
    birth_date_str: A string representing the birth date in YYYY-MM-DD format.

  Returns:
    An integer representing the age in years.
  """

    # Try converting the birth_date string to a datetime object
    try:
        birth_date = date.fromisoformat(birth_date_str)
    except ValueError:
        print("Invalid birth date format. Please use YYYY-MM-DD.")
        return None

    # Get today's date
    today = date.today()

    # Calculate age by subtracting birth year from current year
    # Consider days and months for accurate age calculation
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
        return age
    else:
        return age


if __name__ == "__main__":
    # Get birth_date input from user
    birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")

    # Calculate and display age
    age = calculate_age(birth_date_str)
    if age:
        print(f"Your age is {age} years old.")
