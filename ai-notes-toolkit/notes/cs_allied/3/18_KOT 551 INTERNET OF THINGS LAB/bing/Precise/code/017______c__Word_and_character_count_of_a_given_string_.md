#### c) Word and character count of a given string.

- To count the number of words in a given string, one can split the string into a list of words using the `split()` method and then find the length of the list using the `len()` function.
- To count the number of characters in a given string, one can use the `len()` function on the string itself.
- For example, consider the string `"Hello, world!"`. The word count can be found by splitting the string into a list of words using the `split()` method: `["Hello,", "world!"]`. The length of this list is `2`, so the word count is `2`.
- The character count can be found by using the `len()` function on the string itself: `len("Hello, world!")` which returns `13`, so the character count is `13`.
- It is important to note that the `split()` method splits the string on whitespace by default, so punctuation marks and other non-alphabetic characters are included in the word count. If a different definition of a word is desired, a custom function can be used to split the string into words.