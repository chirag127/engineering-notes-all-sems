# How to read a file line by line and print the word count of each line

- To read a file line by line, we can use a loop with the `readline()` method of the file object.
- The `readline()` method returns a string containing the next line of the file, or an empty string if the end of the file is reached.
- To print the word count of each line, we can use the `split()` method of the string object.
- The `split()` method returns a list of words in the string, separated by whitespace characters.
- We can use the `len()` function to get the number of elements in the list, which is the word count of the line.
- We can use the `print()` function to display the word count of each line, along with the line itself or its number.
- Here is an example of Python code that reads a file line by line and prints the word count of each line:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Initialize a line number variable
line_number = 1

# Loop through the file line by line
while True:
  # Read the next line
  line = file.readline()

  # Break the loop if the end of the file is reached
  if line == "":
    break

  # Split the line into words
  words = line.split()

  # Get the word count of the line
  word_count = len(words)

  # Print the word count and the line number or the line itself
  print(f"Line {line_number} has {word_count} words.")
  # Alternatively, you can print the line itself instead of the line number
  # print(f"{line.strip()} has {word_count} words.")

  # Increment the line number
  line_number += 1

# Close the file
file.close()
```