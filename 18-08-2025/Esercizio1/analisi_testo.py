# Imports
import os
import re
from collections import Counter


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

def top_5_words(text: str):
    """Find top 5 most frequent words."""
    words = re.findall(r"\b\w+\b", text.lower())
    counter = Counter(words)
    return counter.most_common(5)



# Main
if __name__ == "__main__":
    content = read_file("input.txt")
    if content is not None:
        # Compute
        line_count = count_lines(content)
        word_count = count_words(content)
        top_5 = top_5_words(content)
        # Print
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Top 5 words: {top_5}")
