 Here is the content in markdown format without any emojis or external links as per your instructions:

### Factory Methods for the notes of the Unit 3 - Scripting in the subject of Web Technology

1. Factory methods are creational design patterns which provide an interface for creating objects in a superclass, but allow subclasses to alter the type of objects that will be created.

2. They are used when you don't know ahead of time the exact types and dependencies of the objects your code needs.

3. Common benefits of factory methods are:
- Using interfaces allows you to decouple the creation of objects from their usage.
- Allows you to encapsulate object creation, giving you more control over the process.
- Increased flexibility, you can introduce new types in the future without breaking existing code.
- Contains object creation code in one place, making your code easier to maintain.

4. Some common examples of factory methods are:
- DocumentBuilderFactory from the Java XML API to create DocumentBuilder instances.
- SocketFactory to create socket instances.
- Calendar#getInstance() to create Calendar instances.

5. To implement a factory method:
- Define an interface for creating an object.
- Create a class with a factory method that returns an object implementing the interface.
- The implementing class can be the factory class itself or a separate subclass.
- The client calls the factory method to create instances, rather than using the constructor.

I hope this helps! Let me know if you would like me to modify or expand the content in any way.