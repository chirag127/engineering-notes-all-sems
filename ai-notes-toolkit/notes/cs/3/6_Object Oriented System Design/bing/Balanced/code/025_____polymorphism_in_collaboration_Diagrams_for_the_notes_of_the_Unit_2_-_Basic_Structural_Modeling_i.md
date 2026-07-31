### Polymorphism in Collaboration Diagrams

- Polymorphism is the ability of an object to behave differently depending on its type or class at run-time.
- Collaboration diagrams are used to show the relationship and interaction between the objects in a system.
- Polymorphism can be represented in a collaboration diagram by using multiple scenarios controlled by guard conditions.
- Guard conditions are expressions that evaluate to true or false and determine whether a message is sent or not.
- For example, suppose we have a Shape class and three subclasses: Triangle, Rectangle and Square. We want to send the show() message to a Shape object, but the behavior of show() depends on the type of the object at run-time.
- We can use a collaboration diagram to model this polymorphic behavior as follows:

```
+-----------------+        +-----------------+
| Shape           |        | Shape           |
|-----------------|        |-----------------|
|                 |        |                 |
|                 |        |                 |
|                 |        |                 |
+-----------------+        +-----------------+
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |[type = Triangle]        |[type = Rectangle]
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     |                          |
     +-----------------+        +-----------------+
     | Triangle        |        | Rectangle       |
     |-----------------|        |-----------------|
     |                 |        |                 |
     |                 |        |                 |
     |                 |        |                 |
     +-----------------+        +-----------------+
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |1. show()                |1. show()
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          |                          |
          +-----------------+        +-----------------+
          | Screen          |        | Screen          |
          |-----------------|        |-----------------|
          |                 |        |                 |
          |                 |        |                 |
          |                 |        |                 |
          +-----------------+        +-----------------+
```

- In this diagram, we have two scenarios: one for when the Shape object is a Triangle, and one for when it is a Rectangle. Each scenario has a guard condition that checks the type of the object before sending the show() message. The message is numbered as 1 in both scenarios, indicating that it is the same message but with different behavior depending on the type of the object. The Screen object is the receiver of the message and displays the shape accordingly.