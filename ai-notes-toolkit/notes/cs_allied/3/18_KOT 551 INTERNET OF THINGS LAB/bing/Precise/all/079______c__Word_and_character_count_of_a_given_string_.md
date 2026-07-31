#### c) Word and character count of a given string

- To count the number of words in a string, we can split the string into a list of words using the `split()` method and then find the length of the list using the `len()` function.
- To count the number of characters in a string, we can use the `len()` function directly on the string.
- For example, consider the string `"Hello, World!"`. The word count can be found using the following code:
```python
string = "Hello, World!"
words = string.split()
word_count = len(words)
print(word_count)
```
This will output `2`, as there are two words in the string.
- The character count can be found using the following code:
```python
string = "Hello, World!"
char_count = len(string)
print(char_count)
```
This will output `13`, as there are 13 characters in the string, including spaces and punctuation.
- It is important to note that the `split()` method splits the string at whitespace characters by default. If the string contains multiple consecutive spaces or other whitespace characters, they will be treated as a single delimiter. If a different delimiter is desired, it can be passed as an argument to the `split()` method.