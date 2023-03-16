# Word and character count of a given string

- A string is a sequence of characters, such as "Hello, world!" or "This is Sydney."
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "world" or "Sydney."
- A character is a single symbol, such as "H" or "!" or "." or "y."
- To count the number of words and characters in a given string, we can use the following steps:

  - Initialize two variables, word_count and char_count, to zero.
  - Loop through each character in the string, using a variable i to keep track of the index.
  - If the character at index i is a space or a punctuation mark, then we have reached the end of a word. Increment word_count by one.
  - If the character at index i is not a space or a punctuation mark, then it is part of a word. Increment char_count by one.
  - After the loop ends, we have the word count and the character count of the string.

- For example, let's count the words and characters in the string "Hello, world!"

  - word_count = 0, char_count = 0
  - i = 0, the character is "H", not a space or a punctuation mark, so char_count = 1
  - i = 1, the character is "e", not a space or a punctuation mark, so char_count = 2
  - i = 2, the character is "l", not a space or a punctuation mark, so char_count = 3
  - i = 3, the character is "l", not a space or a punctuation mark, so char_count = 4
  - i = 4, the character is "o", not a space or a punctuation mark, so char_count = 5
  - i = 5, the character is ",", a punctuation mark, so word_count = 1
  - i = 6, the character is " ", a space, so word_count = 1
  - i = 7, the character is "w", not a space or a punctuation mark, so char_count = 6
  - i = 8, the character is "o", not a space or a punctuation mark, so char_count = 7
  - i = 9, the character is "r", not a space or a punctuation mark, so char_count = 8
  - i = 10, the character is "l", not a space or a punctuation mark, so char_count = 9
  - i = 11, the character is "d", not a space or a punctuation mark, so char_count = 10
  - i = 12, the character is "!", a punctuation mark, so word_count = 2
  - The loop ends, so word_count = 2 and char_count = 10

- Therefore, the string "Hello, world!" has 2 words and 10 characters.