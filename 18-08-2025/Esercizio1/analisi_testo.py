# Imports
import os
import re


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

def count_words(text: str) -> int:
    """Count words number in a string."""
    # Removes punctuation and makes everything lowercase
    words = re.findall(r"\b\w+\b", text.lower())
    return len(words)


# Main
if __name__ == "__main__":
    content = read_file("input.txt")
    if content is not None:
        line_count = count_lines(content)
        word_count = count_words(content)
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
