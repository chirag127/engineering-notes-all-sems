# Polymorphism in Collaboration Diagrams

- Polymorphism is the ability of an object to behave differently depending on its type or context.
- In collaboration diagrams, polymorphism is represented by using multiple scenarios controlled by guard conditions.
- Guard conditions are expressions that evaluate to true or false and determine which scenario is executed.
- Each scenario shows the messages that are sent to the object based on its type or state.
- For example, suppose we have a Shape class and three subclasses: Triangle, Rectangle and Square.
- We want to send the message show() to a Shape object, but the behavior of show() depends on the type of the object at run-time.
- We can use a collaboration diagram to model this polymorphic behavior as follows:

![Polymorphism in Collaboration Diagram](https://i.stack.imgur.com/7n0cX.png)

- The diagram shows four scenarios: one for each type of Shape and one for the default case.
- Each scenario has a guard condition that specifies the type of the object.
- The messages that are sent to the object are shown inside the scenario box.
- For example, in the scenario where the object is a Triangle, the message show() is sent to the object, which then calls the methods draw() and fill() on itself.
- In the default scenario, the message show() is sent to the object, which then calls the method error() on itself.