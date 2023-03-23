 Here is the content in Markdown format without any emojis or external links, written in points and in a formal tone:

### JS Functions for the notes of the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing

1. Functions are a block of code that can be reused and called by their name whenever needed. They provide modularity and reusability to the code.

2. To define a function in JavaScript, use the function keyword followed by:

- The name of the function
- Parentheses ()
- The code to be executed within braces {}

For example:
function greet() {
    console.log("Hello!");
}

3. To call or execute a function, use its name followed by parentheses:
greet(); // logs "Hello!"

4. Functions can take inputs (known as parameters) and return outputs (using the return keyword):
function sum(a, b) {
    return a + b;
}

sum(5, 10); // returns 15

5. Arrow functions are an alternative, shorter syntax for writing functions in modern JavaScript. They have implicit returns and do not bind their own this, arguments, super, or new.target.
For example:
const sum = (a, b) => a + b;

sum(5, 10); // returns 15

6. Functions are first-class objects in JavaScript, which means they can be assigned to variables and properties of objects, passed as arguments to other functions, and returned from functions.

For example:
const square = function(x) {
    return x * x;
}

[1, 2, 3].map(square); // [1, 4, 9]