# How to read a file line by line and print the word count of each line

- To read a file line by line, we need to open the file in read mode and use a loop to iterate over the lines of the file.
- To print the word count of each line, we need to split the line by whitespace characters and count the length of the resulting list.
- Here is an example of how to do this in Python:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Loop over the lines of the file
for line in file:
  # Split the line by whitespace characters
  words = line.split()
  # Count the length of the list
  word_count = len(words)
  # Print the word count of the line
  print(word_count)

# Close the file
file.close()
```