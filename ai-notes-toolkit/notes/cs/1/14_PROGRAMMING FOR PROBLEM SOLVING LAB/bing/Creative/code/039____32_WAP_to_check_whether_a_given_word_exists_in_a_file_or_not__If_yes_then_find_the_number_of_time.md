Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write the content on the topic: 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs. Here is the content in markdown format:

## 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

- To check whether a given word exists in a file or not, we can use the `in` operator to search for the word in each line of the file.
- To find the number of times it occurs, we can use a variable to count the occurrences of the word in each line and add them up.
- We can use the `open()` function to open the file in read mode and the `close()` function to close the file after reading.
- We can use a `for` loop to iterate over each line of the file and use the `strip()` method to remove any whitespace characters from the line.
- We can use an `if` statement to check if the word is in the line and increment the count variable if it is.
- We can use an `else` statement to print a message if the word is not found in the file.
- We can use the `print()` function to display the count variable and the word at the end.

Here is an example of a Python program that implements the above logic:

```python
# WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

# Open the file in read mode
file = open("sample.txt", "r")

# Initialize the count variable to zero
count = 0

# Ask the user to enter the word to search
word = input("Enter the word to search: ")

# Loop through each line of the file
for line in file:

  # Remove any whitespace characters from the line
  line = line.strip()

  # Check if the word is in the line
  if word in line:

    # Increment the count variable by the number of occurrences of the word in the line
    count += line.count(word)

# Close the file
file.close()

# Check if the count variable is greater than zero
if count > 0:

  # Print the count variable and the word
  print(f"The word '{word}' occurs {count} times in the file.")

else:

  # Print a message that the word is not found in the file
  print(f"The word '{word}' does not exist in the file.")
```