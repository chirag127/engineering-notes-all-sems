Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a content on the topic ## 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

Here is the content I have written in markdown format:

## 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

- A word is a sequence of characters that is separated by spaces or punctuation marks.
- To check whether a given word exists in a file or not, we need to read the file line by line and split each line into words using the `split()` method.
- Then we need to compare each word with the given word using the `==` operator or the `lower()` method to ignore the case sensitivity.
- If the word matches, we need to increment a counter variable by one to keep track of the number of occurrences.
- If the word does not match, we need to continue the loop and check the next word.
- After reading all the lines in the file, we need to check the value of the counter variable. If it is zero, it means the word does not exist in the file. If it is positive, it means the word exists in the file and the counter variable is the number of times it occurs.
- We can display the result using the `print()` function.

- Here is an example of a Python program that implements the above logic:

```python
# Open the file in read mode
file = open("sample.txt", "r")

# Ask the user to enter a word to search
word = input("Enter a word to search: ")

# Initialize a counter variable to zero
count = 0

# Read the file line by line
for line in file:
  # Split the line into words
  words = line.split()
  # Loop through each word in the line
  for w in words:
    # Convert the word and the given word to lowercase
    w = w.lower()
    word = word.lower()
    # Compare the word and the given word
    if w == word:
      # Increment the counter by one
      count += 1

# Close the file
file.close()

# Check the value of the counter
if count == 0:
  # Print the word does not exist in the file
  print(f"The word '{word}' does not exist in the file.")
else:
  # Print the word exists in the file and the number of times it occurs
  print(f"The word '{word}' exists in the file {count} times.")
```

- Here is a sample output of the program:

```
Enter a word to search: hello
The word 'hello' exists in the file 3 times.
```

- Here is another sample output of the program:

```
Enter a word to search: bye
The word 'bye' does not exist in the file.
```