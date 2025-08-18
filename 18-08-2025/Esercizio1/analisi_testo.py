# Imports
import os


def read_file(path="input.txt"):
    """Read file content, if file exists."""
    if not os.path.exists(path):
        print(f"Error: File '{path}' not found.")
        return None

    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

        return content


if __name__ == "__main__":
    content = read_file("input.txt")
