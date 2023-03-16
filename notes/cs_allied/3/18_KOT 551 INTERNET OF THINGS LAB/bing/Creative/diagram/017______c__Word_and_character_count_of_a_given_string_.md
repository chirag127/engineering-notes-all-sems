#### c) Word and character count of a given string.

- A string is a sequence of characters enclosed in quotation marks, such as "Hello" or "This is a string".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "This is a word".
- A character is a single symbol, such as "H" or "." or " ".
- To count the number of words in a string, one can split the string by spaces or punctuation marks and count the length of the resulting list.
- To count the number of characters in a string, one can simply count the length of the string itself, including spaces and punctuation marks.
- For example, the string "This is a string." has 4 words and 16 characters.
- Here is a pseudocode algorithm to count the words and characters in a string:

```
# Input: a string s
# Output: the number of words and characters in s

# Initialize word_count and char_count to zero
word_count = 0
char_count = 0

# Loop through each character in s
for each c in s:
  # Increment char_count by one
  char_count = char_count + 1

  # If c is a space or a punctuation mark
  if c is " " or c is "." or c is "," or c is ";" or c is ":" or c is "?" or c is "!":
    # Increment word_count by one
    word_count = word_count + 1

# Return word_count and char_count
return word_count, char_count
```