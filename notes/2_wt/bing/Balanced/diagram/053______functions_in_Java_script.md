A function in JavaScript is a reusable block of code that performs a specific task, taking some form of input and returning an output. A function can be defined with the function keyword, followed by a name, followed by parentheses that may include parameter names separated by commas. A function can also be assigned to a variable or a property, or passed to or returned from another function. A function can be called by using its name followed by parentheses that may include arguments that match the parameters.

Here is a possible ASCII diagram for functions in JavaScript:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Function      |     |  Function      |     |  Function      |
|  declaration   |     |  expression    |     |  call          |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  function foo  |     |  var foo =     |     |  foo(1, 2);    |
|  (a, b) {      |     |  function (a,  |     |                |
|    return a+b; |     |  b) {          |     |                |
|  }             |     |    return a+b; |     |                |
|                |     |  };            |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +---------------------->                      |
       |                      |                      |
       |                      +----------------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +--------------------------------------------->

```

The diagram shows three ways of creating and using a function named foo that takes two parameters a and b and returns their sum. The first way is to declare the function with the function keyword and a name. The second way is to assign a function expression to a variable with the same name. The third way is to call the function by using its name and passing two arguments that match the parameters. The arrows show the flow of execution and the relationship between the function declaration, expression, and call.