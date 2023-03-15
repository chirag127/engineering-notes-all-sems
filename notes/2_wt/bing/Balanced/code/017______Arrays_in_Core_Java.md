#### Arrays in Core Java

An array is a collection of elements of the same type that are stored in contiguous memory locations. Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.

To declare an array, you need to specify the type of elements and the number of elements in square brackets. For example, to declare an array of 10 integers, you can write:

```java
int[] numbers = new int[10];
```

You can also initialize an array with specific values by using curly braces. For example, to create an array of 5 strings, you can write:

```java
String[] names = {"Alice", "Bob", "Charlie", "David", "Eve"};
```

To access an element of an array, you need to use the index of the element in square brackets. The index starts from 0 and goes up to the length of the array minus one. For example, to print the first and the last element of the names array, you can write:

```java
System.out.println(names[0]); // prints Alice
System.out.println(names[4]); // prints Eve
```

To modify an element of an array, you need to assign a new value to the index of the element. For example, to change the second element of the numbers array to 42, you can write:

```java
numbers[1] = 42;
```

To get the length of an array, you can use the length property of the array. For example, to print the number of elements in the names array, you can write:

```java
System.out.println(names.length); // prints 5
```

To iterate over an array, you can use a for loop or a for-each loop. A for loop uses a counter variable to access each element by its index. A for-each loop uses a variable to store each element directly. For example, to print all the elements of the names array, you can write:

```java
// using a for loop
for (int i = 0; i < names.length; i++) {
  System.out.println(names[i]);
}

// using a for-each loop
for (String name : names) {
  System.out.println(name);
}
```

Arrays are useful for storing and manipulating data, but they have some limitations. For example, arrays have a fixed size that cannot be changed once they are created. Arrays also cannot store elements of different types. To overcome these limitations, you can use other data structures such as lists, sets, and maps, which are provided by the Java Collections Framework.