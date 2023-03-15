#### Variable in Core Java

- A variable in Java is a data container that stores the data values during Java program execution  .
- A variable is a name given to a memory location. It is the basic unit of storage in a program.
- Every variable is assigned a data type that designates the type and quantity of value it can hold  .
- Variables in Java can be defined anywhere in the code (inside a class, inside a method, or as a method argument) and can have different modifiers.
- Depending on these conditions, variables in Java can be divided into four categories:
  - Instance Variable: A variable that is declared inside a class but outside a method. It is also called a non-static variable. It is initialized when an object of the class is created and can be accessed by the object reference  .
  - Static Variable: A variable that is declared inside a class but outside a method with the static keyword. It is also called a class variable. It is initialized when the class is loaded and can be accessed by the class name  .
  - Local Variable: A variable that is declared inside a method or a block. It is also called a method variable. It is initialized when the method is invoked and can be accessed only within the method or the block  .
  - Parameter Variable: A variable that is declared as a method argument. It is also called a formal parameter. It is initialized when the method is called and can be accessed only within the method .
- Variables in Java follow some naming conventions and rules :
  - Variable names are case-sensitive, meaning that upper and lower case letters are treated as different.
  - Variable names must start with a letter (a-z or A-Z), an underscore (_) or a dollar sign ($), but not with a digit (0-9).
  - Variable names can contain any combination of letters, digits, underscores and dollar signs, but not any other special characters or spaces.
  - Variable names should not be Java keywords or reserved words, such as int, class, public, etc.
  - Variable names should be descriptive and meaningful, following the camelCase convention for instance and local variables, and the UPPER_CASE convention for static variables.