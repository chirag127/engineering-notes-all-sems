## 32. WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

Here is a Python program that checks whether a given word exists in a file or not. If the word exists, the program will also find the number of times it occurs:

```python
def check_word_in_file(file_name, word):
    with open(file_name, 'r') as file:
        text = file.read()
        word_count = text.count(word)
        if word_count > 0:
            print(f"The word '{word}' was found {word_count} times in the file.")
        else:
            print(f"The word '{word}' was not found in the file.")
```

To use this function, you need to provide the name of the file and the word you want to search for as arguments. For example, to search for the word "example" in a file named "test.txt", you would call the function like this:

```python
check_word_in_file('test.txt', 'example')
```

This function works by opening the file in read mode and reading its contents into a string. Then, it uses the `count` method of strings to count the number of times the word appears in the text. If the count is greater than zero, it means the word was found and the function prints a message indicating how many times it was found. Otherwise, it prints a message indicating that the word was not found.