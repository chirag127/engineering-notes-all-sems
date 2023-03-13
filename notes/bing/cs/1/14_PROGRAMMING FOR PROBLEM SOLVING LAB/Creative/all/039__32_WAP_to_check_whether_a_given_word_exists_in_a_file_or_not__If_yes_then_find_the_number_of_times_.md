## 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

- WAP stands for Write A Program, which is a common abbreviation used in programming assignments and questions.
- To check whether a given word exists in a file or not, we need to perform the following steps:
  - Open the file in read mode using the `open()` function.
  - Read the contents of the file using the `read()` method, which returns a string.
  - Split the string into a list of words using the `split()` method, which separates the words by whitespace characters by default.
  - Use the `in` operator to check if the given word is present in the list of words, which returns a boolean value.
  - If the word is present, use the `count()` method to find the number of times it occurs in the list of words, which returns an integer value.
  - Close the file using the `close()` method.
- Here is an example of a Python program that implements the above steps:

```python
# Define the file name and the word to search
file_name = "sample.txt"
word = "hello"

# Open the file in read mode
file = open(file_name, "r")

# Read the contents of the file
content = file.read()

# Split the content into a list of words
words = content.split()

# Check if the word is present in the list of words
if word in words:
  # Find the number of times the word occurs
  count = words.count(word)
  # Print the result
  print(f"The word '{word}' exists in the file '{file_name}' and occurs {count} times.")
else:
  # Print the result
  print(f"The word '{word}' does not exist in the file '{file_name}'.")

# Close the file
file.close()
```

- Here is a possible output of the program, assuming the file `sample.txt` contains the following text:

```
Hello, world!
This is a sample file.
Hello, hello, hello!
```

```
The word 'hello' exists in the file 'sample.txt' and occurs 4 times.
```

- A possible mnemonic to remember the steps of the program is:

  - **O**pen the file
  - **R**ead the content
  - **S**plit the content
  - **C**heck the word
  - **F**ind the count
  - **P**rint the result
  - **C**lose the file

  - Which can be memorized as **ORSCFPC** or **Oranges Can Fly Past Clouds**.