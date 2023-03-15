Hello, I am Sydney, your AI assistant. I can help you with your study material for Object Oriented System Design. Here are some notes on the topic of default arguments for the Unit 5 - C++ Functions.

### Default arguments

- Default arguments are arguments that have a predefined value in a function declaration.
- They are used when the function is called without passing the corresponding argument or when the argument is omitted.
- Default arguments can make the function call more concise and flexible, as well as provide reasonable default values for the parameters.
- Default arguments are specified in the function declaration, not in the function definition.
- The syntax for default arguments is:

```cpp
return_type function_name(parameter1 = value1, parameter2 = value2, ...);
```

- The default values can be any valid C++ expressions, such as constants, variables, or function calls.
- The default arguments are evaluated at the point of the function call, not at the point of the function declaration.
- The default arguments can be overridden by passing explicit arguments in the function call.
- The default arguments must be specified from right to left, meaning that if a parameter has a default value, all the parameters to its right must also have default values.
- The default arguments cannot be redefined in later declarations of the same function.
- The default arguments are not part of the function signature, meaning that they do not affect the function overloading or the function pointer type.

- Here are some examples of using default arguments in C++ functions:

```cpp
// A function that prints a message with a given number of times and a separator
// The default value for times is 1 and for sep is '\n'
void print_message(string message, int times = 1, char sep = '\n')
{
    for (int i = 0; i < times; i++)
    {
        cout << message << sep;
    }
}

// A function that calculates the area of a rectangle with a given length and width
// The default value for width is the same as length, meaning that the function can also calculate the area of a square
double area(double length, double width = length)
{
    return length * width;
}

// A function that returns the maximum of three integers
// The default values for b and c are the minimum value of int, meaning that the function can also return the maximum of one or two integers
int max(int a, int b = INT_MIN, int c = INT_MIN)
{
    return a > b ? (a > c ? a : c) : (b > c ? b : c);
}

// A function that swaps two integers using references
// The default value for b is a reference to a global variable named temp, meaning that the function can also swap one integer with temp
int temp = 0;
void swap(int& a, int& b = temp)
{
    int t = a;
    a = b;
    b = t;
}

// A function that returns the sum of an array of integers with a given size
// The default value for size is -1, meaning that the function will calculate the size of the array using the sizeof operator
int sum(int arr[], int size = -1)
{
    if (size == -1)
    {
        size = sizeof(arr) / sizeof(arr[0]);
    }
    int s = 0;
    for (int i = 0; i < size; i++)
    {
        s += arr[i];
    }
    return s;
}
```

- Here are some examples of calling the functions with default arguments:

```cpp
// Calling the print_message function with different arguments
print_message("Hello"); // prints "Hello\n"
print_message("Hello", 3); // prints "Hello\nHello\nHello\n"
print_message("Hello", 3, '*'); // prints "Hello*Hello*Hello*"

// Calling the area function with different arguments
cout << area(10) << endl; // prints 100, the area of a square with side 10
cout << area(10, 5) << endl; // prints 50, the area of a rectangle with length 10 and width 5

// Calling the max function with different arguments
cout << max(10) << endl; // prints 10, the maximum of one integer
cout << max(10, 20) << endl; // prints 20, the maximum of two integers
cout << max(10, 20, 30) << endl; // prints 30, the maximum of three integers

// Calling the swap function with different arguments
int x = 10, y = 20;
swap(x); // swaps x with temp, x becomes