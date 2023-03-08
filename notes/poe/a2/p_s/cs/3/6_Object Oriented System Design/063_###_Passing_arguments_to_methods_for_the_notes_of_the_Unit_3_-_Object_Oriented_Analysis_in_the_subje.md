 Here is the content in markdown format for the topic ### Passing arguments to methods for the notes of the Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design:

### Passing arguments to methods

- Methods in a class can take in values from the user in the form of arguments to process the logic.
- These arguments can be passed to the methods in multiple ways:

1.  By value - The actual value is passed to the method. Changes made to the argument inside the method do not reflect outside.
2.  By reference - The address of the argument is passed to the method. Changes made to the argument inside the method reflect outside.
3.  By constant reference - The address of the constant argument is passed to the method. Changes cannot be made to the argument inside the method.

Advantages of passing by reference:
- Memory efficient as only address is passed instead of the actual value.
- Changes made to the argument inside the method is reflected outside.

Disadvantages of passing by reference:
- Unintentional changes to the argument may produce undesired results as the changes are reflected outside the method as well.

Examples of passing arguments to methods:

By value:
int sum(int num) {
    return num + 1;
}

sum(5); // Returns 6

By reference:
void increment(int& num) {
    num++;
}

int num = 5;
increment(num); // num is now 6

By constant reference:
void print(const int& num) {
    // Cannot modify num here
}

Applications of passing arguments:
- Methods can take in user inputs and process on them.
- Reduce repetition of code by passing values/references to reusable methods.
- Encapsulate logic within methods to make code modular, organized and readable.