#### c) Word and character count of a given string.

- To count the number of words in a given string, one can split the string into a list of words using the `split()` method and then find the length of the list using the `len()` function.
- To count the number of characters in a given string, one can use the `len()` function directly on the string.
- It is important to note that the `len()` function counts the number of characters in the string, including spaces and punctuation.
- Here is an example in Python:

```python
string = "This is an example string."
word_count = len(string.split())
character_count = len(string)
print(f"Word count: {word_count}")
print(f"Character count: {character_count}")
```

- In the above example, the `split()` method is used to split the string into a list of words, and the `len()` function is used to find the length of the list and the length of the string.
- The output of the above code would be:

```
Word count: 5
Character count: 25
```

- As shown in the output, the word count is 5 and the character count is 25, including spaces and punctuation.