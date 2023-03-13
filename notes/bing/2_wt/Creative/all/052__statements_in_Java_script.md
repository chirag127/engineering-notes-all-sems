#### Statements in JavaScript

- A statement is a syntactic unit of code that expresses an action to be carried out.
- A program is a sequence of statements.
- Each statement is terminated by a semicolon (;) that marks the end of the statement.
- There are different types of statements in JavaScript, such as:

  - Declaration statements: These statements declare variables, functions, classes, or modules. For example:

    ```javascript
    var x = 10; // declares a variable named x and assigns it the value 10
    function add(a, b) { // declares a function named add that takes two parameters
      return a + b; // returns the sum of a and b
    }
    class Person { // declares a class named Person
      constructor(name, age) { // defines a constructor method for the class
        this.name = name; // assigns the name property to the instance
        this.age = age; // assigns the age property to the instance
      }
    }
    import { sqrt } from 'math'; // declares a module named math and imports the sqrt function from it
    ```

  - Expression statements: These statements evaluate an expression and return its value. For example:

    ```javascript
    x + y; // evaluates the expression x + y and returns its value
    console.log('Hello'); // evaluates the expression console.log('Hello') and returns its value (undefined)
    3 * (4 + 5); // evaluates the expression 3 * (4 + 5) and returns its value (27)
    ```

  - Control flow statements: These statements alter the execution flow of the program based on some conditions. For example:

    ```javascript
    if (x > 10) { // executes the block of code if the condition x > 10 is true
      console.log('x is greater than 10');
    } else { // executes the block of code if the condition x > 10 is false
      console.log('x is less than or equal to 10');
    }

    switch (color) { // executes the block of code that matches the value of color
      case 'red':
        console.log('The color is red');
        break; // exits the switch statement
      case 'blue':
        console.log('The color is blue');
        break; // exits the switch statement
      default:
        console.log('The color is unknown');
        break; // exits the switch statement
    }

    for (let i = 0; i < 10; i++) { // executes the block of code 10 times, with i ranging from 0 to 9
      console.log(i);
    }

    while (x < 100) { // executes the block of code as long as the condition x < 100 is true
      x = x * 2;
    }

    do { // executes the block of code at least once, and then repeats as long as the condition x > 0 is true
      x = x - 1;
    } while (x > 0);
    ```

  - Iteration statements: These statements iterate over an iterable object (such as an array, a string, a map, a set, etc.) and execute a block of code for each element. For example:

    ```javascript
    for (let item of array) { // executes the block of code for each item in the array
      console.log(item);
    }

    for (let key in object) { // executes the block of code for each key in the object
      console.log(key, object[key]);
    }
    ```

  - Exception handling statements: These statements handle errors or exceptions that may occur during the execution of the program. For example:

    ```javascript
    try { // tries to execute the block of code
      let result = sqrt(-1); // throws an error because the argument is negative
    } catch (error) { // catches the error and executes the block of code
      console.error(error.message); // logs the error message
    } finally { // executes the block of code regardless of whether an error occurred or not
      console.log('Done');
    }
    ```

  - Miscellaneous statements: These statements perform other actions that do not fit in the above categories. For example:

    ```javascript
    break; // exits the current loop or switch statement
    continue; // skips the current iteration of the loop and continues with the next one
    return; // returns a value from a function and exits the function
    throw; // throws an error or exception
    debugger; // invokes the debugger (if available) and pauses the execution of the program
    ```