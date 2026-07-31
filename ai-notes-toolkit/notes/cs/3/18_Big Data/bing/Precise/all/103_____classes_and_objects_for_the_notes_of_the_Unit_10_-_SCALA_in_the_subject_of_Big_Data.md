### Unit 10 - SCALA: Classes and Objects

- **Classes** in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members.
- A **class** is defined using the `class` keyword, followed by the class name and a parameter list.
- The body of the class is defined in curly braces `{}` and can contain class members.
- An **object** is an instance of a class, created using the `new` keyword followed by the class name and any necessary constructor arguments.
- Objects can access the members of their class.
- Scala also has a concept of **singleton objects**, defined using the `object` keyword. A singleton object is an object that is the only instance of its class.
- Singleton objects are often used to hold methods and values that are not associated with instances of a class.
- Companion objects are singleton objects that share the same name and are defined in the same source file as a class. They can access private members of the class and are often used to hold factory methods for creating instances of the class.
