def test_chunk_list():
    """Test cases for the chunk_list function."""
    # Test normal functionality
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list(['a', 'b', 'c', 'd'], 3) == [['a', 'b', 'c'], ['d']]

    # Test edge cases
    assert chunk_list([], 1) == []  # Empty list
    assert chunk_list([1], 1) == [[1]]  # Single-element list
    assert chunk_list([1, 2, 3], 3) == [[1, 2, 3]]  # Chunk size equals list size

    # Test invalid inputs
    try:
        chunk_list([1, 2, 3], 0)  # Invalid chunk size
    except ValueError as e:
        assert str(e) == "chunk_size must be greater than 0"

    try:
        chunk_list("not_a_list", 2)  # Non-list data
    except TypeError as e:
        assert str(e) == "data must be a list"

    try:
        chunk_list([1, 2, 3], "not_an_int")  # Non-integer chunk size
    except TypeError as e:
        assert str(e) == "chunk_size must be an integer"


def test_flatten_nested():
    """Test cases for the flatten_nested function."""
    # Test normal functionality
    assert flatten_nested([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
    assert flatten_nested([]) == []  # Empty list
    assert flatten_nested([1, 2, 3]) == [1, 2, 3]  # Already flat list

    # Test edge cases
    assert flatten_nested([[[]]]) == []  # Deeply nested empty list
    assert flatten_nested([[], [1], [[2]]]) == [1, 2]  # Mixed empty and values

    # Test invalid inputs
    try:
        flatten_nested("not_a_list")  # Non-list input
    except TypeError as e:
        assert str(e) == "nested_list must be a list"


def test_timeit_decorator():
    """Test cases for the timeit_decorator function."""

    @timeit_decorator
    def quick_function():
        return "quick"

    @timeit_decorator
    def slow_function():
        time.sleep(1)
        return "slow"

    # Test normal functionality
    assert quick_function() == "quick"  # Check return value
    assert slow_function() == "slow"  # Check return value

    # Test invalid input
    try:
        timeit_decorator("not_callable")  # Non-callable input
    except TypeError as e:
        assert str(e) == "func must be callable"
