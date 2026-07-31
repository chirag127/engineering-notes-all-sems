### Collaboration Diagrams

Collaboration diagrams are a type of UML diagram that show the interactions and relationships among objects in a system. They are similar to sequence diagrams, but they emphasize the structure and organization of the objects rather than the time sequence of the messages. Collaboration diagrams can be used to model the collaborations, mechanisms, or the structural organization within a system design.

Some of the main features of collaboration diagrams are:

- Objects are represented by rectangles with the object name and optionally the class name inside. For example, `:Customer` or `c1:Customer`.
- Actors are external entities that initiate the interaction in the diagram. They are shown as stick figures with the actor name and role. For example, `User:Customer`.
- Links are lines that connect objects and actors. They represent the associations or connections among them. For example, a solid line with an arrowhead indicates a message being sent from one object to another.
- Messages are the information or actions that are exchanged among the objects and actors. They are shown as labels along the links, with an optional sequence number to indicate the order of execution. For example, `1:login()` or `2.1:validate()`.
- Self messages are messages that an object sends to itself. They are shown as loops on the object rectangle. For example, `3:calculateTotal()`.
- Return messages are messages that indicate the return value or result of a previous message. They are shown as dashed lines with an arrowhead pointing back to the sender. For example, `2.1.1:isValid`.
- Constraints are expressions that specify the conditions or rules that apply to the interaction. They are shown as text in curly braces. For example, `{c1.balance > 0}`.
- Notes are comments or explanations that can be added to the diagram. They are shown as rectangles with a dog-ear and attached to an element by a dashed line. For example, `Note: This is a sample collaboration diagram`.

Here is an example of a collaboration diagram for a bank ATM system:

```text
+----------------+             +----------------+
| User:Customer  |             |:ATM            |
+----------------+             +----------------+
       |                              |
       |1:insertCard()                |
       |----------------------------->|
       |                              |
       |2:enterPIN()                  |
       |----------------------------->|
       |                              |             +----------------+
       |                              |             |:Bank           |
       |                              |             +----------------+
       |                              |3:validate() |                |
       |                              |------------>|                |
       |                              |             |4:checkBalance()|
       |                              |             |--------------->|
       |                              |             |                |
       |                              |<-------------|                |
       |                              |5:isValid    |                |
       |                              |             |                |
       |                              |             |                |
       |6:selectOption()              |             |                |
       |----------------------------->|             |                |
       |                              |             |                |
       |                              |             |                |
       |7:withdrawCash()              |             |                |
       |----------------------------->|             |                |
       |                              |             |                |
       |                              |8:updateBalance()             |
       |                              |------------>|                |
       |                              |             |                |
       |                              |<-------------|                |
       |                              |9:receipt    |                |
       |                              |             |                |
       |<-----------------------------|             |                |
       |10:cash                       |             |                |
       |                              |             |                |
       |                              |             |                |
       |11:ejectCard()                |             |                |
       |----------------------------->|             |                |
       |                              |             |                |
       |<-----------------------------|             |                |
       |12:card                       |             |                |
       |                              |             |                |
```