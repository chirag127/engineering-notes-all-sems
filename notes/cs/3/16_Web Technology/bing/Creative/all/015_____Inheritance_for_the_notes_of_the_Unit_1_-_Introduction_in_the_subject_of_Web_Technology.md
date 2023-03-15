# Inheritance

- Inheritance is a concept in object-oriented programming that allows one class to inherit the properties and methods of another class.
- Inheritance enables code reuse and polymorphism, which means that the same code can behave differently depending on the context.
- Inheritance is implemented using the `extends` keyword in Java, the `:` operator in C++, and the `class` statement in Python.
- The class that inherits from another class is called the **subclass** or the **child class**. The class that is inherited from is called the **superclass** or the **parent class**.
- A subclass can override the methods of its superclass by defining a method with the same name and signature. This allows the subclass to provide a more specific or different behavior than the superclass.
- A subclass can also access the fields and methods of its superclass using the `super` keyword in Java, the `::` operator in C++, and the `super()` function in Python.
- A subclass can inherit from multiple superclasses in some languages, such as Python and C++. This is called **multiple inheritance**. However, multiple inheritance can cause ambiguity and complexity, so some languages, such as Java, do not support it.
- A subclass can also inherit from an **interface**, which is a collection of abstract methods that define a contract or a behavior. An interface does not provide any implementation for the methods, so the subclass must implement them. A subclass can inherit from multiple interfaces in Java, C++, and Python. This is called **interface inheritance** or **implementation inheritance**.