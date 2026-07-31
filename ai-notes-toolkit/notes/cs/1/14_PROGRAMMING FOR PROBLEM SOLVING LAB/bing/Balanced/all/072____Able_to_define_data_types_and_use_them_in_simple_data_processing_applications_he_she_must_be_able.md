# Able to define data types and use them in simple data processing applications

- A data type is a classification of data that specifies how the data is stored, manipulated, and interpreted by the computer.
- Data types can be divided into two categories: primitive and composite.
- Primitive data types are the basic types that are built into the programming language, such as int, char, float, double, boolean, etc.
- Composite data types are the types that are defined by the programmer using primitive data types or other composite data types, such as arrays, structures, classes, etc.
- An array is a composite data type that stores a collection of elements of the same data type in a contiguous memory location.
- A structure is a composite data type that stores a collection of elements of different data types in a single variable.
- An array of structures is a composite data type that stores an array of structure variables, each of which can hold different types of data.
- An array of structures can be used to store and process complex data that consists of multiple attributes, such as records of students, employees, products, etc.
- To define an array of structures, the following steps are required:
  - Define the structure type using the keyword struct and specify the names and data types of the elements inside curly braces.
  - Declare an array of structure variables using the structure type name and specify the size of the array in square brackets.
  - Initialize the array of structure variables by assigning values to the elements of each structure variable using curly braces and commas.
- To access and manipulate the elements of an array of structures, the following syntax is used:
  - array_name[index].element_name
  - where array_name is the name of the array of structure variables, index is the position of the structure variable in the array, and element_name is the name of the element in the structure variable.
- Example: Define an array of structures to store the name, age, and grade of three students and print their details.

```c
// Define the structure type
struct student {
  char name[20];
  int age;
  char grade;
};

// Declare an array of structure variables
struct student students[3];

// Initialize the array of structure variables
students[0] = {"Alice", 18, 'A'};
students[1] = {"Bob", 19, 'B'};
students[2] = {"Charlie", 20, 'C'};

// Print the details of each student
for (int i = 0; i < 3; i++) {
  printf("Name: %s\n", students[i].name);
  printf("Age: %d\n", students[i].age);
  printf("Grade: %c\n", students[i].grade);
  printf("\n");
}
```