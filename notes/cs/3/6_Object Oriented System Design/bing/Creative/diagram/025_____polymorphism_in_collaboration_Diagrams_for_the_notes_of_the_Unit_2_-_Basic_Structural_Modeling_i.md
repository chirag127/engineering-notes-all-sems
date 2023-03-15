### Polymorphism in Collaboration Diagrams

- Polymorphism is the ability of an object to behave differently depending on its type or class at run-time.
- In a collaboration diagram, polymorphism is represented by using multiple scenarios controlled by guard conditions.
- A guard condition is a boolean expression that determines whether a message can be sent or not.
- A scenario is a set of messages that are exchanged between objects in a specific situation.
- A scenario box is a dashed rectangle that encloses a scenario and its guard condition.
- For example, suppose we have a Shape class and three subclasses: Triangle, Rectangle, and Square. Each subclass has a show() method that displays the shape on the screen.
- In a collaboration diagram, we can represent the polymorphic invocation of show() by using three scenario boxes, one for each subclass, with the guard condition indicating the type of the object.
- The following diagram illustrates this example:

![Collaboration diagram example](https://i.stack.imgur.com/5Z1fF.png)

- In this diagram, the object s is an instance of Shape, but its actual type is determined at run-time.
- Depending on the type of s, the show() message is sent to either Triangle, Rectangle, or Square.
- The guard condition [s is Triangle] means that the message is sent only if s is an instance of Triangle, and so on for the other scenarios.
- The scenario boxes are numbered to indicate the order of execution. The first scenario that satisfies its guard condition is executed, and the rest are ignored.
- This way, the collaboration diagram can capture the dynamic behavior of polymorphism.