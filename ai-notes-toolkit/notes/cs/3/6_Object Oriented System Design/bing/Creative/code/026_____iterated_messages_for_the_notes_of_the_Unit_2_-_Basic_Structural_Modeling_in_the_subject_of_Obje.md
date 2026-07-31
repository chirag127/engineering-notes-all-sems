### Iterated Messages

- Iterated messages are a way of representing repeated messages in an interaction diagram.
- An iterated message is a message that is sent to multiple objects in a collection, such as an array, a list, or a set.
- An iterated message is denoted by an asterisk (*) in front of the message name, followed by an optional iteration expression in square brackets.
- The iteration expression specifies the condition or range for selecting the objects from the collection.
- For example, `*print[1..3]` means that the message `print` is sent to the first three objects in the collection.
- Iterated messages can be used to simplify the interaction diagram by avoiding the need to show individual messages to each object in the collection.
- Iterated messages can also be used to model the iterator pattern, which is a design pattern that allows sequential access to the elements of a container without exposing its internal structure.
- The iterator pattern involves two types of objects: an iterator and an iterable.
- An iterator is an object that provides a method to get the next element from the container.
- An iterable is an object that provides a method to create an iterator for the container.
- For example, `*next()` means that the message `next()` is sent to the iterator object to get the next element from the container.
- Iterated messages are related to the concept of iterative design, which is a design methodology based on a cyclic process of prototyping, testing, analyzing, and refining a product or process.
- Iterative design aims to improve the quality and functionality of a design by incorporating feedback from users and stakeholders.
- Iterative design is often used in conjunction with incremental development, which is a development approach that delivers a product or process in small, usable pieces.
- Incremental development allows for early testing and validation of the product or process, as well as easier integration and maintenance.
- Iterative design and incremental development are common practices in object-oriented system design, which is a design paradigm that focuses on modeling the system as a collection of interacting objects that encapsulate data and behavior.
- Object-oriented system design aims to achieve modularity, reusability, extensibility, and abstraction in the system.