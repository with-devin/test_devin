from max_value import find_max

def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    
    assert find_max([-5, -4, -3, -2, -1]) == -1
    
    assert find_max([-10, 0, 10]) == 10
    
    assert find_max([5, 5, 5]) == 5
    
    assert find_max([42]) == 42
    
    try:
        find_max([])
        assert False, "Expected ValueError for empty list"
    except ValueError:
        assert True
    
    print("All tests passed!")

if __name__ == "__main__":
    test_find_max()
