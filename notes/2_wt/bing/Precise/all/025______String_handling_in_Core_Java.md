#### String handling in Core Java
String handling in Core Java refers to the various ways in which strings can be manipulated and used in Java programs. Some of the key features of string handling in Core Java include:

1. **String creation**: Strings can be created in Java using the `new` keyword or by assigning a string literal to a variable. For example:
```java
String str1 = new String("Hello");
String str2 = "World";
```

2. **String concatenation**: Strings can be concatenated in Java using the `+` operator or the `concat()` method. For example:
```java
String str1 = "Hello";
String str2 = "World";
String str3 = str1 + str2;
String str4 = str1.concat(str2);
```

3. **String comparison**: Strings can be compared in Java using the `equals()` method or the `compareTo()` method. The `equals()` method returns `true` if two strings are equal, while the `compareTo()` method returns an integer value indicating the lexicographic difference between two strings. For example:
```java
String str1 = "Hello";
String str2 = "World";
boolean result1 = str1.equals(str2);
int result2 = str1.compareTo(str2);
```

4. **String manipulation**: Strings can be manipulated in various ways in Java, such as by converting them to upper or lower case, trimming white spaces, replacing characters or substrings, and splitting them into an array of substrings. For example:
```java
String str = "Hello World";
String upper = str.toUpperCase();
String lower = str.toLowerCase();
String trimmed = str.trim();
String replaced = str.replace('l', 'x');
String[] split = str.split(" ");
```

5. **String immutability**: Strings in Java are immutable, meaning that their value cannot be changed once they are created. Any operation that appears to modify a string actually creates a new string object. For example:
```java
String str = "Hello";
str = str.concat(" World");
```
In the above example, the `concat()` method creates a new string object with the value `"Hello World"` and assigns it to the `str` variable.

A mnemonic to remember the methods of the `String` class in Java is **SCCRRT**: **S**tring creation, **C**oncatenation, **C**omparison, **R**eplacement, **R**egex, **T**rimming.

These are some of the key features of string handling in Core Java. Understanding these concepts is essential for working with strings in Java programs.