#### c) Word and character count of a given string.

- A string is a sequence of characters enclosed in quotation marks, such as "Hello" or "This is a string".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "This is a word".
- A character is a single symbol, such as "H" or "." or " ".
- To count the number of words in a string, we can split the string by spaces or punctuation marks and count the length of the resulting list.
- To count the number of characters in a string, we can simply count the length of the string itself.
- For example, the string "This is a string with 7 words and 29 characters." has 7 words and 29 characters.
- Here is a possible algorithm to count the words and characters in a string:

```
# Input: a string s
# Output: the number of words and characters in s

# Initialize word_count and char_count to zero
word_count = 0
char_count = 0

# Loop through each character in s
for c in s:
  # Increment char_count by one
  char_count = char_count + 1
  # If c is a space or a punctuation mark, increment word_count by one
  if c == " " or c in [".", ",", "!", "?", ";", ":"]:
    word_count = word_count + 1

# If s is not empty and does not end with a space or a punctuation mark, increment word_count by one
if s != "" and s[-1] not in [" ", ".", ",", "!", "?", ";", ":"]:
  word_count = word_count + 1

# Return word_count and char_count
return word_count, char_count
```