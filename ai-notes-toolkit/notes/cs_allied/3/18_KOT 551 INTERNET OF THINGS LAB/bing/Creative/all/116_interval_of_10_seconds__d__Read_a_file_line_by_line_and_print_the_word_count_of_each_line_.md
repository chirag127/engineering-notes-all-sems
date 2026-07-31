# How to read a file line by line and print the word count of each line

- To read a file line by line, we can use a loop with the `readline()` method of the file object.
- The `readline()` method returns a string containing the next line of the file, or an empty string if the end of the file is reached.
- To print the word count of each line, we can use the `split()` method of the string object, which returns a list of words separated by whitespace characters.
- The `len()` function can be used to get the number of elements in a list, which is the word count of the line.
- We can use a variable to keep track of the line number, and increment it by one in each iteration of the loop.
- We can use the `format()` method of the string object to print the line number and the word count in a formatted way.

- Here is an example of Python code that implements this logic:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Initialize the line number
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

  # Get the word count
  word_count = len(words)

  # Print the line number and the word count
  print("Line {}: {} words".format(line_number, word_count))

  # Increment the line number
  line_number += 1

# Close the file
file.close()
```