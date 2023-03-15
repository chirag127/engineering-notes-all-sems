Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a content on the topic: 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs. Here is the content I have written in markdown format:

# 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

- A word is a sequence of characters that is separated by spaces or punctuation marks.
- A file is a collection of data that is stored in a permanent or temporary storage device.
- To check whether a given word exists in a file or not, we need to perform the following steps:
  - Open the file in read mode using the `open()` function.
  - Read the contents of the file using the `read()` method.
  - Split the contents of the file into a list of words using the `split()` method.
  - Use the `in` operator to check if the given word is present in the list of words.
  - If the word is present, use the `count()` method to find the number of times it occurs in the list of words.
  - If the word is not present, print a message indicating that the word does not exist in the file.
  - Close the file using the `close()` method.
- Here is an example of a Python program that implements the above steps:

```python
# Define the file name and the word to search
file_name = "sample.txt"
word = "hello"

# Open the file in read mode
file = open(file_name, "r")

# Read the contents of the file
contents = file.read()

# Split the contents into a list of words
words = contents.split()

# Check if the word is present in the list of words
if word in words:
  # Find the number of times the word occurs
  count = words.count(word)
  # Print the result
  print(f"The word '{word}' exists in the file '{file_name}' and occurs {count} times.")
else:
  # Print a message indicating that the word does not exist
  print(f"The word '{word}' does not exist in the file '{file_name}'.")

# Close the file
file.close()
```