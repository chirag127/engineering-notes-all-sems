#### c) Word and character count of a given string

To count the number of words and characters in a given string, the following steps can be taken:

1. Initialize two variables, one to store the word count and the other to store the character count.
2. Iterate through each character in the string.
3. For each character, increment the character count variable.
4. If the current character is a space or the end of the string is reached, increment the word count variable.
5. Continue iterating until the end of the string is reached.
6. The final values of the word count and character count variables will represent the number of words and characters in the given string, respectively.

Example:

```python
def word_and_character_count(string):
    word_count = 0
    character_count = 0
    for i in range(len(string)):
        character_count += 1
        if string[i] == ' ' or i == len(string)-1:
            word_count += 1
    return word_count, character_count

string = "Hello, world!"
word_count, character_count = word_and_character_count(string)
print(f"Word count: {word_count}")
print(f"Character count: {character_count}")
```

Output:

```
Word count: 2
Character count: 13
```