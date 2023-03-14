#### Methods & Classes in Core Java

- A method is a block of code that performs a specific task. A method can be invoked (called) by another method, by creating an object, or directly from a class.
- A class is a blueprint for creating objects. A class defines the properties (attributes) and behaviors (methods) of its objects.
- A class can have one or more constructors, which are special methods that are used to initialize the objects of the class.
- A class can also have one or more fields, which are variables that store the state of the objects of the class.
- A class can implement one or more interfaces, which are contracts that specify what methods a class must provide.
- A class can extend another class, which means it inherits all the fields and methods of the parent class, and can also add its own fields and methods.
- A class can be abstract, which means it cannot be instantiated, but can be used as a superclass for other classes.
- A class can be final, which means it cannot be extended by other classes.
- A class can have one or more inner classes, which are classes defined inside another class. Inner classes can access the fields and methods of the outer class, and can also have their own fields and methods.
- A class can have one or more static members, which are fields and methods that belong to the class itself, not to any object of the class. Static members can be accessed without creating an object of the class.

Some examples of methods and classes in core Java are:

- The `Math` class is a final class that provides various mathematical methods and constants, such as `Math.sqrt()`, `Math.PI`, etc. The `Math` class has only static members, so they can be used directly without creating an object of the class.
- The `String` class is a final class that represents a sequence of characters. The `String` class has many methods that manipulate and compare strings, such as `String.length()`, `String.equals()`, etc. The `String` class also has a constructor that takes a character array as an argument and creates a string object from it.
- The `Scanner` class is a class that provides methods for reading input from various sources, such as keyboard, file, etc. The `Scanner` class has a constructor that takes an input stream as an argument and creates a scanner object that can read from it. The `Scanner` class has methods such as `Scanner.nextInt()`, `Scanner.nextLine()`, etc. that read different types of data from the input stream.
- The `System` class is a final class that provides access to system resources and properties, such as standard input, output, and error streams, system time, environment variables, etc. The `System` class has only static members, so they can be used directly without creating an object of the class. Some of the methods of the `System` class are `System.out.println()`, `System.currentTimeMillis()`, `System.getenv()`, etc.