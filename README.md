# Find Max Function

A simple Python utility that provides a function to find the maximum value in a list.

## Installation

Clone this repository to get started:

```bash
git clone https://github.com/with-devin/test_devin.git
cd test_devin
```

No additional dependencies are required as this uses only Python's built-in functions.

## Usage

### Basic Usage

```python
from max_value import find_max

# Find maximum in a list of positive numbers
max_value = find_max([1, 2, 3, 4, 5])
print(max_value)  # Output: 5

# Find maximum in a list of negative numbers
max_value = find_max([-5, -4, -3, -2, -1])
print(max_value)  # Output: -1

# Find maximum in a list with mixed numbers
max_value = find_max([-10, 0, 10])
print(max_value)  # Output: 10
```

### Error Handling

The function raises a `ValueError` if an empty list is provided:

```python
try:
    find_max([])
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Cannot find maximum value in an empty list
```

## Running Tests

To run the tests and verify the function works correctly:

```bash
python test_max_value.py
```

This will run all test cases and display the results for each test.

## Function Details

```python
def find_max(numbers):
    """
    Returns the maximum value in a list of numbers.
    
    Args:
        numbers (list): A list of numeric values.
        
    Returns:
        The maximum value in the list.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot find maximum value in an empty list")
    
    return max(numbers)
```
