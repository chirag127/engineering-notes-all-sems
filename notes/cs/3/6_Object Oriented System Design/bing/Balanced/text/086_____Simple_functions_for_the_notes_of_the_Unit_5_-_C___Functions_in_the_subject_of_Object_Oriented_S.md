### Simple functions in C++

- A function is a block of code that performs a specific task, such as calculating the sum of two numbers, printing a message, or sorting an array.
- A function can be called by another function or by the main program, and can also call other functions within itself.
- A function has a name, a list of parameters, and a return type. For example, the function `int max_of_four(int a, int b, int c, int d)` returns the maximum of the four arguments it receives.
- A function definition consists of the function header and the function body. The function header specifies the name, parameters, and return type of the function. The function body contains the statements that implement the logic of the function. For example:

```c++
// Function header
int max_of_four(int a, int b, int c, int d) {
  // Function body
  int max = a; // Assume a is the largest
  if (b > max) // Compare b with max
    max = b; // Update max if b is larger
  if (c > max) // Compare c with max
    max = c; // Update max if c is larger
  if (d > max) // Compare d with max
    max = d; // Update max if d is larger
  return max; // Return the maximum value
}
```

- A function can be declared before it is defined, using a function prototype. A function prototype is a statement that tells the compiler the name, parameters, and return type of the function, without providing the function body. For example:

```c++
// Function prototype
int max_of_four(int a, int b, int c, int d);
```

- A function prototype allows the compiler to check the validity of the function calls, and also helps the programmer to organize the code better.
- A function can be defined in a different file from where it is called, as long as the function prototype is included in the file that calls the function. For example, if the function `max_of_four` is defined in a file called `max.cpp`, and the main program is in a file called `main.cpp`, then the main program can call the function `max_of_four` by including the function prototype in `main.cpp`, and linking the two files during compilation. For example:

```c++
// main.cpp
#include <iostream>
using namespace std;

// Function prototype
int max_of_four(int a, int b, int c, int d);

int main() {
  int a, b, c, d;
  cout << "Enter four numbers: ";
  cin >> a >> b >> c >> d;
  cout << "The maximum is: " << max_of_four(a, b, c, d) << endl;
  return 0;
}
```

```c++
// max.cpp
// Function definition
int max_of_four(int a, int b, int c, int d) {
  // Function body
  int max = a; // Assume a is the largest
  if (b > max) // Compare b with max
    max = b; // Update max if b is larger
  if (c > max) // Compare c with max
    max = c; // Update max if c is larger
  if (d > max) // Compare d with max
    max = d; // Update max if d is larger
  return max; // Return the maximum value
}
```

- To compile and run the program, the two files need to be linked together. For example, using the g++ compiler, the command would be:

```bash
g++ main.cpp max.cpp -o main
```

- This would create an executable file called `main`, which can be run as:

```bash
./main
```

- A function can also be defined inside another function, which is called a nested function. A nested function can only be called by the function that contains it, and cannot be accessed by other functions. A nested function can access the variables and parameters of the outer function, but cannot modify them. For example:

```c++
// A function that calculates the factorial of a number
int factorial(int n) {
  // A nested function that checks if a number is positive
  bool is_positive(int x) {
    return x > 0;
  }
  // Check if n is positive
  if (is_positive(n)) {
    // Calculate the factorial using recursion
    if (n == 0 || n == 1

```
