### Polymorphism in Collaboration Diagrams

- Polymorphism is the ability of an object to behave differently depending on its type or context.
- In collaboration diagrams, polymorphism is represented by using multiple scenarios controlled by guard conditions.
- Guard conditions are expressions that evaluate to true or false and determine which scenario is executed.
- Each scenario shows the messages sent to and from the polymorphic object and the corresponding actions performed by the object.
- The polymorphic object is usually shown as an abstract class or an interface with a stereotype of <<polymorphic>>.
- An example of a collaboration diagram with polymorphism is shown below:

![Collaboration diagram with polymorphism](https://i.stack.imgur.com/8o6Zs.png)

- In this diagram, the object s of type Shape can be an instance of Triangle, Rectangle or Square at run-time.
- The guard conditions [s is Triangle], [s is Rectangle] and [s is Square] determine which scenario is executed when the message show() is sent to s.
- Each scenario shows the different actions performed by s depending on its type, such as drawing a triangle, a rectangle or a square.