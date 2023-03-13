#### String handling in Core Java

String handling is an important concept in Java programming language as it is used to manipulate and store textual data in a program. A string is a sequence of characters and is represented by the Java String class. In this section, we will cover the basics of string handling in Core Java.

##### Creating Strings

In Java, strings can be created in three ways:

1. Using String literal: String literals are enclosed in double quotes and stored in the String constant pool. For example, `String str = "Hello World";`

2. Using the new keyword: Strings can also be created using the `new` keyword. For example, `String str = new String("Hello World");`

3. Using character array: Strings can be created using an array of characters. For example, `char[] charArray = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'}; String str = new String(charArray);`

##### String Operations

Java provides various methods to perform operations on a string. Some of the commonly used methods are:

1. `length()`: This method returns the length of the string.

2. `charAt(index)`: This method returns the character at the specified index.

3. `substring(beginIndex, endIndex)`: This method returns the substring of the specified string from the beginIndex to the endIndex.

4. `concat(String str)`: This method concatenates the specified string to the end of the current string.

5. `equals(Object obj)`: This method compares the current string with the specified object and returns `true` if they are equal.

6. `equalsIgnoreCase(String str)`: This method compares the current string with the specified string ignoring case.

7. `indexOf(int ch)`: This method returns the index of the first occurrence of the specified character in the string.

8. `lastIndexOf(int ch)`: This method returns the index of the last occurrence of the specified character in the string.

##### Mnemonics and Learning Tricks

Some of the mnemonics and learning tricks that can be used to remember the string handling methods are:

1. Remember the mnemonic "LASCIEI" to remember the commonly used string methods: length, charAt, substring, concat, equals, equalsIgnoreCase, and indexOf.

2. Remember the phrase "Last Index, First Occurrence" to remember the `lastIndexOf` method.

##### Advantages of String Handling in Core Java

1. Strings are immutable in Java, which means that once a string object is created, it cannot be modified. This makes it easy to work with strings in a multi-threaded environment.

2. String handling methods are built-in and easy to use, which reduces the amount of code required to perform common string operations.

##### Disadvantages of String Handling in Core Java

1. Creating a new string object for every modification can be memory-intensive and can impact the performance of a program.

2. String concatenation using the `+` operator can be slow, especially when dealing with large strings.

##### Applications of String Handling in Core Java

String handling is used in various applications such as:

1. Text processing, such as searching, replacing, and formatting text.

2. Parsing data from files or input streams.

3. Storing and manipulating user input.

##### Example

Here is an example of a Java program that demonstrates string handling:

```
public class StringHandlingExample {
   public static void main(String[] args) {
      String str1 = "Hello World";
      String str2 = "world";
      
      System.out.println("Length of str1: " + str1.length());
      System.out.println("Character at index 4 in str1: " + str1.charAt(4));
      System.out.println("Substring of str1 from index 6 to 11: " + str1.substring(6, 11));
      System.out.println("Concatenation of str1 and str2: " + str1.concat(str2));
      System.out.println("Is str1 equal to str2: " + str1.equals(str2));
      System.out.println("Is str1 equal to str2 (ignoring case): " + str1.equalsIgnoreCase(str2));
      System.out.println("Index of 'o' in str1: " + str1.indexOf('o'));
      System.out.println("Last index of 'o' in str1: " + str1.lastIndexOf('o'));
   }
}
```

Output:
```
Length of str1: 11
Character at index 4 in str1: o
Substring of str1 from index 6 to 11: World
Concatenation of str1 and str2: HelloWorldworld
Is str1 equal to str2: false
Is str1 equal to str2 (ignoring case): false
Index of 'o' in str1: 4
Last index of 'o' in str1: 7
```

