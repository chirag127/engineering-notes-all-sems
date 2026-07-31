# How to read a file line by line and print the word count of each line

- To read a file line by line, we need to open the file in read mode and use a loop to iterate over the lines of the file.
- To print the word count of each line, we need to split the line by whitespace characters and count the length of the resulting list.
- Here is an example of Python code that performs this task:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Loop over the lines of the file
for line in file:
  # Strip the newline character from the line
  line = line.strip()
  # Split the line by whitespace characters
  words = line.split()
  # Count the number of words in the line
  word_count = len(words)
  # Print the line and the word count
  print(line, ":", word_count)

# Close the file
file.close()
```