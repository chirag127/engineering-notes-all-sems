# Word and character count of a given string

- A string is a sequence of characters, such as "Hello, world!" or "This is a sentence.".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "world" or "sentence".
- A character is a single symbol, such as "H" or "!" or ".".
- To count the number of words and characters in a given string, we can use the following steps:

  1. Initialize two variables, word_count and char_count, to zero.
  2. Loop through each character in the string, using a variable i to keep track of the index.
  3. If the character at index i is a space or a punctuation mark, and the previous character was not, then increment word_count by one. This means we have reached the end of a word.
  4. Increment char_count by one for every character, regardless of whether it is a space or a punctuation mark. This means we have counted one more character.
  5. After the loop ends, check if the last character was not a space or a punctuation mark. If so, increment word_count by one more. This means we have counted the last word in the string.
  6. Return word_count and char_count as the final results.

- Here is an example of how this algorithm works on the string "Hello, world!":

  1. word_count = 0, char_count = 0
  2. i = 0, character = "H", not a space or a punctuation mark, char_count = 1
  3. i = 1, character = "e", not a space or a punctuation mark, char_count = 2
  4. i = 2, character = "l", not a space or a punctuation mark, char_count = 3
  5. i = 3, character = "l", not a space or a punctuation mark, char_count = 4
  6. i = 4, character = "o", not a space or a punctuation mark, char_count = 5
  7. i = 5, character = ",", a punctuation mark, and the previous character was not, word_count = 1, char_count = 6
  8. i = 6, character = " ", a space, and the previous character was a punctuation mark, char_count = 7
  9. i = 7, character = "w", not a space or a punctuation mark, char_count = 8
  10. i = 8, character = "o", not a space or a punctuation mark, char_count = 9
  11. i = 9, character = "r", not a space or a punctuation mark, char_count = 10
  12. i = 10, character = "l", not a space or a punctuation mark, char_count = 11
  13. i = 11, character = "d", not a space or a punctuation mark, char_count = 12
  14. i = 12, character = "!", a punctuation mark, and the previous character was not, word_count = 2, char_count = 13
  15. The loop ends, and the last character was a punctuation mark, so we do not increment word_count.
  16. Return word_count = 2 and char_count = 13 as the final results.