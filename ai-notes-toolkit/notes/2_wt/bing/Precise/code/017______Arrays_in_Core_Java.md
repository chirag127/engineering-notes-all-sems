#### Arrays in Core Java
An array is a collection of elements of the same type, stored in contiguous memory locations. Here is an example of how to declare, initialize, and access an array in Java:

```java
int[] myArray = new int[5]; // declaration and initialization of an array of size 5
myArray[0] = 1; // assigning value to the first element
myArray[1] = 2; // assigning value to the second element
myArray[2] = 3; // assigning value to the third element
myArray[3] = 4; // assigning value to the fourth element
myArray[4] = 5; // assigning value to the fifth element

for (int i = 0; i < myArray.length; i++) { // accessing elements of the array
    System.out.println(myArray[i]);
}
```