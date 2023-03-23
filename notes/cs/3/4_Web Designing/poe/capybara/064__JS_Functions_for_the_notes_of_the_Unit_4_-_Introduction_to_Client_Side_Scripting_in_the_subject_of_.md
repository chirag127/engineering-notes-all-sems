### JS Functions for the notes of the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing

In this unit, we will cover the basics of JavaScript functions. Functions are blocks of code that can be called repeatedly to perform a specific task. They are one of the most important concepts in JavaScript and are widely used in web development.

Here are some important points to keep in mind when working with JavaScript functions:

- **Creating a function:** To create a function, you need to use the `function` keyword, followed by the name of the function and the parameters it accepts. For example:

  ```
  function greet(name) {
      console.log("Hello, " + name + "!");
  }
  ```

- **Calling a function:** To call a function, you simply need to use its name followed by the arguments it requires (if any). For example:

  ```
  greet("John");
  ```

- **Returning a value:** Functions can also return a value using the `return` keyword. For example:

  ```
  function add(a, b) {
      return a + b;
  }
  ```

- **Anonymous functions:** Anonymous functions are functions without a name. They are often used as callbacks or as arguments to other functions. For example:

  ```
  setTimeout(function() {
      console.log("Hello from anonymous function!");
  }, 1000);
  ```

- **Function scope:** Functions have their own scope, which means that variables declared inside a function are not accessible outside of it. For example:

  ```
  function myFunction() {
      var x = 10;
  }
  
  console.log(x); // This will throw an error
  ```

- **Function parameters:** Functions can accept any number of parameters, which are passed as arguments when the function is called. For example:

  ```
  function multiply(a, b, c) {
      return a * b * c;
  }
  
  multiply(2, 3, 4); // Returns 24
  ```

By understanding these key concepts, you will be able to create and use functions effectively in your JavaScript code.