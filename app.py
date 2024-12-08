"""Example of a clean Python script with perfect pylint score"""

def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"


def calculate_sum(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def main() -> None:
    """Main function to demonstrate greeting and sum calculation."""
    try:
        name = "Alice"
        print(greet(name))
        result = calculate_sum(5, 3)
        print(f"The sum is: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

