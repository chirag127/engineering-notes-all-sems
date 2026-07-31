### Iterated messages for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- Iterated messages are a way of representing repeated communication between objects in an interaction diagram.
- An iterated message is shown as a message with an asterisk (*) in front of it, indicating that it is sent to multiple objects in a collection.
- An iterated message can have a guard condition, which is a boolean expression that specifies which objects in the collection receive the message.
- An example of an iterated message is shown below, where the `*` indicates that the `print()` message is sent to all the `Document` objects in the `documents` collection, and the `[type = "pdf"]` indicates that only the `Document` objects with the `type` attribute equal to `"pdf"` receive the message.

![Iterated message example](https://www.guru99.com/images/1/022518_0618_Interactio2.png)

- Iterated messages are useful for modeling scenarios where an object needs to perform an action on multiple other objects, such as iterating over a collection, filtering a list, or applying a function.
- Iterated messages are different from iterator patterns, which are a design pattern that decouples algorithms from containers and allows sequential access to the elements of a container.
- Iterated messages are also different from iterative design, which is a design methodology that involves a cyclic process of prototyping, testing, analyzing, and refining a product or process.
- Iterated messages are related to object oriented design, which is a design paradigm that focuses on modeling the state, behavior, and identity of objects and their interactions.
- Iterated messages are one of the many concepts that are covered in the unit 2 of the subject of object oriented system design, which aims to teach the principles and techniques of designing software systems using object oriented approach.