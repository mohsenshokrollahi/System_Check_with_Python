import os

def rename_files(directory, pattern, new_pattern):
    """Renames files in the specified directory based on a pattern."""

    for filename in os.listdir(directory):
        if pattern in filename:
            old_path = os.path.join(directory, filename)
            new_name = filename.replace(pattern, new_pattern)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")


# Note: The “if __ name __ == '__ main __'” statement in Python checks if the current script is being run directly as the main program, 
# or if it's being imported as a module into another program. __name__ is a variable that exists in every Python module, and is set to the name of the module
if __name__ == "__main__":
    directory = "/Users/mosen.shokr/Documents/test"  # Replace with your directory path
    pattern = "test"  # Replace with the pattern you want to replace
    new_pattern = "test1"  # Replace with the new pattern

    rename_files(directory, pattern, new_pattern)