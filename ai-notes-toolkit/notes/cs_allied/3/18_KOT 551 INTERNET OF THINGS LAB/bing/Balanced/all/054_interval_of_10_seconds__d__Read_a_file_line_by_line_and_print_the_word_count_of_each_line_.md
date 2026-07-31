# How to read a file line by line and print the word count of each line

- To read a file line by line, we can use a loop with the `readline()` method of the file object. This method returns a string containing the next line of the file, or an empty string if the end of the file is reached.
- To print the word count of each line, we can use the `split()` method of the string object. This method returns a list of words in the string, separated by whitespace characters. We can then use the `len()` function to get the number of elements in the list, which is the word count of the line.
- Here is an example of Python code that reads a file line by line and prints the word count of each line:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Loop through the file line by line
for line in file:
  # Remove the newline character at the end of the line
  line = line.strip()
  # Split the line into words
  words = line.split()
  # Get the word count of the line
  word_count = len(words)
  # Print the word count of the line
  print(word_count)

# Close the file
file.close()
```