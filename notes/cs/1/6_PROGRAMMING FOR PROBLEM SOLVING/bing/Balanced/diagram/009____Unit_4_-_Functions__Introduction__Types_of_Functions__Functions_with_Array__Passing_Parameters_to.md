## Unit 4 - Functions: Introduction, Types of Functions, Functions with Array, Passing Parameters to Functions, Call by Value, Call by Reference, Recursive Functions.

- A function is a block of code that performs a specific task and can be reused in a program.
- A function has a name, a list of parameters, and a return value. The parameters are the inputs to the function, and the return value is the output of the function.
- A function can be defined using the following syntax:

```c
return_type function_name(parameter_list)
{
    // function body
    // statements
    return expression;
}
```

- A function can be called by using its name and passing the arguments that match the parameters. For example:

```c
int add(int a, int b) // function definition
{
    int c = a + b;
    return c;
}

int main()
{
    int x = 10, y = 20;
    int z = add(x, y); // function call
    printf("The sum is %d\n", z);
    return 0;
}
```

- There are two types of functions in C: built-in functions and user-defined functions.
- Built-in functions are the ones that are predefined in the C library, such as `printf`, `scanf`, `sqrt`, etc. They can be used directly without any definition.
- User-defined functions are the ones that are created by the programmer to perform specific tasks. They need to be defined before they can be used.
- Functions can be used with arrays to perform operations on the elements of the array. For example, a function can be used to find the maximum element in an array, or to sort an array, or to search for an element in an array, etc.
- To pass an array to a function, we need to specify the name of the array and the size of the array as parameters. For example:

```c
void print_array(int arr[], int n) // function definition
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main()
{
    int a[5] = {10, 20, 30, 40, 50};
    print_array(a, 5); // function call
    return 0;
}
```

- When we pass parameters to a function, there are two ways of passing them: call by value and call by reference.
- Call by value means that the function receives a copy of the actual parameters, and any changes made to the parameters inside the function do not affect the original values. For example:

```c
void swap(int a, int b) // function definition
{
    int temp = a;
    a = b;
    b = temp;
}

int main()
{
    int x = 10, y = 20;
    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(x, y); // function call
    printf("After swap: x = %d, y = %d\n", x, y); // no change
    return 0;
}
```

- Call by reference means that the function receives the address of the actual parameters, and any changes made to the parameters inside the function affect the original values. For example:

```c
void swap(int *a, int *b) // function definition
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int x = 10, y = 20;
    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(&x, &y); // function call
    printf("After swap: x = %d, y = %d\n", x, y); // change
    return 0;
}
```

- A recursive function is a function that calls itself within its body. A recursive function must have a base case, which is a condition that stops the recursion, and a recursive case, which is a condition that continues the recursion. For example:

```c
int factorial(int n) // function definition
{
    if (n == 0) // base case
    {
        return 1;
    }
    else // recursive case
    {
        return n * factorial(n - 1); // function call
    }
}

int main()
{
    int x = 5;
    int y = factorial(x); // function call
    printf("The factorial of %d is %d\n", x, y);
    return 0;
}
```