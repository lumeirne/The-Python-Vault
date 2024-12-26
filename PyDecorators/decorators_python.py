def execution_time(func):
    """
    A decorator that measures and prints the execution time of the decorated function.
    Args:
        func (callable): The function to be decorated.
    Returns:
        callable: The wrapped function with execution time measurement.
    """

    def wrapper(*args, **kwargs):
        """
        A wrapper function that measures the execution time of the decorated function.
        Args:
            *args: Variable length argument list for the decorated function.
            **kwargs: Arbitrary keyword arguments for the decorated function.
        Returns:
            The result of the decorated function.
        Prints:
            The execution time of the decorated function.
        """

        import time
        start = time.time()
        # result stores the result of the wrapped function
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end-start}")
        return result
    return wrapper

# Call the decorator(to call function as a decorator use '@' symbol)
@execution_time
def lengthofSubstring(text: str) -> int:
    """
    Calculate the length of the longest substring without repeating characters.
    Args:
        text (str): The input string to be evaluated.
    Returns:
        int: The length of the longest substring without repeating characters.
    """

    n = len(text)  # Get the length of the input string
    maxLength = 0  # Initialize the maximum length of substring without repeating characters
    charMap = {}  # Dictionary to store the last seen index of each character

    start = 0  # Initialize the starting index of the current substring

    for i in range(n):  # Iterate over each character in the string
        if text[i] in charMap:  # If the character is already in the dictionary
            charMap[text[i]] = i  # Update the last seen index of the character
            start = charMap[text[i]] + 1  # Move the start index to the right of the last seen index
        elif text[i] not in charMap or charMap[text[i]] < start:  # If the character is not in the dictionary or its last seen index is before the start index
            maxLength = max(maxLength, i - start + 1)  # Update the maximum length of substring
            charMap[text[i]] = i  # Update the last seen index of the character

    return maxLength  # Return the maximum length of substring without repeating characters


print(lengthofSubstring("aerfaderrerdfjlj"))  # 3


    