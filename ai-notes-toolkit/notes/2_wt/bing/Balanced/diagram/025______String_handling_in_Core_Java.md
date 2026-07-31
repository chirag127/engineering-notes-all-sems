#### String handling in Core Java

String handling is a way of handling and manipulating strings in Java with the help of lot concepts like concatenation, comparison, etc. A string is a sequence of characters that can be created by using the String class or by using string literals.

A string literal is a sequence of characters enclosed in double quotes, such as "Hello". String literals are stored in a special memory area called the string constant pool. When a string literal is created, the JVM checks the string constant pool first. If the string already exists in the pool, a reference to the pooled instance is returned. If the string does not exist in the pool, a new String object is created and placed in the pool.

A string object is an instance of the String class that is created by using the new keyword, such as new String("Hello"). String objects are stored in the heap memory area. When a string object is created, the JVM does not check the string constant pool. It always creates a new String object in the heap.

The following diagram illustrates the difference between string literals and string objects in Java:

```
+------------------+          +------------------+
| String Constant  |          | Heap Memory      |
| Pool             |          |                  |
+------------------+          +------------------+
| "Hello"          |<---------| new String("Hi") |
+------------------+          +------------------+
| "World"          |<---------| new String("Hi") |
+------------------+          +------------------+
| "Hi"             |          |                  |
+------------------+          +------------------+
```

String handling in Java provides a lot of methods to perform operations on strings, such as compare(), concat(), equals(), split(), length(), replace(), compareTo(), intern(), substring(), etc. Some of these methods are defined in the String class, while some are defined in the Object class or the CharSequence interface.

Some of the important concepts of string handling in Java are:

- String immutability: Strings are immutable in Java, which means that once a string is created, it cannot be modified. Any operation that changes the string will create a new string object and leave the original string unchanged.
- String comparison: Strings can be compared in Java using the equals() method or the == operator. The equals() method compares the content of two strings, while the == operator compares the reference of two strings. Therefore, the equals() method is preferred for string comparison.
- String concatenation: Strings can be concatenated in Java using the + operator or the concat() method. The + operator creates a new string object by appending the second string to the first string, while the concat() method appends the second string to the end of the first string and returns the result.
- String intern: The intern() method returns a canonical representation of a string object. It checks the string constant pool and returns a reference to the equal string from the pool. If the string does not exist in the pool, it adds the string to the pool and returns a reference to it.