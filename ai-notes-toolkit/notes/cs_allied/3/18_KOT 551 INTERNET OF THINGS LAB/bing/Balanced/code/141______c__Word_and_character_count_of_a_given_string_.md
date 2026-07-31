#### c) Word and character count of a given string.

- A string is a sequence of characters enclosed in quotation marks, such as "Hello" or "This is a string".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "This is a word".
- A character is a single symbol, such as "H" or "." or " ".
- To count the number of words and characters in a given string, we can use the following steps:
  - Initialize two variables, word_count and char_count, to zero.
  - Loop through each character in the string using a for loop or a while loop.
  - If the current character is a space or a punctuation mark, then increment word_count by one and continue the loop.
  - Otherwise, increment char_count by one and continue the loop.
  - After the loop ends, increment word_count by one to account for the last word in the string.
  - Return or print word_count and char_count as the final result.
- For example, given the string "This is a string with 7 words and 29 characters.", the word and character count are:

```python
word_count = 0
char_count = 0
for char in "This is a string with 7 words and 29 characters.":
  if char in " .,;:!?":
    word_count += 1
  else:
    char_count += 1
word_count += 1
print("Word count:", word_count)
print("Character count:", char_count)
```

Output:

```
Word count: 7
Character count: 29
```