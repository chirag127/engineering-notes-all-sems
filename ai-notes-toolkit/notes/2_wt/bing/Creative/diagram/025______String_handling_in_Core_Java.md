#### String handling in Core Java

String handling is a way of handling and manipulating strings in Java with the help of lot concepts like concatenation, comparison, etc. A string is a sequence of characters that can be created by using the String class or by using string literals.

A string literal is a sequence of characters enclosed in double quotes, such as "Hello". A string literal is stored in a special memory area called the string constant pool. When a string literal is created, the JVM checks the string constant pool first. If the string already exists in the pool, a reference to the pooled instance is returned. If the string does not exist in the pool, a new string object is created and placed in the pool.

Using the new keyword, a string object can be created by passing a character array or another string as an argument to the String constructor, such as new String("Hello"). This creates a new string object in the heap memory, which is separate from the string constant pool.

The following diagram illustrates the difference between string literals and string objects created using the new keyword:

```
+-----------------+     +-----------------+
| String constant |     | Heap memory     |
| pool            |     |                 |
+-----------------+     +-----------------+
| "Hello"         |     | new String("Hi")|
|                 |     |                 |
| "World"         |     | new String("Bye")|
|                 |     |                 |
| "Hi"            |     |                 |
+-----------------+     +-----------------+
```

The String class provides a lot of methods to perform operations on strings, such as compare(), concat(), equals(), split(), length(), replace(), compareTo(), intern(), substring(), etc. The String class also implements the Serializable, Comparable, and CharSequence interfaces.

The String class is immutable, which means that once a string object is created, its value cannot be changed. Any modification to a string object will result in a new string object being created. This makes string objects thread-safe and efficient, but also consumes more memory and creates more garbage for the garbage collector.

To overcome the immutability of strings, Java provides two classes: StringBuffer and StringBuilder. Both classes allow creating and modifying strings without creating new objects. The main difference between them is that StringBuffer is synchronized (thread-safe) and StringBuilder is not (faster).

The following diagram shows the hierarchy of the String, StringBuffer, and StringBuilder classes:

```
+-----------------+
| java.lang.Object|
+-----------------+
        ^
        |
+-----------------+
| java.lang.CharSequence|
+-----------------+
        ^
        |
+-----------------+     +-----------------+     +-----------------+
| java.lang.String|     | java.lang.StringBuffer|     | java.lang.StringBuilder|
+-----------------+     +-----------------+     +-----------------+
```