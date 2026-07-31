# Word and character count of a given string

- A string is a sequence of characters, such as "Hello, world!" or "This is a sentence.".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "world" or "sentence".
- A character is a single symbol, such as "H" or "!" or ".".
- To count the number of words and characters in a given string, we can use the following steps:

  - Initialize two variables, word_count and char_count, to zero.
  - Loop through each character in the string, and do the following:
    - Increment char_count by one, since each character adds to the character count.
    - If the character is a space or a punctuation mark, then increment word_count by one, since each space or punctuation mark indicates the end of a word.
    - If the character is the last one in the string, then increment word_count by one, since the last word does not have a space or a punctuation mark after it.
  - Return word_count and char_count as the final results.

- For example, given the string "Hello, world!", the word count is 2 and the character count is 13. The steps are as follows:

  - word_count = 0, char_count = 0
  - Loop through each character in "Hello, world!":
    - "H": char_count = 1, word_count = 0
    - "e": char_count = 2, word_count = 0
    - "l": char_count = 3, word_count = 0
    - "l": char_count = 4, word_count = 0
    - "o": char_count = 5, word_count = 0
    - ",": char_count = 6, word_count = 1 (end of a word)
    - " ": char_count = 7, word_count = 1
    - "w": char_count = 8, word_count = 1
    - "o": char_count = 9, word_count = 1
    - "r": char_count = 10, word_count = 1
    - "l": char_count = 11, word_count = 1
    - "d": char_count = 12, word_count = 1
    - "!": char_count = 13, word_count = 2 (end of a word and the last character)
  - Return word_count = 2 and char_count = 13