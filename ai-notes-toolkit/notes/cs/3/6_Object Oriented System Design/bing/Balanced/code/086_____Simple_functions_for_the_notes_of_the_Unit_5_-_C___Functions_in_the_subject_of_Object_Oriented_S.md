### Simple functions in C++

- A function is a block of code that performs a specific task, such as calculating the sum of two numbers, printing a message, or sorting an array.
- A function can be called by another function or by the main program, and can also call other functions within itself.
- A function has a name, a list of parameters, and a return type. For example, `int max_of_four(int a, int b, int c, int d)` is a function that takes four integers as parameters and returns the maximum of them as an integer.
- A function definition consists of the function header and the function body. The function header specifies the name, parameters, and return type of the function. The function body contains the statements that implement the logic of the function. For example:

```cpp
// function header
int max_of_four(int a, int b, int c, int d) {
  // function body
  int max = a; // initialize max with the first parameter
  if (b > max) max = b; // compare max with the second parameter
  if (c > max) max = c; // compare max with the third parameter
  if (d > max) max = d; // compare max with the fourth parameter
  return max; // return the maximum value
}
```

- A function can be declared before it is defined, using a function prototype. A function prototype is a statement that tells the compiler the name, parameters, and return type of the function, without providing the function body. For example:

```cpp
// function prototype
int max_of_four(int a, int b, int c, int d);
```

- A function prototype allows the compiler to check the validity of the function calls, and also helps the programmer to organize the code structure.
- A function can be defined in a different file from where it is called, as long as the function prototype is included in the file that calls the function. For example, if the function `max_of_four` is defined in a file called `max.cpp`, and the main program that calls the function is in a file called `main.cpp`, then the file `main.cpp` should include the function prototype as follows:

```cpp
// main.cpp
#include <iostream>
using namespace std;

// function prototype
int max_of_four(int a, int b, int c, int d);

int main() {
  // call the function and print the result
  cout << max_of_four(10, 20, 30, 40) << endl;
  return 0;
}
```

- The file `max.cpp` should include the function definition as follows:

```cpp
// max.cpp
// function definition
int max_of_four(int a, int b, int c, int d) {
  // function body
  int max = a; // initialize max with the first parameter
  if (b > max) max = b; // compare max with the second parameter
  if (c > max) max = c; // compare max with the third parameter
  if (d > max) max = d; // compare max with the fourth parameter
  return max; // return the maximum value
}
```

- A function can also be defined in a header file, and then included in the file that calls the function. For example, if the function `max_of_four` is defined in a file called `max.h`, and the main program that calls the function is in a file called `main.cpp`, then the file `main.cpp` should include the header file as follows:

```cpp
// main.cpp
#include <iostream>
#include "max.h" // include the header file that contains the function definition
using namespace std;

int main() {
  // call the function and print the result
  cout << max_of_four(10, 20, 30, 40) << endl;
  return 0;
}
```

- The file `max.h` should include the function definition as follows:

```cpp
// max.h
// function definition
int max_of_four(int a, int b, int c, int d) {
  // function body
  int max = a; // initialize max with the first parameter
  if (b > max) max = b; // compare max with the second parameter
  if (c > max) max = c; // compare max with the third parameter
  if (d > max) max = d; // compare max with the fourth parameter
  return max; // return

```
