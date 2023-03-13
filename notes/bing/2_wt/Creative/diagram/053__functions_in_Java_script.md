A function in JavaScript is a reusable block of code that performs a specific task, taking some form of input and returning an output. A function can be defined with the function keyword, followed by a name, followed by parentheses that may include parameter names separated by commas. A function can also be assigned to a variable or a property of an object, or passed to or returned from another function. A function can have properties and methods just like any other object.

The following diagram illustrates the basic structure of a function in JavaScript:

```
+-----------------+
| function name   |  <--- function declaration
+-----------------+
| (parameter1,    |  <--- function parameters
|  parameter2,    |
|  ...)           |
+-----------------+
| {               |  <--- function body
|   // statements |  <--- function statements
|   return value; |  <--- function return value
| }               |
+-----------------+
```

The following diagram illustrates the basic usage of a function in JavaScript:

```
+-----------------+      +-----------------+
| function name   |      | variable name   |  <--- function expression
+-----------------+      +-----------------+
| (parameter1,    |      | = function      |
|  parameter2,    |      |   (parameter1,  |
|  ...)           |      |    parameter2,  |
+-----------------+      |    ...)         |
| {               |      +-----------------+
|   // statements |      | {               |
|   return value; |      |   // statements |
| }               |      |   return value; |
+-----------------+      | }               |
                         +-----------------+
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         +-----------------+
                         | object name     |  <--- function as a property
                         +-----------------+
                         | name: function  |
                         |   (parameter1,  |
                         |    parameter2,  |
                         |    ...)         |
                         +-----------------+
                         | {               |
                         |   // statements |
                         |   return value; |
                         | }               |
                         +-----------------+
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         +-----------------+
                         | function name   |  <--- function as an argument
                         +-----------------+
                         | (function       |
                         |   (parameter1,  |
                         |    parameter2,  |
                         |    ...))        |
                         +-----------------+
                         | {               |
                         |   // statements |
                         |   return value; |
                         | }               |
                         +-----------------+
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         |                 |
                         +-----------------+
                         | variable name   |  <--- function as a return value
                         +-----------------+
                         | = function      |
                         |   (parameter1,  |
                         |    parameter2,  |
                         |    ...)         |
                         +-----------------+
                         | {               |
                         |   // statements |
                         |   return        |
                         |     function    |
                         |       (parameter1,  |
                         |        parameter2,  |
                         |        ...)         |
                         | }               |
                         +-----------------+
```