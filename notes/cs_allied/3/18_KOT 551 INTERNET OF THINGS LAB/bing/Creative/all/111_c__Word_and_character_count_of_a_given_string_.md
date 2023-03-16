# Word and character count of a given string

- A string is a sequence of characters, such as "Hello, world!" or "This is a sentence.".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "world" or "sentence".
- A character is a single symbol, such as "H" or "!" or ".".
- To count the number of words and characters in a given string, we can use the following steps:

  - Initialize two variables, word_count and char_count, to zero.
  - Loop through each character in the string, using a variable i to keep track of the index.
  - If the character at index i is a space or a punctuation mark, and the previous character was not, then increment word_count by one. This means we have reached the end of a word.
  - Increment char_count by one for every character, regardless of whether it is a space or a punctuation mark. This means we are counting all the symbols in the string.
  - After the loop, if the last character was not a space or a punctuation mark, then increment word_count by one. This means we have one more word at the end of the string that was not counted by the loop.
  - Return word_count and char_count as the final results.

- For example, given the string "Hello, world! This is a sentence.", we can apply the steps as follows:

  - word_count = 0, char_count = 0
  - i = 0, character = "H", not a space or a punctuation mark, char_count = 1
  - i = 1, character = "e", not a space or a punctuation mark, char_count = 2
  - i = 2, character = "l", not a space or a punctuation mark, char_count = 3
  - i = 3, character = "l", not a space or a punctuation mark, char_count = 4
  - i = 4, character = "o", not a space or a punctuation mark, char_count = 5
  - i = 5, character = ",", a punctuation mark, and the previous character was not, word_count = 1, char_count = 6
  - i = 6, character = " ", a space, and the previous character was a punctuation mark, char_count = 7
  - i = 7, character = "w", not a space or a punctuation mark, char_count = 8
  - i = 8, character = "o", not a space or a punctuation mark, char_count = 9
  - i = 9, character = "r", not a space or a punctuation mark, char_count = 10
  - i = 10, character = "l", not a space or a punctuation mark, char_count = 11
  - i = 11, character = "d", not a space or a punctuation mark, char_count = 12
  - i = 12, character = "!", a punctuation mark, and the previous character was not, word_count = 2, char_count = 13
  - i = 13, character = " ", a space, and the previous character was a punctuation mark, char_count = 14
  - i = 14, character = "T", not a space or a punctuation mark, char_count = 15
  - i = 15, character = "h", not a space or a punctuation mark, char_count = 16
  - i = 16, character = "i", not a space or a punctuation mark, char_count = 17
  - i = 17, character = "s", not a space or a punctuation mark, char_count = 18
  - i = 18, character = " ", a space, and the previous character was not, word_count = 3, char_count = 19
  - i = 19, character = "i", not a space or a punctuation mark, char_count = 20
  - i = 20, character = "s", not a space or a punctuation mark, char_count = 21
  - i = 21, character = " ", a space, and the previous character was not, word_count = 4, char_count = 22
  - i = 22, character = "a", not a space or a punctuation mark, char_count = 23
  - i = 23, character = " ", a space, and the previous character was not, word_count = 5, char_count