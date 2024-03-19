def gcd_looping(numbers):
    """
  Calculates the Greatest Common Divisor (GCD) of a list of integers using looping and checking divisibility.

  Args:
      numbers: A list of integers.

  Returns:
      int: The GCD of all integers in the list, or 1 if no common divisor is found.
  """

    # Find the minimum value from the list
    gcd = min(numbers)

    # Loop through potential divisors from the minimum value down to 1
    while gcd > 0:
        # Check if the current divisor divides all numbers in the list without a remainder
        if all(num % gcd == 0 for num in numbers):
            return gcd
        gcd -= 1

    return 1  # No common divisor found, return 1


# Get the number of integers from the user
num_integers = int(input("Enter the number of integers: "))

# Get integer inputs from the user and store them in a list
numbers = []
for i in range(num_integers):
    number = int(input(f"Enter integer {i + 1}: "))
    numbers.append(number)

# Calculate GCF using the looping approach
gcd_result = gcd_looping(numbers)

if gcd_result == 1:
    print("No common divisor found for the entered numbers.")
else:
    print(f"The Greatest Common Divisor (GCD) of the entered numbers is: {gcd_result}")
