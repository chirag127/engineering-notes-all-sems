## Unit 6 - Creating Procedures and Functions

Procedures and functions are subprograms that are used to modularize and organize code. They allow for code reuse and make it easier to maintain and update code.

1. **Procedures** are subprograms that perform a specific task and do not return a value. They are called using the `CALL` statement or by simply using their name followed by any required parameters in parentheses.

2. **Functions** are subprograms that perform a specific task and return a value. They are called by using their name followed by any required parameters in parentheses, and the returned value can be assigned to a variable or used in an expression.

3. Both procedures and functions can have parameters, which are values passed to the subprogram when it is called. Parameters can be passed by value, where a copy of the value is passed to the subprogram, or by reference, where a reference to the original value is passed to the subprogram.

4. Procedures and functions can be created using the `CREATE PROCEDURE` and `CREATE FUNCTION` statements, respectively. The body of the subprogram is defined using the `BEGIN` and `END` keywords, and any parameters are defined in the parentheses following the subprogram name.

5. Procedures and functions can be called from other subprograms or from the main program. They can also be called recursively, where a subprogram calls itself.

6. It is important to properly design and use procedures and functions to improve the readability, maintainability, and reusability of code. They should have a clear purpose and be well-documented.