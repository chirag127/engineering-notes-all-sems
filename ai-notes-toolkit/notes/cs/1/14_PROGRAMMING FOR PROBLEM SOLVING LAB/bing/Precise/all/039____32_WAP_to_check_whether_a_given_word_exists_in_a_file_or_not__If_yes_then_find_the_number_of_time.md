## 32. WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

Here is a Python program that checks whether a given word exists in a file or not. If the word exists, the program also finds the number of times it occurs:

```python
def check_word_in_file(file_name, word):
    with open(file_name, 'r') as file:
        data = file.read()
        words = data.split()
        count = words.count(word)
        if count > 0:
            print(f"The word '{word}' exists in the file '{file_name}' and it occurs {count} times.")
        else:
            print(f"The word '{word}' does not exist in the file '{file_name}'.")
```

To use this function, you need to provide the name of the file and the word you want to search for as arguments. For example, if you want to check if the word "example" exists in a file named "test.txt", you can call the function like this:

```python
check_word_in_file('test.txt', 'example')
```

This program reads the content of the file, splits it into a list of words, and then counts the number of times the given word occurs in the list. If the count is greater than 0, it means the word exists in the file and the program prints the number of times it occurs. Otherwise, it prints that the word does not exist in the file.