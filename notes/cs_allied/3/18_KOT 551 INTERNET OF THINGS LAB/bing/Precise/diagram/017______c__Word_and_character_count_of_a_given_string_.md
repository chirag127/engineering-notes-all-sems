#### c) Word and character count of a given string.

To count the number of words and characters in a given string, follow these steps:

1. Initialize two variables, one to store the word count and the other to store the character count.
2. Iterate through each character in the string.
3. If the current character is a space or a newline character, increment the word count.
4. Increment the character count for each character in the string.
5. The final values of the word count and character count variables will give the desired result.

Here is an example code snippet in Python that implements the above logic:

```python
def count_words_characters(string):
    word_count = 0
    character_count = 0
    for char in string:
        if char == ' ' or char == '\n':
            word_count += 1
        character_count += 1
    return word_count + 1, character_count

string = "This is an example string."
word_count, character_count = count_words_characters(string)
print(f"Word count: {word_count}")
print(f"Character count: {character_count}")
```

This code will output the following:

```
Word count: 5
Character count: 25
```

Note that the word count is incremented by 1 at the end to account for the last word in the string. Also, the character count includes spaces and newline characters. If you want to exclude them from the count, you can add a condition to check for them before incrementing the character count.