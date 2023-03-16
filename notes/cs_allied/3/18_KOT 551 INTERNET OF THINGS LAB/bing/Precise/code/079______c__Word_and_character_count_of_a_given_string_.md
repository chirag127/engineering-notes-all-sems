#### c) Word and character count of a given string.

- To count the number of words in a given string, we can split the string into a list of words using the `split()` method and then find the length of the list using the `len()` function.
- To count the number of characters in a given string, we can use the `len()` function directly on the string.
- For example, consider the string `"Hello, World!"`. The word count of this string can be found using the following code:
```python
string = "Hello, World!"
words = string.split()
word_count = len(words)
print(word_count)
```
This code will output `2`, indicating that there are 2 words in the given string.
- Similarly, the character count of the string can be found using the following code:
```python
string = "Hello, World!"
char_count = len(string)
print(char_count)
```
This code will output `13`, indicating that there are 13 characters in the given string (including spaces and punctuation).