# Library of General Utility Functions

## Function 1: `chunk_list`

### Description
The `chunk_list` function splits a list into smaller sublists (chunks) of a specified size. Each sublist contains up to `chunk_size` elements, except the final sublist, which may have fewer elements if the total number of elements in the list is not divisible by `chunk_size`.

### Pre-Conditions
- `data` must be a list.
- `chunk_size` must be a positive integer greater than 0.

### Post-Conditions
- Returns a list of sublists, each of size up to `chunk_size`.

### Complexity
- **Time Complexity**: \( O(n) \), where \( n \) is the length of `data`.
- **Space Complexity**: \( O(n) \), due to the new list created to hold the chunks.

### Use Cases
- Splitting data for parallel processing.
- Dividing a dataset into smaller batches for training machine learning models.

### Example
```python
>>> chunk_list([1, 2, 3, 4, 5], 2)
[[1, 2], [3, 4], [5]]
```

---

## Function 2: `flatten_nested`

### Description
The `flatten_nested` function takes a nested list of arbitrary depth and returns a single-level list containing all elements from the original nested structure.

### Pre-Conditions
- `nested_list` must be a list. Elements within the list can be of any type, including other lists.

### Post-Conditions
- Returns a flattened list with all elements from the original nested list.

### Complexity
- **Time Complexity**: \( O(n) \), where \( n \) is the total number of elements across all levels of the nested list.
- **Space Complexity**: \( O(n) \), due to the new flattened list created.

### Use Cases
- Preprocessing hierarchical data for analysis.
- Converting nested JSON-like structures into a flat format.

### Example
```python
>>> flatten_nested([1, [2, [3, 4]], 5])
[1, 2, 3, 4, 5]
```

---

## Function 3: `timeit_decorator`

### Description
The `timeit_decorator` is a function decorator that measures and prints the execution time of a decorated function. This can be useful for performance testing and optimization.

### Pre-Conditions
- `func` must be a callable object (e.g., a function or a method).

### Post-Conditions
- Wraps the original function and prints the execution time after it finishes.

### Complexity
- **Time Complexity**: Dependent on the wrapped function.
- **Space Complexity**: \( O(1) \), as it adds negligible overhead.

### Use Cases
- Measuring performance of functions during development.
- Benchmarking computationally expensive operations.

### Example
```python
@timeit_decorator
def slow_function():
    time.sleep(2)

slow_function()
# Output: Function 'slow_function' executed in 2.00 seconds
```
