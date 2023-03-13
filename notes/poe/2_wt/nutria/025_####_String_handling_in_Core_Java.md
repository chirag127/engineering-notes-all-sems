
#### String handling in Core Java

* Strings are objects that represent a sequence of characters. 
* In Core Java, strings are represented using the `java.lang.String` class. 
* Strings can be created in two ways: 
  * Directly using a String literal: `String str = "Hello World!";`
  * Using the `String` class's constructor: `String str = new String("Hello World!");`
* Strings are immutable in Java, meaning that once created, they cannot be changed.
* To manipulate Strings, there are many methods available in the `String` class.
  * `length()`: returns the length of the String.
  * `charAt(int index)`: returns the character at the specified index.
  * `substring(int beginIndex, int endIndex)`: returns a new String that is a substring of the original String.
  * `concat(String str)`: concatenates the specified String to the end of the original String.
  * `replace(char oldChar, char newChar)`: replaces all occurrences of the specified character in the String with the new character.
  * `toLowerCase()`: returns a new String with all characters in lowercase.
  * `toUpperCase()`: returns a new String with all characters in uppercase.
  * `trim()`: returns a new String with all leading and trailing whitespace removed.
* Mnemonics and learning tricks: 
  * `String` is an object, not a primitive data type. Remember this by thinking of the `String` class as a type of container that holds a sequence of characters. 
  * Strings are immutable, meaning that once created, they cannot be changed. This is an important concept to remember when manipulating Strings. 
  * When using the `String` class's methods, remember to use the correct syntax. For example, for the `substring()` method, the syntax is `substring(int beginIndex, int endIndex)`.