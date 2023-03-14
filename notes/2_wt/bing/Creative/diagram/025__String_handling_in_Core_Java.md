String handling in Java is a way of handling and manipulating strings in Java with the help of lot concepts like concatenation, comparison, etc. A string is a sequence of characters that can be created by using the String class or by using string literals. The String class implements the Serializable, Comparable, and CharSequence interfaces and provides many methods to perform operations on strings. 

#### String handling in Core Java

The following diagram illustrates the basic architecture of a string handling in Core Java:

```
+-----------------+    +-----------------+    +-----------------+
| String literal  |    | String object   |    | String methods  |
| "Hello"         |    | new String("Hi")|    | length(),       |
| "World"         |    | new String(ch)  |    | concat(),       |
| "Java"          |    |                 |    | equals(),       |
|                 |    |                 |    | indexOf(),      |
|                 |    |                 |    | toUpperCase(),  |
|                 |    |                 |    | etc.            |
+-----------------+    +-----------------+    +-----------------+
         |                     |                      |
         |                     |                      |
         |                     |                      |
         |                     |                      |
         |                     |                      |
         |                     |                      |
         |                     |                      |
         +---------------------+----------------------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               v
                      +-----------------+
                      | String handling |
                      | in Core Java    |
                      +-----------------+
```