# Simple functions in C++

- A function is a block of code that performs a specific task, such as calculating the sum of two numbers, printing a message, or sorting an array.
- A function can be called by other parts of the program, or by itself, to execute the code inside it.
- A function can have zero or more parameters, which are variables that hold the values passed to the function when it is called.
- A function can also return a value to the caller, or nothing if it is a void function.
- A function can be defined in one of the following ways:

  - Using the function prototype and the function definition separately. The function prototype declares the name, return type, and parameters of the function, and is usually placed at the beginning of the program or in a header file. The function definition provides the body of the function, and is usually placed after the main function or in a separate source file.
  - Using the function definition only, without the function prototype. This is possible if the function is defined before it is called in the program, or if the function is static, which means it can only be called within the same source file.
  - Using the inline keyword, which instructs the compiler to replace the function call with the function code, instead of generating a separate function call. This can improve the performance of the program, but it is not recommended for large or complex functions.

- A function can be called by using its name and passing the arguments that match its parameters, either by value or by reference. Passing by value means that a copy of the argument is passed to the function, and any changes made to the parameter inside the function do not affect the original argument. Passing by reference means that the address of the argument is passed to the function, and any changes made to the parameter inside the function also affect the original argument.
- A function can also be called by using a function pointer, which is a variable that stores the address of a function. A function pointer can be assigned the address of a function by using the & operator, or by using the function name without parentheses. A function pointer can be used to call the function by using the * operator, or by using the function pointer name with parentheses.
- A function can also be called by using a lambda expression, which is an anonymous function that can be defined and used inline. A lambda expression has the following syntax:

  - [capture list] (parameter list) -> return type {function body}
  - The capture list specifies which variables from the enclosing scope can be accessed by the lambda expression, either by value or by reference. The parameter list and the return type are optional, and can be omitted if the lambda expression has no parameters or returns nothing. The function body contains the code to be executed by the lambda expression.
  - A lambda expression can be assigned to a variable, passed as an argument to another function, or used directly as a function call.

- Some examples of simple functions in C++ are:

  - A function that returns the maximum of four integers:

    ```cpp
    // Function prototype
    int max_of_four(int a, int b, int c, int d);

    // Function definition
    int max_of_four(int a, int b, int c, int d) {
      int max = a; // Initialize max with the first argument
      if (b > max) max = b; // Compare max with the second argument
      if (c > max) max = c; // Compare max with the third argument
      if (d > max) max = d; // Compare max with the fourth argument
      return max; // Return the maximum value
    }

    // Function call
    int x = max_of_four(10, 20, 30, 40); // x = 40
    ```

  - A function that prints a message to the standard output:

    ```cpp
    // Function prototype
    void print_message();

    // Function definition
    void print_message() {
      std::cout << "Hello, world!" << std::endl; // Print the message
    }

    // Function call
    print_message(); // Prints "Hello, world!"
    ```

  - A function that sorts an array of integers using the bubble sort algorithm:

    ```cpp
    // Function prototype
    void bubble_sort(int arr[], int size);

    // Function definition
    void bubble_sort(int arr[], int size) {
      bool swapped; // A flag to indicate if any swap occurred
      do {
        swapped = false; // Initialize swapped to