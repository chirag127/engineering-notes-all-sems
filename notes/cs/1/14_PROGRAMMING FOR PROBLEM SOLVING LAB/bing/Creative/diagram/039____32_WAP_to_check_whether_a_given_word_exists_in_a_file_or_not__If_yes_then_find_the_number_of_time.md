Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write the content in markdown format on the topic: 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs. Here is the content:

## 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

- To check whether a given word exists in a file or not, we can use the `in` operator to search for the word in each line of the file.
- To find the number of times the word occurs, we can use a variable to count the occurrences of the word in each line and add them up.
- We can use the `open()` function to open the file in read mode and the `close()` function to close the file after reading.
- We can use a `try-except` block to handle any errors that may occur while opening or reading the file.
- Here is an example of a Python program that checks whether the word "hello" exists in a file named "test.txt" and finds the number of times it occurs:

```python
# open the file in read mode
try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("File not found")
    exit()

# initialize the count variable
count = 0

# loop through each line of the file
for line in file:
    # check if the word "hello" is in the line
    if "hello" in line:
        # increment the count by the number of occurrences of the word in the line
        count += line.count("hello")

# close the file
file.close()

# print the result
if count > 0:
    print(f"The word 'hello' exists in the file and occurs {count} times.")
else:
    print("The word 'hello' does not exist in the file.")
```