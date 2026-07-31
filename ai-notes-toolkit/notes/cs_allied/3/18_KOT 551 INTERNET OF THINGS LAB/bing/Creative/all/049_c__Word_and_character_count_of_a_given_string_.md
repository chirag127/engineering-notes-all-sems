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

- For example, given the string "Hello, world!", the word count is 2 and the character count is 13. The pseudocode for this algorithm is:

  - word_count = 0
  - char_count = 0
  - for each character in "Hello, world!":
    - char_count = char_count + 1
    - if character is a space or a punctuation mark:
      - word_count = word_count + 1
    - if character is the last one in the string:
      - word_count = word_count + 1
  - return word_count and char_count

- This algorithm can be implemented in different programming languages, such as Python, Java, C++, etc. Here is an example of Python code that performs this task:

  ```python
  def count_words_and_chars(string):
    word_count = 0
    char_count = 0
    for character in string:
      char_count += 1
      if character in " ,.!?;:":
        word_count += 1
      if character == string[-1]:
        word_count += 1
    return word_count, char_count

  string = "Hello, world!"
  word_count, char_count = count_words_and_chars(string)
  print(f"The word count is {word_count} and the character count is {char_count}.")
  ```