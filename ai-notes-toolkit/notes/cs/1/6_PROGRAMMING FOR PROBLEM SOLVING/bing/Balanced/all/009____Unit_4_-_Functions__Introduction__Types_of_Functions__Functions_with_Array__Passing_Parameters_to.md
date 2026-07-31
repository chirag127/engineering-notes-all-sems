# Unit 4 - Functions

## Introduction

- A function is a block of code that performs a specific task or a related task.
- A function can be called and reused multiple times.
- A function can take inputs, process them, and return a result.
- A function can make code more efficient, easier to read, and elegant.

## Types of Functions

- There are two types of functions in programming: built-in functions and user-defined functions.
- Built-in functions are predefined functions that are available in the programming language or its libraries. For example, `printf()` in C, `print()` in Python, `alert()` in JavaScript, etc.
- User-defined functions are functions that are created by the programmer to perform a specific task. For example, `factorial()` in C, `square()` in Python, `add()` in JavaScript, etc.

## Functions with Array

- An array is a collection of elements of the same data type that are stored in contiguous memory locations.
- A function can take an array as an input, process its elements, and return an array or a single value as a result.
- To pass an array to a function, we need to specify the name of the array and its size as parameters.
- For example, in C, we can write a function that calculates the sum of the elements of an array as follows:

```c
// A function that takes an array and its size as parameters and returns the sum of its elements
int sum(int arr[], int n) {
  int s = 0; // initialize the sum variable
  for (int i = 0; i < n; i++) { // loop through the array elements
    s = s + arr[i]; // add each element to the sum
  }
  return s; // return the sum
}
```

## Passing Parameters to Functions

- A parameter is a variable that is used to pass information to a function.
- A function can have zero or more parameters, depending on its task.
- A parameter can be of any data type, such as int, float, char, string, array, etc.
- A parameter can be passed to a function in two ways: by value or by reference.

## Call by Value

- Call by value is a method of passing parameters to a function where the actual value of the parameter is copied to the function.
- In call by value, the changes made to the parameter inside the function do not affect the original value outside the function.
- Call by value is the default method of passing parameters in most programming languages, such as C, Python, JavaScript, etc.
- For example, in C, we can write a function that swaps the values of two variables using call by value as follows:

```c
// A function that takes two int parameters by value and swaps their values
void swap(int a, int b) {
  int temp; // declare a temporary variable
  temp = a; // store the value of a in temp
  a = b; // assign the value of b to a
  b = temp; // assign the value of temp to b
  printf("Inside the function, a = %d and b = %d\n", a, b); // print the values of a and b inside the function
}

int main() {
  int x = 10, y = 20; // declare and initialize two variables
  printf("Before calling the function, x = %d and y = %d\n", x, y); // print the values of x and y before calling the function
  swap(x, y); // call the function with x and y as arguments
  printf("After calling the function, x = %d and y = %d\n", x, y); // print the values of x and y after calling the function
  return 0;
}
```

The output of the above program is:

```
Before calling the function, x = 10 and y = 20
Inside the function, a = 20 and b = 10
After calling the function, x = 10 and y = 20
```

As we can see, the values of x and y are swapped inside the function, but they remain unchanged outside the function.

## Call by Reference

- Call by reference is a method of passing parameters to a function where the address of the