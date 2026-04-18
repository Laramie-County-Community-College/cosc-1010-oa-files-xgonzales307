# filename: 08_Files_Modify_2.py
"""
Activity: Modify the Code

This program asks for a filename and tries to read it. If you type a filename
that doesn't exist (e.g., "nonexistent_file.txt"), the program will crash.

Your goal:
1.  Wrap the file operations in a `try...except` block.
2.  Specifically, you should catch the `FileNotFoundError`.
3.  If the file is not found, print a friendly error message like
    "Error: That file could not be found." instead of crashing.
"""

filename = input("Enter the filename to read: ")

# --- MODIFY THE CODE BELOW ---
# Add a try...except block to handle a FileNotFoundError

try:
    # Attempt to open and read the file
    file = open(filename, "r")
    content = file.read()
    file.close()

    # If successful, print the content
    print("\n--- File Content ---")
    print(content)
    print("--------------------")

except FileNotFoundError:
    # This block executes only if the filename provided does not exist
    print(f"\nError: The file '{filename}' could not be found.")
except Exception as e:
    # This block catches any other unexpected errors (e.g., permission issues)
    print(f"\nAn unexpected error occurred: {e}")

# --- END MODIFICATION ---
