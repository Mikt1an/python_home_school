
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]


def pipe_str(pipe_string: list) -> str:
    """
    Concatenates elements of a list into a single string separated by " | ".

    Each element is converted to its string representation using str(),
    so complex types such as lists and dictionaries preserve their default format.

    Args:
        pipe_string: A list containing elements of any type.
    Returns:
        string with all elements joined by " | ".
    """
    return " | ".join(str(value) for value in pipe_string)

print(pipe_str(data))

data = [
        {"name": "Alice", "scores": [10, 20, 30]},
        {"name": "Bob", "scores": [5, 15, 25]},
        {"name": "Charlie", "scores": [7, 17, 27]}
        ]

def total_points(tabl: list[dict]) -> int:
    """
    Calculates the total number of points across all tables.
    Args:
        tabl: A list of tables.
    Returns:
        int: Total number of points across all tables.
    """
    return sum(sum(user["scores"]) for user in tabl)

print(total_points(data))
