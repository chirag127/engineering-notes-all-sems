# Word and character count of a given string

- A string is a sequence of characters, such as "Hello, world!" or "This is Sydney."
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "world" or "Sydney."
- A character is a single symbol, such as "H" or "!" or "." or "y."
- To count the number of words and characters in a given string, we can use the following steps:

  1. Initialize two variables, word_count and char_count, to zero.
  2. Loop through each character in the string, using a variable i to keep track of the index.
  3. If the character at index i is a space or a punctuation mark, and the previous character was not, then increment word_count by one. This means we have found the end of a word.
  4. Increment char_count by one for every character, regardless of whether it is a space or a punctuation mark. This means we have counted one more character.
  5. After the loop ends, check if the last character in the string was not a space or a punctuation mark. If so, increment word_count by one more. This means we have found the last word in the string.
  6. Return word_count and char_count as the final results.

- For example, given the string "This is Sydney.", the algorithm would work as follows:

  1. word_count = 0, char_count = 0
  2. i = 0, character = "T", not a space or a punctuation mark, char_count = 1
  3. i = 1, character = "h", not a space or a punctuation mark, char_count = 2
  4. i = 2, character = "i", not a space or a punctuation mark, char_count = 3
  5. i = 3, character = "s", not a space or a punctuation mark, char_count = 4
  6. i = 4, character = " ", a space, and the previous character was not, word_count = 1, char_count = 5
  7. i = 5, character = "i", not a space or a punctuation mark, char_count = 6
  8. i = 6, character = "s", not a space or a punctuation mark, char_count = 7
  9. i = 7, character = " ", a space, and the previous character was not, word_count = 2, char_count = 8
  10. i = 8, character = "S", not a space or a punctuation mark, char_count = 9
  11. i = 9, character = "y", not a space or a punctuation mark, char_count = 10
  12. i = 10, character = "d", not a space or a punctuation mark, char_count = 11
  13. i = 11, character = "n", not a space or a punctuation mark, char_count = 12
  14. i = 12, character = "e", not a space or a punctuation mark, char_count = 13
  15. i = 13, character = "y", not a space or a punctuation mark, char_count = 14
  16. i = 14, character = ".", a punctuation mark, and the previous character was not, word_count = 3, char_count = 15
  17. The loop ends, and the last character was a punctuation mark, so we do not increment word_count.
  18. Return word_count = 3 and char_count = 15.