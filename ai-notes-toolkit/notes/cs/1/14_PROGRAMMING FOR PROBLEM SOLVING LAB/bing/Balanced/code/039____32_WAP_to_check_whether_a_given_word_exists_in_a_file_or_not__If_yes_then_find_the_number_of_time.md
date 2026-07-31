Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a content on the topic: 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs. Here is the content:

```markdown
# 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

- A file is a collection of data stored in a disk with a specific name and a directory path.
- A word is a sequence of characters separated by spaces or punctuation marks.
- To check whether a given word exists in a file or not, we need to perform the following steps:
  - Open the file in read mode using the `open()` function.
  - Read the contents of the file using the `read()` method.
  - Split the contents into a list of words using the `split()` method.
  - Use the `in` operator to check if the given word is present in the list of words.
  - If the word is present, use the `count()` method to find the number of times it occurs in the list of words.
  - If the word is not present, print a message saying that the word does not exist in the file.
  - Close the file using the `close()` method.
- Here is an example of a Python program that implements the above steps:

```python
# Open the file in read mode
file = open("sample.txt", "r")

# Read the contents of the file
contents = file.read()

# Split the contents into a list of words
words = contents.split()

# Ask the user to enter a word to search
word = input("Enter a word to search: ")

# Check if the word is present in the list of words
if word in words:
  # Find the number of times the word occurs in the list of words
  count = words.count(word)
  # Print the result
  print(f"The word {word} exists in the file and occurs {count} times.")
else:
  # Print a message saying that the word does not exist in the file
  print(f"The word {word} does not exist in the file.")

# Close the file
file.close()
```
```