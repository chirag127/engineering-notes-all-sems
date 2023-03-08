### Iterated Messages for the Notes of the Unit 2 - Basic Structural Modeling in Object Oriented System Design

Structural modeling is a crucial part of Object Oriented System Design as it helps in representing the structure of the system being developed. Iterated Messages is one of the most commonly used techniques for structural modeling. Here are some important points to understand about Iterated Messages:

1. Iterated Messages is a technique used for modeling the collaboration between objects in an Object Oriented System.

2. In this technique, a sequence of messages is exchanged between objects to achieve a particular goal.

3. The sequence of messages is repeated iteratively until the goal is achieved.

4. The messages exchanged between objects are represented using arrows.

5. The objects involved in the collaboration are represented using boxes.

6. Iterated Messages can be used to model both synchronous and asynchronous communication between objects.

7. This technique is particularly useful for modeling complex interactions between objects.

8. It helps in identifying the roles and responsibilities of each object in the system.

9. Iterated Messages can be used in conjunction with other modeling techniques such as Use Case Diagrams and Class Diagrams to get a complete picture of the system being developed.

10. One of the advantages of Iterated Messages is that it provides a clear and concise representation of the collaboration between objects.

11. However, it can be difficult to model complex interactions using this technique, and it may not be suitable for all types of systems.

12. Let's take an example to understand how Iterated Messages can be used. Suppose we are developing a banking system, and we want to model the process of transferring funds between two accounts. We can use Iterated Messages to represent the sequence of messages exchanged between objects such as Account, Transfer, and Bank.

```
+-------------+         +-----------+         +----------+
|   Account   |---------| Transfer  |---------|   Bank   |
+-------------+         +-----------+         +----------+
      |                      |                      |
      |------debit---------->|                      |
      |                      |                      |
      |                      |------credit--------->|
      |                      |                      |
```

In this example, the Account object sends a message to the Transfer object to debit the funds from the sender's account. The Transfer object then sends a message to the Bank object to credit the funds to the receiver's account. This sequence of messages is repeated iteratively until the transfer is complete.

In conclusion, Iterated Messages is a powerful technique for modeling the collaboration between objects in an Object Oriented System. It provides a clear and concise representation of complex interactions between objects and helps in identifying the roles and responsibilities of each object in the system. However, it may not be suitable for all types of systems, and other modeling techniques may need to be used in conjunction with it to get a complete picture of the system being developed.