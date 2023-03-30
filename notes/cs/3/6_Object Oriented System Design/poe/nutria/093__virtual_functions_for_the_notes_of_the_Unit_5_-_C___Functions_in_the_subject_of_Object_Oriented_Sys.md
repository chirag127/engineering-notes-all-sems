
### Virtual Functions
Virtual functions are a key concept in Object Oriented System Design. They allow derived classes to override the behavior of a base class, while still providing access to the base class's implementation.

* A virtual function is declared in the base class with the keyword `virtual`.
* The function is then overridden in the derived class.
* The overridden function is called instead of the base class's implementation when a pointer or reference to the derived class is used.
* Virtual functions can be used to create a polymorphic interface, allowing derived classes to be used interchangeably.
* Virtual functions can also be used to provide a default implementation of a function that can be overridden in derived classes.