Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write on the topic of reading a file line by line and printing the word count of each line. Here is the content in markdown format:

# Reading a file line by line and printing the word count of each line

- To read a file line by line, we can use the `open()` function to open the file in read mode and then use a `for` loop to iterate over the file object.
- To print the word count of each line, we can use the `split()` method to split the line into a list of words and then use the `len()` function to get the length of the list.
- Here is an example of Python code that reads a file named `sample.txt` and prints the word count of each line:

```python
# Open the file in read mode
file = open("sample.txt", "r")

# Loop over the file object
for line in file:
  # Split the line into a list of words
  words = line.split()
  # Get the length of the list
  word_count = len(words)
  # Print the word count of the line
  print(word_count)

# Close the file
file.close()
```