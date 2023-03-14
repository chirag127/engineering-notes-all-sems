#### Arrays in Core Java

- An array is a collection of elements of the same data type that are stored in contiguous memory locations and can be accessed by using an index.
- An array can be declared by specifying the data type followed by square brackets and the array name, for example: `int[] numbers;`
- An array can be initialized by using the `new` operator and specifying the size of the array, for example: `numbers = new int[10];`
- Alternatively, an array can be initialized by using an array literal, which is a list of values enclosed in curly braces, for example: `numbers = new int[]{1, 2, 3, 4, 5};`
- The elements of an array can be accessed by using the array name and the index of the element in square brackets, for example: `numbers[0]` returns the first element of the array, which is 1.
- The index of an array starts from 0 and goes up to the size of the array minus one, for example: the last element of the array `numbers` is `numbers[4]`, which is 5.
- The size of an array can be obtained by using the `length` property of the array, for example: `numbers.length` returns 5.
- An array can be traversed by using a loop, such as a `for` loop or a `for-each` loop, for example:

```java
// using a for loop
for (int i = 0; i < numbers.length; i++) {
  System.out.println(numbers[i]);
}

// using a for-each loop
for (int num : numbers) {
  System.out.println(num);
}
```

- An array can be modified by assigning a new value to an element of the array, for example: `numbers[2] = 10;` changes the third element of the array from 3 to 10.
- An array can be passed as a parameter to a method by using the array name, for example:

```java
public static void printArray(int[] arr) {
  for (int num : arr) {
    System.out.println(num);
  }
}

// calling the method
printArray(numbers);
```

- An array can be returned from a method by using the `return` statement, for example:

```java
public static int[] reverseArray(int[] arr) {
  int[] reversed = new int[arr.length];
  for (int i = 0; i < arr.length; i++) {
    reversed[i] = arr[arr.length - 1 - i];
  }
  return reversed;
}

// calling the method
int[] reversedNumbers = reverseArray(numbers);
```

- An array can be multidimensional, which means it can have more than one dimension, for example: a two-dimensional array is an array of arrays, where each element is another array.
- A two-dimensional array can be declared by using two pairs of square brackets, for example: `int[][] matrix;`
- A two-dimensional array can be initialized by using the `new` operator and specifying the number of rows and columns, for example: `matrix = new int[3][4];`
- Alternatively, a two-dimensional array can be initialized by using a nested array literal, which is a list of lists enclosed in curly braces, for example: `matrix = new int[][]{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};`
- The elements of a two-dimensional array can be accessed by using the array name and the row and column indices in square brackets, for example: `matrix[0][1]` returns the second element of the first row, which is 2.
- The size of a two-dimensional array can be obtained by using the `length` property of the array, for example: `matrix.length` returns 3, which is the number of rows, and `matrix[0].length` returns 4, which is the number of columns.
- A two-dimensional array can be traversed by using nested loops, for example:

```java
// using nested for loops
for (int i = 0; i < matrix.length; i++) {
  for (int j = 0; j < matrix[i].length; j++) {
    System.out.print(matrix[i][j] + " ");
  }
  System.out.println();
}

// using nested for-each loops
for (int[] row : matrix) {
  for (int num : row) {
    System.out.print(num + " ");
  }
  System.out.println();
}
```

- A