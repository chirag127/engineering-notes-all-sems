### Polymorphism in Collaboration Diagrams

- Polymorphism is the ability of an object to behave differently depending on its type or class at run-time.
- In collaboration diagrams, polymorphism is represented by using multiple scenarios controlled by guard conditions.
- Guard conditions are expressions that evaluate to true or false and determine which scenario is executed.
- Each scenario shows the messages that are sent to the polymorphic object and the responses that are returned.
- The polymorphic object is usually shown as an abstract class or an interface, and the concrete subclasses are shown as instances of that class or interface.
- For example, consider a polymorphic object of type Shape that can be an instance of Triangle, Rectangle or Square at run-time. The object can receive a message show() that displays the shape on the screen. The collaboration diagram below shows how polymorphism is represented in this case.

![Collaboration diagram example](https://i.stack.imgur.com/3qZ9U.png)

- The guard conditions [Triangle], [Rectangle] and [Square] indicate which scenario is executed depending on the type of the Shape object.
- The messages show() are sent to the Shape object, which delegates them to the appropriate subclass object.
- The responses are returned from the subclass object to the Shape object, and then to the sender object.