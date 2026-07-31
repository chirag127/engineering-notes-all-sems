## Unit 6 - Objects and Classes

- An object is a software entity that combines data and behavior.
- A class is a blueprint or template for creating objects of a certain type.
- A class defines the properties (attributes) and methods (operations) of the objects that belong to it.
- An object is an instance of a class, meaning it is a specific realization of the general template.
- To create an object of a class, we use the `new` operator followed by the class name and a pair of parentheses.
- To access the properties or methods of an object, we use the dot notation (`.`) followed by the property or method name.
- For example, if `circle` is an object of the `Circle` class, we can write `circle.radius` to access its radius property, or `circle.area()` to invoke its area method.
- A constructor is a special method that is used to initialize an object when it is created.
- A constructor has the same name as the class and no return type.
- A constructor can have parameters to specify the initial values of the object's properties.
- For example, the `Circle` class can have a constructor that takes a parameter `r` and assigns it to the `radius` property of the object.
- A default constructor is a constructor that takes no parameters and provides default values for the object's properties.
- If a class does not define any constructors, the compiler will automatically provide a default constructor that does nothing.
- A class can have more than one constructor, as long as they have different parameter lists. This is called constructor overloading.
- A class can also have static properties and methods, which belong to the class itself and not to any specific object.
- Static properties and methods are accessed using the class name and the dot notation, without creating an object of the class.
- For example, the `Math` class has static properties like `Math.PI` and static methods like `Math.sqrt()`.
- Static properties and methods are useful for defining constants and utility functions that are related to the class but do not depend on any object state.