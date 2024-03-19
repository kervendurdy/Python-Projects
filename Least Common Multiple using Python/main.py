def lcm_listing_multiples(numbers):
    """
  Calculates the Least Common Multiple (LCM) of a list of integers using listing multiples method.

  Args:
      numbers: A list of integers.

  Returns:
      int: The LCM of the numbers in the list, or None if no common multiple is found.
  """

    # Find the maximum number
    max_num = max(numbers)

    # Initialize empty lists to store multiples of each number
    multiples = [[] for _ in numbers]

    # Find multiples of each number up to the maximum number
    for i, num in enumerate(numbers):
        j = 1
        while num * j <= max_num:
            multiples[i].append(num * j)
            j += 1

    # Find the first common multiple that appears in all lists
    lcm = None
    for multiple in multiples[0]:
        if all(multiple in lst for lst in multiples[1:]):
            lcm = multiple
            break

    # If no common multiple found, calculate product of all numbers
    if lcm is None:
        lcm = 1
        for num in numbers:
            lcm *= num

    return lcm


# Get number of integers from the user
num_integers = int(input("Enter the number of integers: "))

# Get the integers from the user
numbers = []
for i in range(num_integers):
    number = int(input(f"Enter integer {i + 1}: "))
    numbers.append(number)

# Calculate and print the LCM
lcm_result = lcm_listing_multiples(numbers)

if lcm_result is not None:
    print(f"The Least Common Multiple (LCM) of the entered numbers is: {lcm_result}")
else:
    print("No common multiple found. Product of all numbers is:", lcm_result)
