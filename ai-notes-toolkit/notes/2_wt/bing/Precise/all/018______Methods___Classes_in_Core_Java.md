#### Methods & Classes in Core Java

- **Methods** in Java are blocks of code that perform a specific task and can be called by other parts of the program. They are used to organize code and improve code reusability.
- **Classes** in Java are blueprints for creating objects. They define the properties and behaviors of objects through fields and methods.
- A **method** is defined within a class and has a method signature that includes its name, return type, and parameters.
- To call a method, you need to use the dot notation, for example: `objectName.methodName(parameters)`.
- Methods can have different **access modifiers** such as `public`, `private`, `protected`, and `default` (no modifier), which determine the visibility of the method to other classes.
- Methods can also be **static**, which means they belong to the class rather than an instance of the class. Static methods can be called without creating an object of the class, for example: `ClassName.methodName(parameters)`.
- A **constructor** is a special type of method that is called when an object is created. It has the same name as the class and is used to initialize the fields of the object.
- A class can have multiple constructors with different parameters, which is known as **constructor overloading**.
- A class can also have **inner classes**, which are classes defined within another class. Inner classes can access the fields and methods of the outer class.
- A class can **inherit** from another class, which means it can use the fields and methods of the parent class. This is known as **inheritance** and is achieved using the `extends` keyword.
- A class can also **implement** one or more interfaces, which means it must provide implementations for all the methods defined in the interface. This is known as **interface implementation** and is achieved using the `implements` keyword.
- A **final** class cannot be inherited from, and a **final** method cannot be overridden in a subclass.
- An **abstract** class is a class that cannot be instantiated and is used as a base class for other classes. It can have abstract methods, which are methods without a body that must be implemented by subclasses.
- A **static nested class** is a static class defined within another class. It can be accessed without creating an instance of the outer class.
- A **local class** is a class defined within a method. It can only be accessed within the method where it is defined.