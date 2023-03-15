A function in JavaScript is a reusable block of code that performs a specific task, taking some form of input and returning an output. A function can be defined with the function keyword, followed by a name, followed by parentheses that may include parameter names separated by commas. A function can also be assigned to a variable or a property, or passed to or returned from another function. A function can have properties and methods just like any other object. Here is an example of a function definition and a function call in JavaScript:

```javascript
// Define a function named square that takes a parameter named x
function square(x) {
  // Return the square of x
  return x * x;
}

// Call the function with the argument 5 and assign the result to a variable named y
var y = square(5);

// Print the value of y
console.log(y); // 25
```

A possible ASCII diagram for functions in JavaScript is:

```
+-----------------+       +-----------------+       +-----------------+
| Function        |       | Function        |       | Function        |
| definition      |       | call            |       | return          |
+-----------------+       +-----------------+       +-----------------+
| function square |       | var y = square( |       | return x * x;   |
| (x) {           |       | 5);             |       |                 |
|   return x * x; |       |                 |       |                 |
| }               |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
         |                         |                         |
         |                         |                         |
         +-------------------------+-------------------------+
                                   |
                                   |
                                   v
                          +-----------------+
                          | Function        |
                          | execution       |
                          +-----------------+
                          | x = 5           |
                          | y = 25          |
                          +-----------------+
```