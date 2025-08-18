# Imports
import os


# Functions
def read_file(path="input.txt"):
    """Read file content, if file exists."""
    if not os.path.exists(path):
        print(f"Error: File '{path}' not found.")
        return None

    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        return content

def count_lines(text: str) -> int:
    """Count line number."""
    return len(text.splitlines())


# Main
if __name__ == "__main__":
    content = read_file("input.txt")
    if content is not None:
        line_count = count_lines(content)
        print(f"Number of lines: {line_count}")
