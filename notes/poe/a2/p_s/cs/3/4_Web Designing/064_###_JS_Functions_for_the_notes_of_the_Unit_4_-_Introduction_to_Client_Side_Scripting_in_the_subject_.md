 Here is the content in markdown format for the topic ### JS Functions for the notes of the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing:

# JS Functions

A function in JavaScript is a block of code that can be executed whenever it is invoked. It allows you to organize your code, make it more readable, reuse it and also abstract away some logic.

## Declaring a function

A function can be declared in JavaScript in multiple ways:

1. Function declaration:

    function myFunction(arg1, arg2) {
       // code to be executed
    }

2. Function expression:

    var myFunction = function(arg1, arg2) {
       // code to be executed
    }

3. Arrow function:

    var myFunction = (arg1, arg2) => {
       // code to be executed
    }

The syntax for declaring a function consists of:

- The function keyword
- The name of the function
- A list of parameters (arguments) enclosed in parentheses ()
- The function body enclosed in curly brackets {}

The parameters are the inputs that a function takes and the function body contains a sequence of statements that define the function's logic.

## Invoking a function

A function is not executed when it is declared but when it is invoked (called).

To invoke a function, you need to specify its name followed by () :

myFunction(); // invoking the function

You can pass in arguments to the function if it accepts parameters:

myFunction(arg1, arg2); // invoking the function with arguments

The arguments are the actual values passed to (and received by) the parameters.

[Detailed explanations of function scope, return statements, recursion etc. can be included here with examples]

Advantages of using functions:
- Code reusability
- Organized and structured code
- Abstraction

Disadvantages:
- Extra processing required to invoke functions
- Nested functions can affect performance

Applications of functions:
- Performs a task multiple times
- Breaks down complex problems into simpler sub-problems
- Abstraction and modularity
- Code reusability

[Markdown tables, diagrams and code snippets can be included here if required to explain the concepts]