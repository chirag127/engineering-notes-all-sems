## String Operations

- A string is a sequence of characters enclosed in quotation marks, such as "Hello" or "Python".
- Strings can be concatenated (joined) using the + operator, such as "Hello" + "World" = "HelloWorld".
- Strings can be repeated using the * operator, such as "Hello" * 3 = "HelloHelloHello".
- Strings can be accessed by indexing, which returns a single character, such as "Hello"[0] = "H".
- Strings can be sliced, which returns a substring, such as "Hello"[1:3] = "el".
- Strings can be compared using the == operator, which returns True if the strings are equal, and False otherwise, such as "Hello" == "Hello" = True, and "Hello" == "World" = False.
- Strings can be converted to other data types using built-in functions, such as int("123") = 123, and float("3.14") = 3.14.
- Strings have many methods that perform various operations on them, such as:
  - upper(), which returns a copy of the string in uppercase, such as "Hello".upper() = "HELLO".
  - lower(), which returns a copy of the string in lowercase, such as "Hello".lower() = "hello".
  - replace(old, new), which returns a copy of the string with all occurrences of old replaced by new, such as "Hello".replace("l", "x") = "Hexxo".
  - find(sub), which returns the index of the first occurrence of sub in the string, or -1 if not found, such as "Hello".find("l") = 2, and "Hello".find("z") = -1.
  - split(sep), which returns a list of substrings separated by sep, such as "Hello,World".split(",") = ["Hello", "World"].
  - join(iterable), which returns a string that is the concatenation of the elements in iterable, separated by the string itself, such as "-".join(["Hello", "World"]) = "Hello-World".
  - strip(chars), which returns a copy of the string with leading and trailing characters removed, such as "  Hello  ".strip() = "Hello", and "Hello".strip("H") = "ello".
  - format(*args, **kwargs), which returns a formatted version of the string, using placeholders and arguments, such as "Hello, {name}".format(name="World") = "Hello, World".