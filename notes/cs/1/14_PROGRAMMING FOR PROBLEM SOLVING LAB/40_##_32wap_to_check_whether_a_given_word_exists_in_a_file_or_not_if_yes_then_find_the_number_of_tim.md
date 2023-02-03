## 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

Here's one way to do it in Python:
```
def count_word(file_name, word):
    with open(file_name, "r") as file:
        text = file.read()
        word_count = text.count(word)
        if word_count > 0:
            return f"{word} found {word_count} times in {file_name}"
        else:
            return f"{word} not found in {file_name}"

file_name = "example.txt"
word = "hello"
print(count_word(file_name, word))
```
