#### Arrays in Core Java

- An array is an object that can store a fixed number of values of the same type .
- An array can be used as a static field, a local variable, or a method parameter .
- The elements of an array are indexed, which means we can access them with numbers (called indices).
- The index of the first element of an array is 0, and the index of the last element is array.length - 1, where array.length is the number of elements in the array .
- To declare an array, we need to specify the type of the elements and the size of the array in square brackets, for example: `int[] numbers = new int[5];`.
- To initialize an array, we can assign values to each element using the index, for example: `numbers[0] = 10; numbers[1] = 20;` etc. or we can use an array literal, which is a list of values separated by commas and enclosed in curly braces, for example: `int[] numbers = {10, 20, 30, 40, 50};`.
- We can also create multidimensional arrays, which are arrays of arrays, for example: `int[][] matrix = new int[3][3];` creates a 3 by 3 matrix of integers.
- To access or modify an element of a multidimensional array, we need to specify the indices of both the subarray and the element, for example: `matrix[0][0] = 1; matrix[1][1] = 2;` etc. or we can use nested array literals, for example: `int[][] matrix = {{1, 0, 0}, {0, 2, 0}, {0, 0, 3}};`.
- Arrays are useful for storing and manipulating data that have a fixed size and a homogeneous type.
- Arrays can be passed as arguments to methods or returned from methods, but the reference to the array object is passed or returned, not the array itself.
- Arrays inherit from the Object class and implement the Serializable and Cloneable interfaces.
- Arrays have a public final field called length that stores the number of elements in the array.
- Arrays have a public method called clone() that returns a copy of the array object.
- Arrays can be sorted using the Arrays.sort() method from the java.util package.
- Arrays can be compared for equality using the Arrays.equals() method from the java.util package.
- Arrays can be converted to strings using the Arrays.toString() method from the java.util package.

A possible mnemonic to remember the features of arrays in Java is:

**A**rrays are objects that store fixed number of values of the same type.

**R**eference to the array object is passed or returned, not the array itself.

**R**ows and columns are used to access or modify multidimensional arrays.

**A**rrays inherit from Object and implement Serializable and Cloneable.

**Y**ou can use Arrays class methods to sort, compare, and convert arrays.

**S**ize of the array is specified in square brackets and can be accessed by length field.