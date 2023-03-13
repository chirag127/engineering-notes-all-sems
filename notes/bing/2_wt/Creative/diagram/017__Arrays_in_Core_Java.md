An array in Java is an object that can store a fixed number of values of the same type. The values are called elements and they are accessed by their index, which starts from 0. An array can be declared as a static field, a local variable, or a method parameter. An array can store primitive values or objects, and can be single-dimensional or multi-dimensional.

#### Arrays in Core Java

The following diagram illustrates the basic structure of a single-dimensional array in Java:

```
+---+---+---+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
+---+---+---+---+---+---+---+---+---+---+
| 5 | 8 | 3 | 9 | 6 | 2 | 4 | 7 | 1 | 0 |
+---+---+---+---+---+---+---+---+---+---+
```

The array has 10 elements, each of type int. The index of the first element is 0 and the index of the last element is 9. The value of the element at index i is shown below the index. For example, the value of the element at index 3 is 9.

To declare an array in Java, we use the following syntax:

```java
type[] arrayName; // declare an array of type
arrayName = new type[size]; // create an array of size
```

For example, to declare and create the array shown in the diagram, we can write:

```java
int[] numbers; // declare an array of int
numbers = new int[10]; // create an array of 10 int
```

To assign values to the elements of the array, we can use the following syntax:

```java
arrayName[index] = value; // assign value to the element at index
```

For example, to assign 5 to the first element of the array, we can write:

```java
numbers[0] = 5; // assign 5 to the element at index 0
```

To access the values of the elements of the array, we can use the same syntax:

```java
value = arrayName[index]; // get the value of the element at index
```

For example, to get the value of the fourth element of the array, we can write:

```java
int x = numbers[3]; // get the value of the element at index 3 and store it in x
```

A multi-dimensional array in Java is an array of arrays. The elements of a multi-dimensional array are arrays themselves. Each array can have a different length, which makes the multi-dimensional array a jagged array. A multi-dimensional array can be declared and created as follows:

```java
type[][] arrayName; // declare a two-dimensional array of type
arrayName = new type[size1][]; // create a two-dimensional array of size1
for (int i = 0; i < size1; i++) {
  arrayName[i] = new type[size2]; // create an array of size2 for each element of the two-dimensional array
}
```

For example, to declare and create a two-dimensional array of int with 3 rows and 4 columns, we can write:

```java
int[][] matrix; // declare a two-dimensional array of int
matrix = new int[3][]; // create a two-dimensional array of 3 rows
for (int i = 0; i < 3; i++) {
  matrix[i] = new int[4]; // create an array of 4 columns for each row
}
```

The following diagram illustrates the structure of the two-dimensional array:

```
+---+---+---+---+
| 0 | 1 | 2 | 3 |
+---+---+---+---+
| 1 | 2 | 3 | 4 |
+---+---+---+---+
| 5 | 6 | 7 | 8 |
+---+---+---+---+
| 9 | 10| 11| 12|
+---+---+---+---+
```

The array has 3 rows and 4 columns, each element of type int. The index of the first row is 0 and the index of the last row is 2. The index of the first column is