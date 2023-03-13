Exception handling in Java is a mechanism to handle the runtime errors and maintain the normal flow of the application. An exception is an abnormal condition that occurs when a program violates the semantic constraints of the Java language. There are two types of exceptions in Java: checked and unchecked. Checked exceptions are those that are checked by the compiler at compile time and must be handled by the programmer using the try-catch-finally blocks or the throws keyword. Unchecked exceptions are those that are not checked by the compiler and are usually caused by logic errors or bugs in the code. They are also known as runtime exceptions.

The following diagram illustrates the basic architecture of exception handling in Java using ASCII characters:

#### Exception Handling in Core Java

```
+-----------------+       +-----------------+       +-----------------+
|  try block     |       |  catch block    |       |  finally block  |
|  Normal code   |       |  Exception      |       |  Cleanup code   |
|  that may      |       |  handling code  |       |  that executes  |
|  throw an      |       |  for a specific |       |  regardless of  |
|  exception     |       |  type of        |       |  exception      |
|                |       |  exception      |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                |       |                 |       |                 |
|                |       |                 |       |                 |
|                |       |                 |       |                 |
|                |       |                 |       |                 |
|                |       |                 |       |                 |
|                |       |                 |       |                 |
|                |       |                 |       |                 |
|                |       |                 |       |                 |
|                |       |                 |       |                 |
|                |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                |       |                 |       |                 |
|                |       |                 |       |                 |
|                |       |                 |       |                 |
|                |       |                 |       |                 |
|                |       |                 |       |                 |
|                |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|  throws        |       |  throw          |       |                 |
|  Keyword to    |       |  Keyword to     |       |                 |
|  declare the   |       |  create and     |       |                 |
|  exceptions    |       |  throw an       |       |                 |
|  that a method |       |  exception      |       |                 |
|  may throw     |       |  object         |       |                 |
|                |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```