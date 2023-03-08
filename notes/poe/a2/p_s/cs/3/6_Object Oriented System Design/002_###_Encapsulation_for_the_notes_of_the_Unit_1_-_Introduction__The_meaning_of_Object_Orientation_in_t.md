 Here is the content in markdown format:

### Encapsulation

Encapsulation refers to the bundling of data with the methods that operate on that data, or the restricting of direct access to some of an object's components. The purpose of encapsulation is to hide the values or state of a structured data object inside a class, preventing unauthorized parties' direct access to them. Only the object's own methods are allowed to access and modify its fields, using access modifiers.

- **Access modifiers**: In encapsulation, the variables of a class can have access modifiers to control the access level. The three main access modifiers are:
- **Public**: The variables and methods can be accessed from anywhere.
- **Private**: The variables and methods can be accessed only within the class.
- **Protected**: The variables and methods can be accessed only within the class and by subclasses.

Encapsulation promotes reusability, modularity and maintainability. Since the inner workings of objects are hidden from the outside, the code using those objects does not depend on the objects' inner structure. This isolation makes it possible to change and refine the implementation details of objects without affecting the code that uses them.

Advantages:
- The users of a class do not know how the class stores its data. A class can change the data type of a field and users of the class do not need to change any of their code.
- A class can have methods to protect its data (encapsulation) and hide its implementation details.
- The users of a class can easily understand its interface (data and method signatures) without knowing its inner workings.
- The encapsulation provides greater security as only important data is exposed to users.

Examples:
- A car has an engine - the users know how to start, stop and accelerate the car without knowing the specific workings of the engine.
- A television has channels and volume controls - we know how to operate them but not how it works internally.

Applications: Encapsulation is used everywhere in programming to hide unnecessary details and build modular programs. It is a fundamental concept of object-oriented programming languages like Java, C++, Python, etc.