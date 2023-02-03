interval of 10 seconds. d) Read a file line by line and print the word count of each line.

Sure! Let's talk about reading a file line by line and printing the word count of each line in Python programming language.

To read a file line by line and print the word count of each line, you can use the following code in Python:

```
# Open the file for reading
with open("file.txt", "r") as file:
    # Loop through each line in the file
    for line in file:
        # Strip the line of any leading or trailing whitespace
        line = line.strip()
        # Split the line into words
        words = line.split()
        # Print the word count for the line
        print("Line word count:", len(words))
```

This code uses the `with` statement to open the file for reading, which automatically closes the file when the block of code is finished. The code then loops through each line in the file using a `for` loop, and uses the `strip` method to remove any leading or trailing whitespace from the line. The code then splits the line into words using the `split` method, and uses the `len` function to get the number of words in the line. Finally, the code prints the word count for the line using the `print` function.

In conclusion, to read a file line by line and print the word count of each line in Python, you can use the code shown above, which uses the `with` statement to open the file for reading, loops through each line in the file, removes any leading or trailing whitespace from the line, splits the line into words, and prints the word count for the line.
