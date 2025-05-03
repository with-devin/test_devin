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
