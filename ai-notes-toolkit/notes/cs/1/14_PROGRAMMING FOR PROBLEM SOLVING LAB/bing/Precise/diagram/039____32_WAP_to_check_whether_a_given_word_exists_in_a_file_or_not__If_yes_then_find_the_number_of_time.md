## 32. WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

Here is an example of a program that checks whether a given word exists in a file or not. If the word exists, the program will also find the number of times it occurs.

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

This program defines a function `check_word_in_file` that takes two arguments: `file_name` and `word`. The function opens the file with the given file name in read mode and reads its content. Then, it uses the `count` method of strings to count the number of occurrences of the given word in the text. If the word count is greater than 0, the function prints a message indicating that the word was found and the number of times it occurs. Otherwise, it prints a message indicating that the word was not found.

To use this function, you can call it and pass the name of the file and the word you want to search for as arguments. For example:

```python
check_word_in_file('example.txt', 'word')
```

This will check if the word 'word' exists in the file 'example.txt' and print the result.