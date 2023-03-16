#### c) Word and character count of a given string.

- A string is a sequence of characters enclosed in quotation marks, such as "Hello" or "This is a string".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "This is a word".
- A character is a single symbol, such as "H" or "." or " ".
- To count the number of words and characters in a given string, we can use the following steps:
  - Initialize two variables, word_count and char_count, to zero.
  - Loop through each character in the string using a for loop or a while loop.
  - If the current character is a space or a punctuation mark, then increment word_count by one and continue to the next character.
  - Otherwise, increment char_count by one and continue to the next character.
  - After the loop ends, increment word_count by one to account for the last word in the string.
  - Return or print word_count and char_count as the final result.