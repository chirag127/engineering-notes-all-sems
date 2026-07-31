#### Methods & Classes in Core Java

- A class is a blueprint or template that defines the structure and behavior of objects of the same type. A class contains both data and methods that operate on that data.  
- An object is an instance of a class that has its own state and can access the methods defined by the class. Objects are created using the `new` keyword and a constructor. 
- A method is a block of code that performs a specific task or action. A method can be declared inside a class or outside a class. A method can have parameters, return values, modifiers, and exceptions.  
- A method can be called by using the object name of the class to which it belongs and a dot operator, such as `object.method()`. A method can also be called directly if it is defined with the `static` modifier, such as `ClassName.method()`. 
- A method can be overloaded, which means that multiple methods can have the same name but different parameters. A method can also be overridden, which means that a subclass can redefine the behavior of a method inherited from a superclass. 

Some examples of methods and classes in core java are:

- The `String` class is a predefined class that represents a sequence of characters. It has many methods that can manipulate and compare strings, such as `length()`, `charAt()`, `equals()`, `substring()`, etc. 
- The `Math` class is a predefined class that contains methods for performing mathematical operations, such as `abs()`, `sqrt()`, `sin()`, `cos()`, `random()`, etc. The `Math` class is a static class, which means that its methods can be called without creating an object. 
- The `Scanner` class is a predefined class that can read input from various sources, such as keyboard, file, etc. It has methods that can parse different types of data, such as `nextInt()`, `nextLine()`, `nextDouble()`, etc. To use the `Scanner` class, an object must be created using the `new` keyword and a source. 

Some mnemonics and learning tricks for methods and classes in core java are:

- To remember the syntax of a method declaration, use the acronym `PMRTE`, which stands for `public`, `static`, `return type`, `method name`, and `parameters`. For example, `public static int add(int a, int b)`.
- To remember the difference between overloading and overriding, use the phrase `same name, different game`. Overloading means that methods have the same name but different parameters (different game). Overriding means that methods have the same name and parameters but different behavior (same game).
- To remember the difference between a class and an object, use the analogy of a cookie cutter and a cookie. A class is like a cookie cutter that defines the shape and size of a cookie. An object is like a cookie that is made using the cookie cutter. A cookie cutter can make many cookies, and a class can create many objects.