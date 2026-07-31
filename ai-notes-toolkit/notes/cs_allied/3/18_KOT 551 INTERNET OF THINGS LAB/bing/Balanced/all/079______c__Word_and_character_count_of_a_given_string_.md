#### c) Word and character count of a given string.

- A string is a sequence of characters enclosed in quotation marks, such as "Hello" or "This is a string".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "This is a word".
- A character is a single symbol, such as "H" or "." or " ".
- To count the number of words and characters in a given string, we can use the following steps:
  - Initialize two variables, word_count and char_count, to zero.
  - Loop through each character in the string using a for loop or a while loop.
  - If the current character is a space or a punctuation mark, then increment word_count by one and char_count by one.
  - If the current character is not a space or a punctuation mark, then increment char_count by one.
  - After the loop ends, check if the last character in the string was a space or a punctuation mark. If not, then increment word_count by one.
  - Return word_count and char_count as the final result.
- For example, given the string "This is a string.", the word count is 4 and the character count is 16. The pseudocode for this algorithm is:

```
word_count = 0
char_count = 0
for each character in string:
  if character is a space or a punctuation mark:
    word_count = word_count + 1
    char_count = char_count + 1
  else:
    char_count = char_count + 1
if last character in string is not a space or a punctuation mark:
  word_count = word_count + 1
return word_count and char_count
```