# Polymorphism in Collaboration Diagrams

- Polymorphism is the ability of an object to behave differently depending on its type or context.
- In collaboration diagrams, polymorphism is represented by using multiple scenarios controlled by guard conditions.
- Guard conditions are expressions that evaluate to true or false and determine which scenario is executed.
- Each scenario shows the messages that are sent to the object based on its type or state.
- For example, suppose we have a Shape class and three subclasses: Triangle, Rectangle and Square.
- We want to send the message show() to a Shape object, which could be an instance of any of the subclasses at run-time.
- We can represent this polymorphism in a collaboration diagram as follows:

![collaboration diagram](https://i.stack.imgur.com/8Zp0f.png)

- The diagram shows four scenarios: one for each subclass and one for the default case.
- The guard conditions are written in brackets above the scenarios.
- The messages are numbered according to the order of execution.
- The diagram shows that the show() message is sent to the Shape object, which then delegates it to the appropriate subclass object based on its type.
- The subclass object then performs its own show() method, which may differ from the other subclasses.