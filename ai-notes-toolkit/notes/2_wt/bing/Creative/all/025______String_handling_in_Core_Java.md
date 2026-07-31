#### String handling in Core Java

- String handling is the process of manipulating, storing, and retrieving strings in Java.
- A string is a sequence of characters enclosed in double quotes, such as "Hello".
- Strings are immutable in Java, which means they cannot be modified once created.
- Strings are stored in a special memory area called the string constant pool, which is a part of the heap memory.
- Strings can be created in two ways: by using string literals or by using string objects.
- String literals are assigned to a variable directly, such as `String s = "Hello";`. They are interned in the string constant pool, which means that if two string literals have the same value, they will refer to the same memory location.
- String objects are created by using the `new` keyword or by using constructors, such as `String s = new String("Hello");`. They are stored in the heap memory, and each string object has its own memory location.
- Strings can be compared using the `equals()` method or the `==` operator. The `equals()` method compares the values of two strings, while the `==` operator compares the references of two strings.
- Strings can be concatenated using the `+` operator or the `concat()` method. The `+` operator creates a new string object every time it is used, while the `concat()` method modifies the existing string object if possible.
- Strings can be converted to other data types using methods such as `parseInt()`, `parseFloat()`, `valueOf()`, etc.
- Strings can be converted to character arrays using the `toCharArray()` method, and character arrays can be converted to strings using the `String` constructor.
- Strings can be manipulated using various methods, such as `length()`, `charAt()`, `substring()`, `replace()`, `trim()`, `toLowerCase()`, `toUpperCase()`, `split()`, `join()`, etc.
- Strings can be formatted using the `format()` method or the `printf()` method, which allow specifying placeholders and arguments for different data types and formats.
- Strings can be searched using methods such as `indexOf()`, `lastIndexOf()`, `startsWith()`, `endsWith()`, `contains()`, `matches()`, etc.
- Strings can be compared using methods such as `compareTo()`, `compareToIgnoreCase()`, `equalsIgnoreCase()`, etc., which return an integer value indicating the lexicographical order of two strings.
- Strings can be sorted using the `Arrays.sort()` method or the `Collections.sort()` method, which accept a string array or a string list as an argument.
- Strings can be used in switch statements, which compare the string value with the case labels using the `equals()` method.