## 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

- A possible solution to this problem is to use the `open()` function to read the file and the `count()` method to count the occurrences of the word in each line of the file.
- The `open()` function takes the name of the file as an argument and returns a file object that can be used to read or write the file.
- The `count()` method takes a substring as an argument and returns the number of times it appears in the string.
- The algorithm for the solution is as follows:

  - Declare a variable `word` to store the word to be searched and assign it a value.
  - Declare a variable `filename` to store the name of the file and assign it a value.
  - Declare a variable `count` to store the number of occurrences of the word and initialize it to zero.
  - Open the file using the `open()` function and assign the file object to a variable `file`.
  - Use a `for` loop to iterate over each line of the file.
  - Use the `count()` method to count the number of occurrences of the word in the current line and add it to the `count` variable.
  - Close the file using the `close()` method of the file object.
  - Check if the `count` variable is greater than zero. If yes, print the word and the number of occurrences. If no, print that the word does not exist in the file.

- A possible implementation of the solution in Python is as follows:

```python
# Declare the word and the filename
word = "hello"
filename = "sample.txt"

# Initialize the count to zero
count = 0

# Open the file
file = open(filename, "r")

# Loop over each line of the file
for line in file:
  # Count the occurrences of the word in the line
  count += line.count(word)

# Close the file
file.close()

# Check if the word exists in the file
if count > 0:
  # Print the word and the number of occurrences
  print(f"The word '{word}' exists in the file '{filename}' and occurs {count} times.")
else:
  # Print that the word does not exist in the file
  print(f"The word '{word}' does not exist in the file '{filename}'.")
```