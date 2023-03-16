# Word and character count of a given string

- A string is a sequence of characters, such as "Hello, world!" or "This is Sydney."
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "world" or "Sydney."
- A character is a single symbol, such as "H" or "!" or "." or "y".
- To count the number of words and characters in a given string, we can use the following steps:

  1. Initialize two variables, word_count and char_count, to zero.
  2. Loop through each character in the string, using a variable i to keep track of the index.
  3. If the character at index i is a space or a punctuation mark, and the previous character was not, then increment word_count by one. This means we have reached the end of a word.
  4. Increment char_count by one for every character, regardless of whether it is a space or a punctuation mark. This means we are counting all the symbols in the string.
  5. After the loop ends, check if the last character in the string was not a space or a punctuation mark. If so, increment word_count by one, since we have one more word at the end of the string that was not counted by the loop.
  6. Return word_count and char_count as the final results.

- For example, given the string "This is Sydney.", the word count is 3 and the character count is 13. The steps are as follows:

  1. word_count = 0, char_count = 0
  2. i = 0, the character is "T", not a space or a punctuation mark, so word_count stays at 0 and char_count becomes 1.
  3. i = 1, the character is "h", not a space or a punctuation mark, so word_count stays at 0 and char_count becomes 2.
  4. i = 2, the character is "i", not a space or a punctuation mark, so word_count stays at 0 and char_count becomes 3.
  5. i = 3, the character is "s", not a space or a punctuation mark, so word_count stays at 0 and char_count becomes 4.
  6. i = 4, the character is " ", a space, and the previous character was not, so word_count becomes 1 and char_count becomes 5.
  7. i = 5, the character is "i", not a space or a punctuation mark, so word_count stays at 1 and char_count becomes 6.
  8. i = 6, the character is "s", not a space or a punctuation mark, so word_count stays at 1 and char_count becomes 7.
  9. i = 7, the character is " ", a space, and the previous character was not, so word_count becomes 2 and char_count becomes 8.
  10. i = 8, the character is "S", not a space or a punctuation mark, so word_count stays at 2 and char_count becomes 9.
  11. i = 9, the character is "y", not a space or a punctuation mark, so word_count stays at 2 and char_count becomes 10.
  12. i = 10, the character is "d", not a space or a punctuation mark, so word_count stays at 2 and char_count becomes 11.
  13. i = 11, the character is "n", not a space or a punctuation mark, so word_count stays at 2 and char_count becomes 12.
  14. i = 12, the character is "e", not a space or a punctuation mark, so word_count stays at 2 and char_count becomes 13.
  15. i = 13, the character is ".", a punctuation mark, and the previous character was not, so word_count becomes 3 and char_count stays at 13.
  16. The loop ends, and the last character was a punctuation mark, so word_count stays at 3 and char_count stays at 13.
  17. Return word_count = 3 and char_count = 13.