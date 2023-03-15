Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are some notes on the topic of functions for Unit 3 - Scripting.

### Functions

- A function is a block of code that performs a specific task and can be reused in a program.
- A function can have zero or more parameters that are passed as input values and can return zero or more values as output.
- A function can be defined using the `function` keyword followed by the function name and a list of parameters in parentheses.
- A function can be called by using the function name followed by a list of arguments in parentheses that match the parameters of the function.
- A function can be declared before or after the code that calls it, as long as the function is in the same scope as the caller.
- A function can be assigned to a variable or passed as an argument to another function, as functions are first-class objects in JavaScript.
- A function can be anonymous, meaning it does not have a name, and can be used as an expression or a callback.
- A function can be nested inside another function, creating a closure that can access the variables and parameters of the outer function.
- A function can use the `return` statement to end the execution of the function and return a value to the caller.
- A function can use the `this` keyword to refer to the object that invoked the function, or the global object if the function is not bound to any object.
- A function can use the `arguments` object to access all the arguments passed to the function, regardless of the number and names of the parameters.

Here is an example of a function that calculates the area of a circle:

```javascript
// Define a function named areaOfCircle that takes one parameter named radius
function areaOfCircle(radius) {
  // Calculate the area using the formula pi * radius * radius
  var area = Math.PI * radius * radius;
  // Return the area value
  return area;
}

// Call the function with different arguments and print the results
console.log(areaOfCircle(5)); // 78.53981633974483
console.log(areaOfCircle(10)); // 314.1592653589793
console.log(areaOfCircle(2.5)); // 19.634954084936208
```
