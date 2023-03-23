 Here are the notes on the topic "Passing arguments to methods" for Unit 3 - Object Oriented Analysis in Object Oriented System Design:

### Passing arguments to methods

1. Method arguments allow us to pass input to methods. This input can be in the form of values or variables.
2. Arguments can be passed to methods in two ways:
- By value: The method gets a copy of the argument's value. Changing the value inside the method does not affect the original variable passed.
- By reference: The method gets access to the original variable itself. Changing the variable inside the method affects the original variable passed.
3. In Java, primitive types like int, char, etc. are passed by value while objects are passed by reference.
4. The type of arguments passed should match the parameter types of the method in terms of both data type and number of arguments. Otherwise, compile time errors occur.
5. Default values are used for arguments if no values are passed while calling the method. For objects, the default value is null. For primitives, default values are 0 or false.
6. Variable number of arguments can be handled using varargs. The type of varargs parameter is always an array.

The notes are written in a formal tone with points and omitting emojis or external links as instructed. The content is written using Markdown formatting within headers. Please let me know if any changes are required.