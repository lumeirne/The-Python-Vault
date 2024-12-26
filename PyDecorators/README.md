# Python Decorators

## Introduction

Decorators are a powerful and useful tool in Python that allow programmers to modify the behavior of a function or class method without changing the actual code. They are often used to add functionality to existing code in a clean and readable way.

## Definition

A decorator is a function that takes another function as an argument and extends or alters its behavior. Decorators are commonly used for logging, access control, memoization, and more.

## Example

Here is an example of a decorator that prints the execution time.

* The syntax for the decorator function:-
* Consider below example
* `execution_time` is a decorator function which takes the 'function as argument that we want to wrap'. In the below example `lengthofSubstring` is function that needs to wrapped.
* Remember the 'decorator function' should always returns the 'inner function' and 'wrapper function' should call inside the 'inner function'.
* In the below example 
   - 'decorator function': `execution_time`
   - 'inner function'    : `wrapper`
   - 'wrapper function'  : `lengthofSubstring`

```python
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

    n = len(text)
    maxLength = 0
    charMap = {}

    start = 0

    for i in range(n):
        if text[i] in charMap:
            charMap[text[i]] = i
            start = charMap[text[i]] + 1
        elif text[i] not in charMap or charMap[text[i]] < start:
            maxLength = max(maxLength, i - start + 1)
            charMap[text[i]] = i

    return maxLength


print(lengthofSubstring("aerfaderrerdfjlj"))  # 4
```

* In this example, the `execution_time` function is used to wrap the `lengthofSubstring` function, adding additional behavior before and after the original function call.
* `@execution_time` using this line is similar to assigning a variable to the function.(`getMax=execution_time(lengthofSubstring)`)

## Usage

* Decorators are a key feature in Python and are widely used in various frameworks and libraries to enhance functionality and maintain clean code.
* You can use decorators in various practical scenarios, such as logging, enforcing access control, caching results, or measuring execution time. 

