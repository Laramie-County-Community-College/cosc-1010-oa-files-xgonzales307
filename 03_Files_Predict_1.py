# filename: 03_Files_Predict_1.py
"""
Activity: Predict the Output

1.  Imagine a file named `story.txt` already exists with the content:
    "It was a dark and stormy night."

2.  Read the Python code below.
3.  Without running the code, what do you think the **final content of `story.txt`** will be?
4.  Write your prediction in the `prediction` variable.
"""

# What will be the final text inside story.txt?
prediction = "The sun was shining."

# The 'w' mode stands for 'write'. It will overwrite the file.
file = open("story.txt", "w")

file.write("The sun was shining.")

file.close()

# If you were to open and read "story.txt" now, what would you see?
# You would see: "The sun was shining."
