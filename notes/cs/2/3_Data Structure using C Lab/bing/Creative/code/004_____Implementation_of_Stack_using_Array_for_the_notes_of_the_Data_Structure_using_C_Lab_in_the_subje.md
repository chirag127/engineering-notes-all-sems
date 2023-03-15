### Implementation of Stack using Array

A stack is a linear data structure that follows the LIFO (Last In First Out) principle. It means that the last element inserted into the stack is the first one to be removed. A stack has two basic operations: push and pop. Push adds an element to the top of the stack, and pop removes and returns the top element of the stack. A stack can be implemented using an array in C as follows:

- Declare an array of a fixed size to store the stack elements. For example, `int stack[10];`
- Declare a variable to keep track of the top of the stack. For example, `int top = -1;`
- To push an element into the stack, first check if the stack is full or not. If the stack is full, then print an error message and return. Otherwise, increment the top variable and assign the element to the stack array at the top index. For example,

```c
void push(int element)
{
    if (top == 9) // stack is full
    {
        printf("Stack overflow\n");
        return;
    }
    top++; // increment top
    stack[top] = element; // assign element to stack
}
```

- To pop an element from the stack, first check if the stack is empty or not. If the stack is empty, then print an error message and return. Otherwise, store the top element of the stack in a temporary variable, decrement the top variable, and return the temporary variable. For example,

```c
int pop()
{
    if (top == -1) // stack is empty
    {
        printf("Stack underflow\n");
        return -1;
    }
    int temp = stack[top]; // store top element
    top--; // decrement top
    return temp; // return top element
}
```

- To display the stack elements, loop through the stack array from the top index to the bottom index and print each element. For example,

```c
void display()
{
    if (top == -1) // stack is empty
    {
        printf("Stack is empty\n");
        return;
    }
    for (int i = top; i >= 0; i--) // loop from top to bottom
    {
        printf("%d ", stack[i]); // print element
    }
    printf("\n");
}
```

- To test the stack implementation, write a main function that performs some push and pop operations on the stack and displays the stack after each operation. For example,

```c
int main()
{
    push(10); // push 10
    display(); // display stack
    push(20); // push 20
    display(); // display stack
    push(30); // push 30
    display(); // display stack
    pop(); // pop 30
    display(); // display stack
    pop(); // pop 20
    display(); // display stack
    pop(); // pop 10
    display(); // display stack
    pop(); // pop error
    display(); // display stack
    return 0;
}
```

- The output of the above program should be:

```
10 
10 20 
10 20 30 
10 20 
10 
Stack is empty
Stack underflow
Stack is empty
```