### Arrays

Arrays are a collection of similar or different types of data elements stored under a single name. These data elements are accessed using an index or a subscript number, which starts from 0 to n-1. Arrays are useful when we have to deal with a large amount of data of the same type.

#### Array Notation and Representation

Arrays can be declared and initialized in different ways. The most common way is to declare an array with a fixed size and initialize it with values. For example:

```
int arr[5] = {1, 2, 3, 4, 5};
```

This declares an integer array `arr` of size 5 and initializes it with the values 1 to 5.

#### Manipulating Array Elements

Array elements can be accessed and manipulated using their index number. For example:

```
arr[0] = 10; // assigns 10 to the first element of the array
```

Arrays can also be traversed using loops. For example:

```
for (int i = 0; i < 5; i++) {
    cout << arr[i] << " ";
}
```

This prints all the elements of the array.

#### Using Multi Dimensional Arrays

Arrays can have more than one dimension. For example, a two-dimensional array can be declared and initialized as follows:

```
int arr[3][2] = {{1, 2}, {3, 4}, {5, 6}};
```

This declares a two-dimensional integer array `arr` of size 3x2 and initializes it with the values 1 to 6.

#### Character Arrays and Strings

Character arrays are arrays of characters that are used to store strings. Strings are a sequence of characters terminated by a null character '\0'. For example:

```
char str[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
```

This declares a character array `str` of size 6 and initializes it with the string "Hello".

#### Structure, Union, Enumerated Data types

Structures, unions, and enumerated data types are user-defined data types that can hold multiple data elements of different data types. Structures and unions are similar, except that structures allocate memory for each data element, while unions allocate memory for the largest data element only.

Enumerated data types are used to define a set of named constants. For example:

```
enum Color {Red, Green, Blue};
```

This declares an enumerated data type `Color` with three named constants Red, Green, and Blue.

#### Array of Structures

An array of structures is an array that contains structures as its elements. For example:

```
struct Employee {
    char name[50];
    int age;
    float salary;
};

Employee emp[3] = {{"John", 30, 5000.00}, {"Mary", 25, 4000.00}, {"David", 35, 6000.00}};
```

This declares a structure `Employee` and initializes an array `emp` of size 3 with three structures.

#### Passing Arrays to Functions

Arrays can be passed to functions by reference or by pointer. When passed by reference, any changes made to the array within the function will reflect in the original array. For example:

```
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
}

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    printArray(arr, 5);
    return 0;
}
```

This declares a function `printArray` that takes an integer array and its size as parameters and prints all its elements. The function is then called from the main function with an integer array `arr` of size 5.