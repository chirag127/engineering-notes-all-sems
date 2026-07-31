## Able to define data types and use them in simple data processing applications

- A data type is a classification of data that specifies how the data is stored, manipulated, and interpreted by the computer.
- Data types can be divided into two categories: primitive and composite.
- Primitive data types are the basic types that are built-in to the programming language, such as int, char, float, bool, etc.
- Composite data types are the types that are defined by the programmer using primitive types or other composite types, such as array, structure, union, class, etc.
- An array is a composite data type that stores a fixed number of elements of the same type in a contiguous memory location.
- A structure is a composite data type that stores a group of elements of different types in a single variable.
- An array of structures is a composite data type that stores an array of structure variables, each containing a group of elements of different types.
- An array of structures can be used to store and process complex data that consists of multiple attributes, such as records, students, products, etc.
- To define an array of structures, the syntax is:

```c
struct structure_name {
  // declare the elements of the structure
};

struct structure_name array_name[size]; // declare the array of structures
```

- To access the elements of an array of structures, the syntax is:

```c
array_name[index].element_name; // access the element of a specific structure in the array
```

- To initialize an array of structures, the syntax is:

```c
struct structure_name array_name[size] = {
  // initialize the elements of the first structure
  {value1, value2, ...},
  // initialize the elements of the second structure
  {value3, value4, ...},
  // and so on
};
```

- To use an array of structures in simple data processing applications, some examples are:

  - To read and display the data of n students, each having name, roll number, and marks, the code is:

```c
#include <stdio.h>
#define n 5 // number of students

struct student {
  char name[20];
  int roll;
  float marks;
};

int main() {
  struct student s[n]; // declare an array of structures
  int i;
  // read the data of n students
  for (i = 0; i < n; i++) {
    printf("Enter the name, roll number, and marks of student %d: ", i + 1);
    scanf("%s %d %f", s[i].name, &s[i].roll, &s[i].marks);
  }
  // display the data of n students
  printf("The data of the students are:\n");
  printf("Name\tRoll\tMarks\n");
  for (i = 0; i < n; i++) {
    printf("%s\t%d\t%.2f\n", s[i].name, s[i].roll, s[i].marks);
  }
  return 0;
}
```

  - To sort and display the data of n products, each having name, price, and quantity, the code is:

```c
#include <stdio.h>
#include <string.h>
#define n 5 // number of products

struct product {
  char name[20];
  float price;
  int quantity;
};

// function to sort the array of structures by price in ascending order
void sort(struct product p[n]) {
  int i, j;
  struct product temp;
  for (i = 0; i < n - 1; i++) {
    for (j = 0; j < n - i - 1; j++) {
      if (p[j].price > p[j + 1].price) {
        // swap the structures
        temp = p[j];
        p[j] = p[j + 1];
        p[j + 1] = temp;
      }
    }
  }
}

int main() {
  struct product p[n] = {
    // initialize the array of structures
    {"Pen", 10.0, 50},
    {"Notebook", 20.0, 40},
    {"Eraser", 5.0, 60},
    {"Pencil", 2.0, 100},
    {"Ruler", 15.0, 30}
  };
  int i;
  // display the data of n products before sorting
  printf("The data of the products before sorting are:\n");
  printf("Name\tPrice\tQuantity\n");
  for (i = 0; i < n; i++) {
    printf("%s\t%.2f\t

```
