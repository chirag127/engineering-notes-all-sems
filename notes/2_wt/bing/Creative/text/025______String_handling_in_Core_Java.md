#### String handling in Core Java

- String handling is a way of handling and manipulating strings in Java with the help of lot concepts like concatenation, comparison, etc. 
- A string is a sequence of characters. In Java, a string is an object that is created by using the String class.  
- The String class provides a lot of methods to perform operations on strings such as `compare()`, `concat()`, `equals()`, `split()`, `length()`, `replace()`, `compareTo()`, `intern()`, `substring()` etc. 
- The String class implements `Serializable`, `Comparable` and `CharSequence` interfaces. 
- There are two ways to create a string in Java: 
  - String literal: `String s = "GeeksforGeeks";`
  - Using new keyword: `String s = new String("GeeksforGeeks");` 
- String literals are stored in a special memory area called the string constant pool. 
- Strings are immutable in Java, which means they cannot be changed once created. 
- To create mutable strings, we can use classes like `StringBuffer` or `StringBuilder`. 
- `StringBuffer` is a peer class of String that provides much of the functionality of strings. It is synchronized and thread-safe. 
- `StringBuilder` is similar to `StringBuffer`, but it is not synchronized and not thread-safe. It is faster than `StringBuffer`.