import os


def load_instruction_from_file(filepath):
    """Loads instruction from a file.

    Args:
        filepath: The relative path to the instruction file.

    Returns:
        The content of the file as a string.
    """
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error: An error occurred while reading the file: {e}")
        return None
