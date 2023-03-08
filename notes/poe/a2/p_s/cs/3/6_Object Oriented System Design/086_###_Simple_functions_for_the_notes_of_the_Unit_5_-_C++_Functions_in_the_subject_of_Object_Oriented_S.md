 Here is the content in markdown format for the given topic:

### Simple functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design

1. Functions are blocks of code that perform a specific task. They allow you to organize your code into reusable pieces, avoid repetition, and make your code more readable and manageable.

2. A C++ function definition contains:

    - The function's return type - void if the function does not return a value
    - The function's name
    - Parameters (optional) - input values passed to the function
    - The function's body (within braces) - the code that is executed

3. A function is called by using its name followed by parentheses () and any required parameters.

4. Example of a simple function:

    void hello() {
        std::cout << "Hello!";
    }

    int main() {
        hello();  // Calls the hello function
    }

5. Function parameters:

    - Allow functions to accept input values
    - Listed inside the parentheses in the function definition
    - Used in the function body to modify the behavior of the function

    For example:

    int sum(int num1, int num2) {
        return num1 + num2;
    }

    int main() {
        int total = sum(10, 5);  // Calls sum function with parameters 10 and 5
    }

6. Function return values:

    - The return statement is used to return a value from a function back to the caller
    - The return type of the function defines the type of value that is returned (int, double, etc.)

    For example:

    int multiply(int num1, int num2) {
        return num1 * num2;
    }

    int main() {
        int product = multiply(10, 5);  // Store return value of multiply function in product variable
    }

[ Further explanations, diagrams, code examples, advantages, disadvantages, applications, etc. can be added here for the given topic to make the study material comprehensive. ]