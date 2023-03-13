 Here is the content in markdown format for the topic #### Exception Handling in Core Java:

#### Exception Handling in Core Java

- Exceptions are anomalies that arise during program execution and disrupt the normal flow of the program.
- Exception handling is a mechanism to handle exceptions/errors in order to continue the execution of the program.
- The `try-catch-finally` block is used for exception handling in Java.
- The `try` block contains code that may throw an exception.
- The `catch` block contains code to handle the exception if it occurs in the try block.
- The `finally` block contains code that will always be executed whether an exception occurs or not.
- Mnemonic: `Try` to `Catch` any `Exception` and do something `Finally`.
- Key benefits of exception handling:
	- Allows the program to continue execution even after the occurrence of an exception.
	- Provides the capability to gracefully recover from exceptional conditions.
	- Separates the normal flow of the program from the error handling flow.
- The `Throwable` class is the superclass of all exceptions and errors in Java.
- Checked exceptions: Must be handled or declared. E.g. IOException.
- Unchecked exceptions: Do not need to be handled or declared. E.g. NullPointerException.
- Errors: Denote serious problems that a reasonable application should not try to catch. E.g. OutOfMemoryError.
- Best practices:
	- Use try-catch-finally judiciously.
	- Be specific while catching exceptions. Catch the most specific exception possible.
	- Do not swallow important exceptions.
	- Throw meaningful exceptions.
	- Maintain clean exception hierarchies.

[Detailed diagrams, code examples and additional points can be added here if required.]