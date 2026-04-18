# filename: 07_Files_Modify_1.py
"""
Activity: Modify the Code

This program is intended to add a new high score to a file every time it runs.
However, it has a bug! It keeps overwriting the file.

Your goal:
1.  Identify the bug in the `open()` function call.
2.  Modify the mode so that it **appends** to the file instead of overwriting it.
3.  Run the program multiple times to confirm that new scores are added to the end.
"""

new_score = input("Enter a new high score: ")

# --- MODIFY THE LINE BELOW ---
# The mode here is incorrect for what we want to do.
file = open("high_scores.txt", "a")  # Change "w" to "a" to append instead of overwrite10
# --- END MODIFICATION ---

file.write(new_score + "\n")

file.close()

print("High score saved!")
