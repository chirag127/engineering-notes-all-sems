# c) Word and Character Count of a Given String

When working with strings, it is often necessary to know the number of words and characters in the string. This information can be useful for a variety of purposes, from analyzing text to setting character limits for input fields. In this section, we will discuss how to count the number of words and characters in a given string.

## Counting Words in a String

To count the number of words in a string, we can use the `split()` method. This method splits the string into a list of words based on a specified delimiter, which is usually a space character. We can then use the `len()` function to count the number of words in the list.

Here's an example:

```python
string = "This is a sample string."
word_count = len(string.split())
print("Word count:", word_count)
```

Output:
```
Word count: 5
```

In the above example, we first define a string and assign it to the variable `string`. We then use the `split()` method to split the string into a list of words and assign the result to the variable `word_count`. Finally, we print the word count using the `print()` function.

## Counting Characters in a String

To count the number of characters in a string, we can use the `len()` function directly on the string. This function returns the number of characters in the string, including spaces and punctuation marks.

Here's an example:

```python
string = "This is a sample string."
char_count = len(string)
print("Character count:", char_count)
```

Output:
```
Character count: 23
```

In the above example, we define a string and assign it to the variable `string`. We then use the `len()` function to count the number of characters in the string and assign the result to the variable `char_count`. Finally, we print the character count using the `print()` function.

## Handling Special Cases

When counting words and characters in a string, it is important to consider special cases like empty strings and strings with extra spaces. Here are some tips to handle these cases:

- If the string is empty, the word and character counts should be 0.
- If the string has extra spaces, we can use the `strip()` method to remove them before counting the words and characters.

Here's an example:

```python
string = "   This is a sample    string.   "
string = string.strip()
if string:
    word_count = len(string.split())
    char_count = len(string)
    print("Word count:", word_count)
    print("Character count:", char_count)
else:
    print("The string is empty.")
```

Output:
```
Word count: 5
Character count: 23
```

In the above example, we first define a string with extra spaces and assign it to the variable `string`. We then use the `strip()` method to remove the extra spaces and assign the result back to `string`. We then check if `string` is not empty using a conditional statement. If it is not empty, we count the words and characters in the string and print the results. If it is empty, we print a message indicating that the string is empty.

## Conclusion

Counting the number of words and characters in a string is a common task in Python programming. By using the `split()` method and the `len()` function, we can easily count the number of words and characters in a given string. We should also consider special cases like empty strings and strings with extra spaces to ensure accurate counts.