 Here is the content in markdown format for the topic #### Variable in Core Java:

#### Variable in Core Java

A variable is a naming convention given to a memory location to refer to the data stored in that memory location. In Core Java, there are mainly 3 types of variables:

1. Local Variables: Declared inside methods, constructors or blocks. They are created when the method is invoked and destroyed when the method is exited. For example:
int age = 25; (inside a method).

Mnemonics: Think of local variables as temporary variables that are **local** to the method and cease to exist once the method is exited.

2. Instance Variables: Declared inside a class outside of any method, constructor or block. There is only one instance of an instance variable per object. For example:
class Person {
    int age; //instance variable
}

Mnemonics: Think of instance variables as variables that are **instantiated** once per object and shared by all methods of the object.

3. Static Variables: Also declared inside a class outside of any method, constructor or block. There is only one static variable per class, shared by all instances (objects) of the class. For example:
class Person {
    static int count; //static variable
}

Mnemonics: Think of static variables as variables that are shared by all **static** members of the class, i.e. the variable is associated with the class itself rather than with any object instance.

Some key points and examples regarding variables in Core Java are as follows:

- Variables must be declared before use.
- Variables are assigned values using = operator.
- Valid names for variables - alphanumeric, underscore, dollar sign, should not start with a number.
- Variable names are case-sensitive.
- Local variables must be assigned a value before use.
- Instance and static variables are initialized to default values (0, false, null) if not assigned.
- Variables can be reassigned new values.
- final variables cannot be reassigned values.
- etc.

[You can include diagrams, codes, tables, advantages, disadvantages, applications, etc here if helpful]