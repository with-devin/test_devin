from max_value import find_max

def test_find_max():
    result = find_max([1, 2, 3, 4, 5])
    print(f"Test 1 - Positive numbers: find_max([1, 2, 3, 4, 5]) = {result}")
    assert result == 5
    
    result = find_max([-5, -4, -3, -2, -1])
    print(f"Test 2 - Negative numbers: find_max([-5, -4, -3, -2, -1]) = {result}")
    assert result == -1
    
    result = find_max([-10, 0, 10])
    print(f"Test 3 - Mixed numbers: find_max([-10, 0, 10]) = {result}")
    assert result == 10
    
    result = find_max([5, 5, 5])
    print(f"Test 4 - Duplicate values: find_max([5, 5, 5]) = {result}")
    assert result == 5
    
    result = find_max([42])
    print(f"Test 5 - Single value: find_max([42]) = {result}")
    assert result == 42
    
    print("Test 6 - Empty list: Testing find_max([]) raises ValueError")
    try:
        find_max([])
        assert False, "Expected ValueError for empty list"
    except ValueError as e:
        print(f"  Correctly raised ValueError: {e}")
        assert True
    
    print("\nAll tests passed successfully!")

if __name__ == "__main__":
    test_find_max()
