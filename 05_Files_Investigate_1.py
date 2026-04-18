 
# filename: 05_Files_Investigate_1.py
"""
Activity: Investigate the Code

1.  Run this program **once**. A file named `log.txt` will be created.
    Open `log.txt` in your file explorer to see its content. It should say "First entry."

2.  Now, run this program a **second time**. Check the content of `log.txt` again.

3.  Change the mode in the `open()` function from "w" to "a".

4.  Run the program a **third time**. Check `log.txt`.

5.  Run the program a **fourth time**. Check `log.txt`.

6.  Answer the questions below in comments.

Questions:
1. What happened to the content of `log.txt` when you ran the program the second time (while in 'w' mode)?
   # Your Answer Here: it overwrote the existing content of `log.txt`, so it only contained "First entry." after the second run.

2. What happened to the content of `log.txt` when you ran the program the third and fourth times (while in 'a' mode)?
   # Your Answer Here: it appended the new content to the existing content of `log.txt`, so it contained both "First entry." and "New entry." after the third and fourth runs.

3. What is the key difference between 'w' (write) mode and 'a' (append) mode?
   # Your Answer Here: 'w' mode overwrites the entire file each time it is opened, while 'a' mode appends new content to the end of the file without affecting existing content.
"""

# Change the mode below from "w" to "a" after the second run
file = open("log.txt", "a")

file.write("New entry.\n")

file.close()

print("Wrote a new entry to log.txt")
