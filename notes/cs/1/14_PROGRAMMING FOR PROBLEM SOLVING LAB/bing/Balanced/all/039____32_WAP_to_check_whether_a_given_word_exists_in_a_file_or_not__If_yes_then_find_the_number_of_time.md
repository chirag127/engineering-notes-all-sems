## 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

- A word is a sequence of characters separated by spaces or punctuation marks.
- A file is a collection of data stored in a disk or memory.
- To check whether a given word exists in a file or not, we need to read the file line by line and split each line into words.
- Then we need to compare each word with the given word and count the number of matches.
- If the count is greater than zero, then the word exists in the file and we can print the count.
- If the count is zero, then the word does not exist in the file and we can print a message accordingly.
- We can use the `open()` function to open the file in read mode and the `close()` function to close the file after reading.
- We can use the `for` loop to iterate over the lines of the file and the `split()` method to split each line into words.
- We can use the `==` operator to compare two words and the `+=` operator to increment the count.
- We can use the `print()` function to display the output.

- Here is an example of a Python program that checks whether a given word exists in a file or not. If yes then finds the number of times it occurs.

```python
# open the file in read mode
file = open("sample.txt", "r")

# input the word to search
word = input("Enter the word to search: ")

# initialize the count to zero
count = 0

# loop through the lines of the file
for line in file:
  # split the line into words
  words = line.split()
  # loop through the words
  for w in words:
    # compare the word with the given word
    if w == word:
      # increment the count
      count += 1

# close the file
file.close()

# check if the count is greater than zero
if count > 0:
  # print the count
  print(f"The word '{word}' exists in the file and occurs {count} times.")
else:
  # print a message
  print(f"The word '{word}' does not exist in the file.")
```

- Here is an example of the output of the program.

```
Enter the word to search: hello
The word 'hello' exists in the file and occurs 3 times.
```