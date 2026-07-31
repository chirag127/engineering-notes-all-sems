# Collaboration Diagrams

Collaboration diagrams are a type of UML diagram that show the interactions and relationships among objects in a system. They are also known as communication diagrams in UML 2.x. They are similar to sequence diagrams, but they emphasize the structure and organization of the objects rather than the time sequence of the messages.

## Components of a Collaboration Diagram

A collaboration diagram consists of the following components:

- Objects: Objects are shown as rectangles with naming labels inside. The naming label follows the convention of object name : class name. For example, a1 : Account. Objects can also have attributes and operations, which are shown below the naming label. For example, a1 : Account
balance : int
deposit(amount : int)
- Actors: Actors are instances that invoke the interaction in the diagram. Each actor has a name and a role, with one of them underlined. For example, c : Customer. Actors are shown as stick figures or icons.
- Links: Links are solid lines that connect objects and actors. They represent the associations or relationships among them. For example, a link between a customer and an account object indicates that the customer owns the account.
- Messages: Messages are the communications or interactions that occur between objects and actors. They are shown as labeled arrows along the links. The label indicates the name of the message and the arguments, if any. For example, deposit(100) is a message from the customer to the account object. Messages can also have sequence numbers, which indicate the order of execution. For example, 1. deposit(100) is the first message in the interaction.
- Constraints: Constraints are conditions or rules that apply to the interaction. They are shown as text in curly brackets. For example, {balance > 0} is a constraint that the balance of the account must be positive.

## How to Create a Collaboration Diagram

A collaboration diagram can be created by following these steps:

- Identify the objects and actors involved in the interaction. Determine their roles and responsibilities, and their relationships with each other.
- Draw the objects and actors as rectangles and stick figures, respectively. Label them with their names and classes, and their attributes and operations if needed.
- Draw the links between the objects and actors to show their associations. Use different types of lines to indicate different types of relationships, such as aggregation, composition, inheritance, etc.
- Draw the messages along the links to show the interactions. Label them with their names and arguments, and their sequence numbers if needed. Use different types of arrows to indicate different types of messages, such as synchronous, asynchronous, return, etc.
- Add constraints if necessary to specify the conditions or rules that apply to the interaction. Use curly brackets to enclose the text.

## Example of a Collaboration Diagram

Here is an example of a collaboration diagram that shows the interaction between a customer and an ATM system to withdraw money from an account.

![Collaboration diagram example](https://www.edrawmax.com/images/article/collaboration-diagram-uml.png)

The diagram shows the following components:

- Objects: atm : ATM, a : Account, c : Card, p : Printer
- Actors: cust : Customer
- Links: cust and atm are associated, atm and a are associated, atm and c are associated, atm and p are associated, a and c are aggregated
- Messages: 1. insertCard(c), 2. validate(c), 3. enterAmount(), 4. checkBalance(), 5. dispenseCash(), 6. printReceipt(), 7. ejectCard()
- Constraints: {amount <= balance}