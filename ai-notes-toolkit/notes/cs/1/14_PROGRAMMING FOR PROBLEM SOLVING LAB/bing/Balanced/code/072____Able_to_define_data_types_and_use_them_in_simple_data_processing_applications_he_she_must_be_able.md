## Able to define data types and use them in simple data processing applications

- A data type is a classification of data that specifies how the data is stored, manipulated, and displayed by a programming language.
- Data types can be primitive or composite, depending on whether they are built-in or user-defined.
- Primitive data types are the basic types that are supported by the language, such as int, char, float, bool, etc.
- Composite data types are the types that are composed of other types, such as arrays, structures, classes, etc.
- An array is a composite data type that stores a collection of elements of the same type in a contiguous memory location.
- A structure is a composite data type that stores a collection of elements of different types in a single variable.
- An array of structures is a composite data type that stores an array of structure variables, each containing elements of different types.
- An array of structures can be used to store and process complex data, such as records, tables, etc.
- To define an array of structures, the following steps are required:
  - Define the structure type using the struct keyword and specify the names and types of the elements.
  - Declare an array of structure variables using the structure type name and the array size.
  - Initialize the array of structure variables using curly braces and comma-separated values for each structure variable.
- To use an array of structures in simple data processing applications, the following steps are required:
  - Access the elements of the array of structures using the array index and the dot operator.
  - Perform operations on the elements of the array of structures using the assignment operator, arithmetic operators, logical operators, etc.
  - Pass the array of structures as a parameter to a function using the array name and the structure type name.
  - Return the array of structures from a function using the return statement and the array name.
- Example: Define an array of structures to store the name, age, and salary of three employees and calculate their average salary.

```c
// Define the structure type
struct employee {
  char name[20];
  int age;
  float salary;
};

// Declare an array of structure variables
struct employee emp[3];

// Initialize the array of structure variables
emp[0] = {"Alice", 25, 5000.0};
emp[1] = {"Bob", 30, 6000.0};
emp[2] = {"Charlie", 35, 7000.0};

// Access the elements of the array of structures
printf("Name\tAge\tSalary\n");
for (int i = 0; i < 3; i++) {
  printf("%s\t%d\t%.2f\n", emp[i].name, emp[i].age, emp[i].salary);
}

// Perform operations on the elements of the array of structures
float sum = 0.0;
float avg = 0.0;
for (int i = 0; i < 3; i++) {
  sum += emp[i].salary;
}
avg = sum / 3;
printf("Average salary: %.2f\n", avg);
```