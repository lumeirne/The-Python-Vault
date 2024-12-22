#Simple generator function that yields 1, 2, and 3
def simple_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
for value in simple_generator():
    print(value)

#Example 1 using range to get the square of numbers
def square_generator(limit):
    """
    Generate the square of numbers up to a specified limit.

    Args:
        limit (int): The upper limit for the square generation. The generator will produce the square of numbers up to this limit.

    Yields:
        int: The square of the next number.
    """
    for i in range(limit):
        yield i ** 2

#Using the square generator
for value in square_generator(5):
    print(value)

#Example 2 using fibonacci series
def fibonacci_generator(limit):
    """
    Generate Fibonacci numbers up to a specified limit.

    Args:
        limit (int): The upper limit for the Fibonacci sequence generation. The generator will produce Fibonacci numbers less than this limit.

    Yields:
        int: The next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

#Remember when using the generator, if you call the function directly(normal way) you will get the generator object
print(fibonacci_generator) #<function fibonacci_generator at 0x7f8b3f7b7d30> 

#To get the values, you need to iterate over the generator object like below
# Using the Fibonacci generator
for value in fibonacci_generator(10):
    print(value)