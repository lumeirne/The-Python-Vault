# Python Generators

Generators are a simple and powerful tool for creating iterators. They allow you to iterate through a sequence of values without creating and storing the entire sequence in memory.

## Creating a Generator

A generator in Python is created using a function with the `yield` statement. Here is an example:

```python
def simple_generator():
    yield 1
    yield 2
    yield 3
```

You can use this generator as follows:

```python
gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
```

## Generator Expressions

Generator expressions provide an easy way to create generators. They are similar to list comprehensions but use parentheses instead of square brackets.

Example:

```python
gen_exp = (x **2 for x in range(5))
for num in gen_exp:
    print(num)
```

Output:
```
0
1
4
9
16
25
```

## Examples'square generator' and 'fibonacci generator'

You can find the code for 'square generator' and 'fibonacci generator' [here](./generators.py)

## Advantages of Generators

- **Memory Efficiency**: Generators do not store the entire sequence in memory. Unlike normal iterators.
- **Lazy Evaluation**: Values are produced only when needed.
- **Improved Performance**: Generators can be faster than list comprehensions for large datasets.

## Use Cases

- Reading large files line by line.
- Generating an infinite sequence of numbers.
- Implementing pipelines for data processing.

## Conclusion

Generators are a powerful feature in Python that can help you write more efficient and readable code. They are particularly useful when working with large datasets or streams of data.
