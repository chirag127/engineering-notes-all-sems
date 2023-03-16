Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write on the topic of reading a file line by line and printing the word count of each line. Here is the content in markdown format:

#### Reading a file line by line and printing the word count of each line

- To read a file line by line, we can use a loop with the `readline()` method of the file object. This method returns a string containing one line of the file, or an empty string if the end of the file is reached.
- To print the word count of each line, we can use the `split()` method of the string object. This method returns a list of words separated by whitespace characters. The length of the list is the word count of the line.
- Here is an example of Python code that reads a file named `sample.txt` and prints the word count of each line:

```python
# Open the file in read mode
file = open("sample.txt", "r")

# Loop through the file line by line
for line in file:
  # Remove the newline character at the end of the line
  line = line.strip()
  # Split the line into words
  words = line.split()
  # Print the word count of the line
  print(len(words))

# Close the file
file.close()
```