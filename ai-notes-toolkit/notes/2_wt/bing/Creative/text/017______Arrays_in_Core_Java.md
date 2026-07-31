#### Arrays in Core Java

- An array is a collection of elements of the same data type that are stored in contiguous memory locations.
- An array can be declared by specifying the data type followed by square brackets and the array name, for example: `int[] numbers;`
- An array can be initialized by assigning a list of values enclosed in curly braces, for example: `int[] numbers = {1, 2, 3, 4, 5};`
- An array can also be initialized by specifying the size of the array and allocating memory for it, for example: `int[] numbers = new int[5];`
- The size of an array can be obtained by using the `length` property of the array, for example: `int size = numbers.length;`
- The elements of an array can be accessed by using the array name and the index of the element, for example: `int first = numbers[0];`
- The index of an array starts from 0 and goes up to the size of the array minus one, for example: `numbers[0]` is the first element and `numbers[4]` is the last element in the array above.
- An array can be iterated over by using a for loop or an enhanced for loop, for example:

```java
// using a for loop
for (int i = 0; i < numbers.length; i++) {
  System.out.println(numbers[i]);
}

// using an enhanced for loop
for (int number : numbers) {
  System.out.println(number);
}
```

- An array can be passed as a parameter to a method by using the array name, for example: `public static void printArray(int[] array) { ... }`
- An array can be returned from a method by using the array name, for example: `public static int[] reverseArray(int[] array) { ... }`
- An array can be multidimensional, meaning that it can have more than one dimension, for example: `int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};`
- A multidimensional array can be declared, initialized, accessed, iterated over, passed and returned in a similar way as a one-dimensional array, but with an additional index for each dimension, for example: `int element = matrix[1][2];`
- A multidimensional array can have different lengths for each dimension, for example: `int[][] jagged = {{1, 2}, {3, 4, 5}, {6}};`
- An array can be sorted by using the `Arrays.sort()` method from the `java.util` package, for example: `Arrays.sort(numbers);`
- An array can be searched by using the `Arrays.binarySearch()` method from the `java.util` package, for example: `int index = Arrays.binarySearch(numbers, 4);`
- An array can be copied by using the `Arrays.copyOf()` or `Arrays.copyOfRange()` methods from the `java.util` package, for example: `int[] copy = Arrays.copyOf(numbers, 3);`
- An array can be compared by using the `Arrays.equals()` or `Arrays.deepEquals()` methods from the `java.util` package, for example: `boolean equal = Arrays.equals(numbers, copy);`
- An array can be converted to a string by using the `Arrays.toString()` or `Arrays.deepToString()` methods from the `java.util` package, for example: `String str = Arrays.toString(numbers);`