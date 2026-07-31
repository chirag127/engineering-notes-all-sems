# String handling

- A string is a sequence of characters that can be manipulated by various methods and operators.
- Strings are commonly used to store and display text data, such as names, messages, URLs, etc.
- Strings can be created by enclosing characters in single quotes (' ') or double quotes (" ").
- Strings can be concatenated (joined) by using the + operator, e.g. "Hello" + "World" = "HelloWorld".
- Strings can be repeated by using the * operator, e.g. "Hi" * 3 = "HiHiHi".
- Strings can be accessed by indexing, which returns a single character at a given position, e.g. "Hello"[0] = "H".
- Strings can be sliced, which returns a substring of a given range, e.g. "Hello"[1:3] = "el".
- Strings can be compared by using the == operator, which returns True if the strings are equal, and False otherwise, e.g. "Hello" == "Hello" = True, "Hello" == "World" = False.
- Strings can be modified by using various methods, such as:
  - upper(), which returns a copy of the string in uppercase, e.g. "Hello".upper() = "HELLO".
  - lower(), which returns a copy of the string in lowercase, e.g. "Hello".lower() = "hello".
  - replace(old, new), which returns a copy of the string with all occurrences of old replaced by new, e.g. "Hello".replace("l", "x") = "Hexxo".
  - split(sep), which returns a list of substrings separated by sep, e.g. "Hello,World".split(",") = ["Hello", "World"].
  - join(iterable), which returns a string that is the concatenation of the elements in iterable, separated by the string itself, e.g. "-".join(["Hello", "World"]) = "Hello-World".
  - strip(chars), which returns a copy of the string with leading and trailing characters removed, e.g. " Hello ".strip() = "Hello", "Hello".strip("H") = "ello".
  - format(args), which returns a formatted version of the string, where placeholders are replaced by the arguments, e.g. "Hello, {name}".format(name="World") = "Hello, World".