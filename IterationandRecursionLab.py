def factorial_iterative(n):
  """
  Calculates the factorial of a number using an iterative approach.

  Args:
    n: The number to calculate the factorial of.

  Returns:
    The factorial of n.
  """
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result


def factorial_recursive(n):
  """
  Calculates the factorial of a number using a recursive approach.

  Args:
    n: The number to calculate the factorial of.

  Returns:
    The factorial of n.
  """
  if n == 0:
    return 1
  else:
    return n * factorial_recursive(n - 1)


# Calculate factorials for different values
numbers = [5, 10, 25, 50, 100]

print("Factorial results using an iterative function")
for number in numbers:
  print(f"{number}! = {factorial_iterative(number)}")

print("\nFactorial results using a recursive function")
for number in numbers:
  print(f"{number}! = {factorial_recursive(number)}")
