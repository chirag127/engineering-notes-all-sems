 Here is the content in markdown format:

### Mapping object oriented concepts using non-object oriented language

Object Oriented Analysis involves analyzing the problem domain in terms of objects and the interactions between those objects. However, not all programming languages support Object Oriented concepts directly. We can map the core Object Oriented concepts to non-Object Oriented languages as follows:

1. Objects -> Records/Structures: We can model objects as records/structures containing data and functions operating on that data. The functions can act as methods of the object.
2. Classes -> Types: We can model classes as types defining a common structure for multiple records/structures. The types can contain common data and functions which are shared by all instances/records of that type.
3. Inheritance -> Subtyping: The IS-A relationship between classes can be modeled as a subtyping relationship between types. The subtypes inherit and extend the supertypes.
4. Encapsulation -> Information hiding: We can hide the internal details of records/structures and expose only selective functions to encapsulate data and enforce invariants.
5. Polymorphism -> Function overloading: We can overload functions based on the type of the arguments to achieve polymorphic behavior using common interfaces for different types.

The above mappings can enable us to apply core Object Oriented analysis techniques even using non-Object Oriented languages. However, the implementations may not be as clean/efficient as true Object Oriented languages providing first-class support for Object Oriented concepts. The mappings can be useful as a tactical solution but for strategic, long-term applications, it is better to use Object Oriented languages.