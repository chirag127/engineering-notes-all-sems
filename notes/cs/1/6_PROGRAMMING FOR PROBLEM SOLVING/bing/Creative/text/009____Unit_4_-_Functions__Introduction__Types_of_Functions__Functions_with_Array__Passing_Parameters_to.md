## Unit 4 - Functions: Introduction, Types of Functions, Functions with Array, Passing Parameters to Functions, Call by Value, Call by Reference, Recursive Functions.

- A function is a block of code that performs a specific task and can be reused in a program.
- A function has a name, a list of parameters, and a return value. The parameters are the input values that the function receives from the caller. The return value is the output value that the function sends back to the caller.
- A function can be defined using the following syntax:

```c
return_type function_name(parameter_list)
{
  // function body
  return value;
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
- Built-in functions are the functions that are predefined in the C library and can be used without defining them. For example, printf(), scanf(), sqrt(), etc.
- User-defined functions are the functions that are created by the programmer to perform a specific task. For example, add(), factorial(), etc.
- Functions can be used with arrays to manipulate the elements of the array. For example, a function can be used to sort an array, to search an element in an array, to calculate the sum of the elements in an array, etc.
- When passing an array to a function, the name of the array is passed as a pointer to the first element of the array. For example:

```c
void print_array(int *arr, int n) // function definition
{
  for(int i = 0; i < n; i++)
  {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

int main()
{
  int a[5] = {1, 2, 3, 4, 5};
  print_array(a, 5); // function call
  return 0;
}
```

- When passing parameters to a function, there are two ways of passing them: call by value and call by reference.
- Call by value means that the function receives a copy of the actual parameters and any changes made to the parameters inside the function do not affect the original values. For example:

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
  printf("After swap: x = %d, y = %d\n", x, y); // no change in x and y
  return 0;
}
```

- Call by reference means that the function receives the addresses of the actual parameters and any changes made to the parameters inside the function affect the original values. For example:

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
  printf("After swap: x = %d, y = %d\n", x, y); // x and y are swapped
  return 0;
}
```

- A recursive function is a function that calls itself to solve a smaller subproblem until a base case is reached. For example, a function to calculate the factorial of a number can be written as:

```c
int factorial(int n) // function definition
{
  if(n == 0 || n == 1) // base case
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
  int n = 5;
  int f = factorial(n); // function call
  printf("The factorial of %d is %d\n", n, f);
  return 0;
}
```
<|im_end|