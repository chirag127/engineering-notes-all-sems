 Here is the content in markdown format for the topic ### Factory Methods for the notes of the Unit 3 - Scripting in the subject of Web Technology:

### Factory Methods

Factory Methods are methods that create and return objects. They are used to:

-   Decide which class to instantiate at runtime.
-   Hide the creation logic from the client.
-   Refer to newly created objects using a common interface.

Advantages:

-   It provides a generic interface for creating objects. The client code does not need to know which concrete class is actually instantiated.
-   It promotes loose coupling as the client code is not dependent on concrete classes.
-   Single Responsibility Principle is followed as object creation is the sole responsibility of the factory method.

Disadvantages:

-   The code can become more complicated as more factory methods are added.
-   It can be overused leading to unnecessary complexity.

Examples:

-   The DocumentBuilderFactory class in JAXP creates DocumentBuilder objects needed to parse XML documents.
-   The NumberFormat class's getInstance() method which gets a NumberFormat for a specific locale.
-   The Calendar class's getInstance() method which gets a Calendar for a specific time zone and locale.

Applications:

-   When the classes to instantiate are specified at run-time.
-   To avoid building a class hierarchy of factories that parallels the class hierarchy of products.
-   When instances of a class cannot be created directly due to some restrictions.

Notes:

-   Factory Methods are a creational pattern.
-   They return a product object.
-   The product classes and concrete factories are decoupled from each other.
-   Products of a factory method are usually related by a common interface.