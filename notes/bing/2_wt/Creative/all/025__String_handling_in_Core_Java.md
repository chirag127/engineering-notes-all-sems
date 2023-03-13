#### String handling in Core Java

- A string is a sequence of characters that can be manipulated, compared, searched, or formatted.
- In Java, strings are objects of the `String` class, which is defined in the `java.lang` package.
- The `String` class provides various methods and constructors to create and manipulate strings.
- Some of the common methods of the `String` class are:

  - `length()`: returns the number of characters in the string.
  - `charAt(int index)`: returns the character at the specified index in the string.
  - `substring(int beginIndex, int endIndex)`: returns a new string that is a part of the original string from the specified begin index (inclusive) to the end index (exclusive).
  - `concat(String str)`: returns a new string that is the concatenation of the original string and the specified string.
  - `equals(Object obj)`: returns true if the original string and the specified object are equal, false otherwise.
  - `equalsIgnoreCase(String anotherString)`: returns true if the original string and the specified string are equal, ignoring case differences, false otherwise.
  - `compareTo(String anotherString)`: returns a negative integer, zero, or a positive integer as the original string is lexicographically less than, equal to, or greater than the specified string.
  - `indexOf(int ch)`: returns the index of the first occurrence of the specified character in the string, or -1 if not found.
  - `indexOf(int ch, int fromIndex)`: returns the index of the first occurrence of the specified character in the string, starting from the specified index, or -1 if not found.
  - `indexOf(String str)`: returns the index of the first occurrence of the specified substring in the string, or -1 if not found.
  - `indexOf(String str, int fromIndex)`: returns the index of the first occurrence of the specified substring in the string, starting from the specified index, or -1 if not found.
  - `lastIndexOf(int ch)`: returns the index of the last occurrence of the specified character in the string, or -1 if not found.
  - `lastIndexOf(int ch, int fromIndex)`: returns the index of the last occurrence of the specified character in the string, starting backward from the specified index, or -1 if not found.
  - `lastIndexOf(String str)`: returns the index of the last occurrence of the specified substring in the string, or -1 if not found.
  - `lastIndexOf(String str, int fromIndex)`: returns the index of the last occurrence of the specified substring in the string, starting backward from the specified index, or -1 if not found.
  - `replace(char oldChar, char newChar)`: returns a new string that is the result of replacing all occurrences of the old character with the new character in the original string.
  - `replace(CharSequence target, CharSequence replacement)`: returns a new string that is the result of replacing all occurrences of the target sequence with the replacement sequence in the original string.
  - `toLowerCase()`: returns a new string that is the lowercase version of the original string.
  - `toUpperCase()`: returns a new string that is the uppercase version of the original string.
  - `trim()`: returns a new string that is the result of removing any leading and trailing whitespace characters from the original string.
  - `valueOf(Object obj)`: returns the string representation of the specified object.

- Some of the common constructors of the `String` class are:

  - `String()`: creates an empty string.
  - `String(byte[] bytes)`: creates a string from the specified array of bytes, using the default charset.
  - `String(byte[] bytes, int offset, int length)`: creates a string from the specified subarray of bytes, using the default charset.
  - `String(byte[] bytes, String charsetName)`: creates a string from the specified array of bytes, using the specified charset.
  - `String(byte[] bytes, int offset, int length, String charsetName)`: creates a string from the specified subarray of bytes, using the specified charset.
  - `String(char[] value)`: creates a string from the specified array of characters.
  - `String(char[] value, int offset, int count)`: creates a string from the specified subarray of characters.
  - `String(String original)`: creates a string that is a copy of the original string.
  - `String(StringBuffer buffer)`: creates a string that represents the contents of the specified string buffer.
  - `String(StringBuilder builder)`: creates a string that represents the contents of the specified string builder.

- Strings are immutable in