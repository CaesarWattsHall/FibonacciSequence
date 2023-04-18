# Define a function to generate the Fibonacci sequence
def fibonacci(n):
  # Initialize the first two terms
  a = 0
  b = 1
  # Create an empty list to store the sequence
  sequence = []
  # Loop until the nth term
  for i in range(n):
    # Append the current term to the sequence
    sequence.append(a)
    # Update the next term by adding the previous two terms
    c = a + b
    # Assign the values of b and c to a and b respectively
    a = b
    b = c
  # Return the sequence
  return sequence

# Test the function with some examples
print(fibonacci(5)) # [0, 1, 1, 2, 3]
print(fibonacci(10)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
