#### Arrays in Core Java
An array in Core Java is an object that can store a fixed-size sequential collection of homogeneous elements of the same type. An array is used to store a collection of data, but it also more useful to think of an array as a collection of variables of the same type. The elements of an array are indexed, which means we can access them with numbers (called indices). In Java, the numbering starts at 0.

A diagram of an array in Core Java can be drawn using ASCII characters as follows:

```
+---+---+---+---+---+---+---+---+---+---+
| 5 | 8 | 3 | 9 | 6 | 2 | 7 | 4 | 1 | 0 |
+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9
```

This diagram shows an array of 10 integers, with each element having a value and an index. For example, the element at index 0 has the value 5, and the element at index 9 has the value 0. We can access any element of the array by using its index in square brackets, such as array[0] or array[9]. We can also modify the value of any element by assigning a new value to it, such as array[0] = 10 or array[9] = -1.