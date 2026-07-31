## 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

Here are the steps to check whether a given word exists in a file or not and find the number of times it occurs:

1. Open the file: To check whether a given word exists in a file, we need to first open the file in read mode. This can be done using the `open()` function in Python.

2. Read the file: Once the file is open, we can read its contents using the `read()` function. This will return the entire contents of the file as a string.

3. Split the contents: After reading the file, we can split the contents into individual words using the `split()` function. This will create a list of words.

4. Count the occurrence: We can then loop through the list of words and check whether the given word exists in the list. If it does, we can increment a counter to keep track of the number of times the word occurs.

5. Display the result: Finally, we can display the number of times the word occurs in the file.

Here's the Python code for the above steps:

```python
# Open the file
with open('filename.txt', 'r') as file:
    # Read the file
    contents = file.read()
    # Split the contents into words
    words = contents.split()
    # Initialize the counter
    count = 0
    # Loop through the words and count the occurrence
    for word in words:
        if word == 'given_word':
            count += 1
    # Display the result
    print('The word occurs', count, 'times in the file.')
```

Make sure to replace `filename.txt` with the name of your file and `given_word` with the word you want to search for.

That's it! With these simple steps, you can easily check whether a given word exists in a file and find the number of times it occurs.