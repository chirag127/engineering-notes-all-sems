# How to read a file line by line and print the word count of each line

- To read a file line by line, we can use a loop and the `readline()` method of the file object.
- The `readline()` method returns a string containing the next line of the file, or an empty string if the end of the file is reached.
- To print the word count of each line, we can use the `split()` method of the string object and the `len()` function.
- The `split()` method returns a list of words in the string, separated by whitespace characters by default.
- The `len()` function returns the number of items in a list or any other iterable object.
- Here is an example of Python code that reads a file line by line and prints the word count of each line:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Loop through the file line by line
while True:
  # Read the next line
  line = file.readline()

  # Break the loop if the line is empty
  if not line:
    break

  # Split the line into words
  words = line.split()

  # Print the word count of the line
  print(len(words))

# Close the file
file.close()
```