#### c) Word and character count of a given string.

- To count the number of words in a given string, we can split the string into a list of words using the `split()` method and then find the length of the list using the `len()` function.
- To count the number of characters in a given string, we can use the `len()` function directly on the string.
- For example, consider the string `"Hello, World!"`. The word count of this string is `2` and the character count is `13`.
- It is important to note that the character count includes spaces and punctuation marks.
- In some cases, it may be necessary to remove certain characters or substrings from the string before counting the words or characters. This can be done using the `replace()` method or by using regular expressions.