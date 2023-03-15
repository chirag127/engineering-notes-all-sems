### Polymorphism in Collaboration Diagrams

- Polymorphism is the ability of an object to behave differently depending on its type or context.
- In collaboration diagrams, polymorphism is represented by using multiple scenarios controlled by guard conditions.
- Guard conditions are expressions that evaluate to true or false and determine which scenario is executed.
- Each scenario shows how a message is sent to an object of a specific type or class.
- For example, suppose we have a Shape class and three subclasses: Triangle, Rectangle and Square.
- We want to send a show() message to a Shape object, but the behavior of show() depends on the type of the object at run-time.
- We can use a collaboration diagram to show the different scenarios for show() as follows:

```
+-----------------+
| Shape           |
+-----------------+
| show()          |
+-----------------+
        |
        | show()
        |
        V
+-----------------+
| Triangle        |
+-----------------+
| show()          |
+-----------------+
[shapeType == Triangle]
        |
        | show()
        |
        V
+-----------------+
| Rectangle       |
+-----------------+
| show()          |
+-----------------+
[shapeType == Rectangle]
        |
        | show()
        |
        V
+-----------------+
| Square          |
+-----------------+
| show()          |
+-----------------+
[shapeType == Square]
```

- The diagram shows that the show() message is sent to a Shape object, which can be an instance of Triangle, Rectangle or Square at run-time.
- The guard conditions [shapeType == Triangle], [shapeType == Rectangle] and [shapeType == Square] indicate which scenario is executed depending on the value of the shapeType attribute of the Shape object.
- Each scenario shows how the show() message is forwarded to the corresponding subclass object, which implements the show() method in a different way.