#### String handling in Core Java

- String handling is a way of handling and manipulating strings in Java with the help of lot concepts like concatenation, comparison, etc.
- A string is a sequence of characters. In Java, a string is an object that is created by using the String class. 
- The String class provides a lot of methods to perform operations on strings such as compare(), concat(), equals(), split(), length(), replace(), compareTo(), intern(), substring(), etc.
- There are two ways to create a string in Java:
  - String literal: String s = "GeeksforGeeks";
  - Using new keyword: String s = new String("GeeksforGeeks");
- String literals are stored in a special memory area called the string constant pool. When a string is created using a literal, the JVM checks the string constant pool first. If the string already exists in the pool, a reference to the pooled instance is returned. If the string does not exist in the pool, a new String object is created and placed in the pool.
- When a string is created using the new keyword, the JVM creates a new String object in normal (non-pool) heap memory, and the literal "GeeksforGeeks" is placed in the string constant pool. The variable s refers to the object in heap (non-pool).
- Strings are immutable in Java, which means they cannot be changed once created. Any modification to a string will result in a new string object, leaving the original string unchanged.
- StringBuffer and StringBuilder are two classes that provide mutable strings, which means they can be modified without creating new objects. The difference between them is that StringBuffer is thread-safe and synchronized, while StringBuilder is not.