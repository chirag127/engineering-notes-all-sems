## Able to define data types and use them in simple data processing applications

- A data type is a classification of data that specifies how the data is stored, manipulated, and displayed by a programming language.
- Data types can be primitive or composite, depending on whether they are built-in or user-defined, and whether they can hold one or more values.
- A primitive data type is a basic data type that can hold only one value at a time, such as int, char, float, or boolean.
- A composite data type is a data type that can hold multiple values of the same or different types, such as array, structure, union, or class.
- An array is a composite data type that can store a fixed number of values of the same type in a contiguous memory location.
- A structure is a composite data type that can store a group of values of different types under a single name.
- An array of structures is a composite data type that can store multiple structures of the same type in an array.
- An array of structures can be used to store and process complex data that has multiple attributes, such as records of students, employees, products, etc.
- To define an array of structures, we need to first define the structure type, then declare the array of that type, and then initialize the array elements with the structure values.
- For example, to define an array of structures to store the details of three students, we can write:

```c
// Define the structure type
struct student {
  int roll_no;
  char name[20];
  float marks;
};

// Declare the array of structures
struct student students[3];

// Initialize the array elements with the structure values
students[0] = {1, "Alice", 85.5};
students[1] = {2, "Bob", 76.0};
students[2] = {3, "Charlie", 92.0};
```

- To access and manipulate the data in an array of structures, we can use the array index and the dot operator to refer to the structure fields.
- For example, to print the name and marks of the second student in the array, we can write:

```c
// Print the name and marks of the second student
printf("Name: %s\n", students[1].name);
printf("Marks: %.2f\n", students[1].marks);
```

- To use an array of structures in a simple data processing application, we can write functions that perform operations on the array, such as sorting, searching, updating, deleting, etc.
- For example, to write a function that sorts an array of structures based on the marks in ascending order, we can use the bubble sort algorithm and compare the marks field of the structures, as shown below:

```c
// Define a function that sorts an array of structures based on the marks
void sort_students(struct student students[], int n) {
  // n is the number of elements in the array
  int i, j;
  struct student temp; // a temporary variable to swap the structures
  // Loop through the array n-1 times
  for (i = 0; i < n-1; i++) {
    // Loop through the array from 0 to n-i-1
    for (j = 0; j < n-i-1; j++) {
      // Compare the marks of the current and next element
      if (students[j].marks > students[j+1].marks) {
        // Swap the structures if the current element has higher marks
        temp = students[j];
        students[j] = students[j+1];
        students[j+1] = temp;
      }
    }
  }
}
```