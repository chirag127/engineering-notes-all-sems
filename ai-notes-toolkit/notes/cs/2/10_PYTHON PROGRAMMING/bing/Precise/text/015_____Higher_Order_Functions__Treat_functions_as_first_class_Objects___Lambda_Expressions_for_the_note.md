### Higher Order Functions: Treat functions as first class Objects , Lambda Expressions

In the subject of Python programming, Unit 3 covers the topic of functions. Here are some key points to remember:

- **Functions as first-class objects**: In Python, functions are considered first-class objects. This means that they can be assigned to variables, passed as arguments to other functions, and returned as values from other functions.

- **Higher-order functions**: A higher-order function is a function that takes one or more functions as arguments and/or returns a function as its result. Examples of higher-order functions in Python include `map`, `filter`, and `reduce`.

- **Lambda expressions**: Lambda expressions, also known as anonymous functions, are a way to create small, one-time-use functions in Python. They are often used as arguments to higher-order functions. Lambda expressions are defined using the `lambda` keyword, followed by a list of arguments, a colon, and an expression. For example, `lambda x: x * 2` is a lambda expression that takes a single argument `x` and returns the value of `x * 2`.

- **Parts of a function**: A function in Python consists of a `def` statement, which defines the function, followed by the function's name, a pair of parentheses containing any arguments, and a colon. The body of the function, which contains the code that will be executed when the function is called, is indented beneath the `def` statement.

- **Execution of a function**: When a function is called, the code in the body of the function is executed. The function can return a value using the `return` statement. If no `return` statement is present, the function returns `None`.

- **Keyword and default arguments**: In Python, you can specify default values for function arguments. This is done by assigning a value to the argument in the function definition, using the `=` operator. When calling the function, you can use keyword arguments to specify the values of the arguments by name.

- **Scope rules**: In Python, the scope of a variable refers to the region of the code where the variable can be accessed. Variables defined inside a function have local scope, meaning they can only be accessed within the function. Variables defined outside of a function have global scope, meaning they can be accessed from anywhere in the code.
