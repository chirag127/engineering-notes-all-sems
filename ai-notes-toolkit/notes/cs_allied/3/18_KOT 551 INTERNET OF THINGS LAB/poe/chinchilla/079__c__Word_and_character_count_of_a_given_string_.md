#### c) Word and Character Count of a Given String

When working with text data, it is often necessary to determine the number of words and characters in a given string. This can be useful for a variety of tasks, such as analyzing text for sentiment or performing statistical analysis on text data. In this section, we will discuss how to count the number of words and characters in a given string.

##### Word Count

To count the number of words in a given string, we can use the following steps:

1. Split the string into a list of words using the `split()` method. This method splits the string at whitespace characters and returns a list of the resulting words.
2. Count the number of words in the list using the `len()` function.

Here is an example code snippet that demonstrates how to count the number of words in a string:

```python
s = "This is a sample string."
words = s.split()
word_count = len(words)
print("Number of words:", word_count)
```

This code will output:

```
Number of words: 5
```

##### Character Count

To count the number of characters in a given string, we can use the following steps:

1. Use the `len()` function to count the number of characters in the string.

Here is an example code snippet that demonstrates how to count the number of characters in a string:

```python
s = "This is a sample string."
char_count = len(s)
print("Number of characters:", char_count)
```

This code will output:

```
Number of characters: 23
```

It is important to note that the `len()` function counts all characters in the string, including spaces and punctuation marks. If you want to exclude certain characters from the count, you will need to modify the code accordingly.

In conclusion, counting the number of words and characters in a given string is a basic but important task when working with text data. By following the steps outlined above, you can easily determine the word and character count of any string in Python.