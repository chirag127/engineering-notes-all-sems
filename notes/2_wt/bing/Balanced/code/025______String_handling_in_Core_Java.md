#### String handling in Core Java

String handling in Core Java refers to the manipulation of strings, which are objects that represent sequences of characters. Strings are immutable in Java, meaning that they cannot be modified once created. However, there are various ways to create, compare, concatenate, search, replace, split, and format strings using the methods of the String class and other related classes such as StringBuilder, StringBuffer, and StringJoiner.

Here is an example of some common string operations in Core Java:

```java
// Creating strings using literals and constructors
String s1 = "Hello"; // string literal
String s2 = new String("World"); // string object

// Comparing strings using equals and compareTo methods
System.out.println(s1.equals(s2)); // false
System.out.println(s1.compareTo(s2)); // -15 (s1 is lexicographically smaller than s2)

// Concatenating strings using + operator and concat method
String s3 = s1 + " " + s2; // Hello World
String s4 = s1.concat(" ").concat(s2); // Hello World

// Searching strings using indexOf and lastIndexOf methods
System.out.println(s3.indexOf("o")); // 4 (first occurrence of o)
System.out.println(s3.lastIndexOf("o")); // 7 (last occurrence of o)

// Replacing strings using replace and replaceAll methods
String s5 = s3.replace('o', 'a'); // Hella Warld
String s6 = s3.replaceAll("\\s", "-"); // Hello-World

// Splitting strings using split method
String[] words = s3.split(" "); // ["Hello", "World"]

// Formatting strings using format method
String s7 = String.format("The length of %s is %d", s3, s3.length()); // The length of Hello World is 11
```