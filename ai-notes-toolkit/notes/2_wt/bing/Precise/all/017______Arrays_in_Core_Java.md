#### Arrays in Core Java
An array is a data structure that stores a collection of elements of the same data type. Each element can be accessed by its index, which is an integer value starting from 0. Here are some key points to remember about arrays in Core Java:

1. Arrays can store primitive data types (such as int, char, and double) as well as objects.
2. The size of an array must be specified when it is created and cannot be changed later.
3. Array elements are stored in contiguous memory locations.
4. The default value of numeric array elements is 0, for boolean arrays it is false, and for object arrays it is null.
5. Arrays can be one-dimensional or multi-dimensional.
6. The length of an array can be obtained using the `length` property.

Here is an example of how to declare, initialize, and access an array in Core Java:

```java
int[] myArray = new int[5]; // declaration and initialization
myArray[0] = 1; // assigning value to the first element
myArray[1] = 2; // assigning value to the second element
int x = myArray[0]; // accessing the first element
```

A useful mnemonic to remember the steps for using an array in Core Java is **DIAL**: **D**eclare, **I**nitialize, **A**ssign, and **L**ength.

Advantages of using arrays:
- Arrays allow random access to elements, which means that any element can be accessed directly using its index.
- Arrays are efficient in terms of memory usage because they store elements in contiguous memory locations.

Disadvantages of using arrays:
- The size of an array is fixed and cannot be changed after it is created.
- Inserting and deleting elements in an array can be time-consuming because it may require shifting elements.

In summary, arrays are a fundamental data structure in Core Java that can be used to store collections of elements of the same data type. They have several advantages, such as random access to elements and efficient memory usage, but also have some limitations, such as fixed size and time-consuming insertions and deletions. A useful mnemonic to remember the steps for using an array is **DIAL**: **D**eclare, **I**nitialize, **A**ssign, and **L**ength.