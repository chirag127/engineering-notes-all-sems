# Broadcast messages for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- Broadcast messages are a type of messages that are sent from one object to multiple objects in an object-oriented system.
- Broadcast messages are useful for implementing scenarios where an event or an action affects many objects at once, such as notifications, alerts, updates, etc .
- Broadcast messages can have different scopes depending on the context and the design of the system. For example, a broadcast message can be sent to all objects in the system, or only to a subset of objects that belong to a certain class, group, or hierarchy .
- Broadcast messages can be implemented using different mechanisms, such as:
  - Publish-subscribe pattern: The sender object publishes a message to a topic or a channel, and the receiver objects subscribe to that topic or channel to receive the message.
  - Observer pattern: The sender object maintains a list of observer objects that are interested in its state changes, and notifies them whenever a change occurs.
  - Multicast protocol: The sender object uses a network protocol that allows sending a message to a group of destination addresses simultaneously.
- Broadcast messages have some advantages and disadvantages, such as:
  - Advantages:
    - They reduce the coupling between the sender and the receiver objects, as the sender does not need to know the identity or the number of the receiver objects.
    - They allow for dynamic and flexible communication, as the receiver objects can join or leave the broadcast group at any time.
    - They enable parallel and concurrent processing, as the receiver objects can handle the message independently and asynchronously.
  - Disadvantages:
    - They can cause performance issues, as the sender object has to send the same message multiple times, and the receiver objects have to process the message even if they are not interested or affected by it.
    - They can introduce complexity and ambiguity, as the sender object has to ensure the consistency and the validity of the message, and the receiver objects have to coordinate their actions and responses to the message.
    - They can create security and privacy risks, as the sender object has to protect the message from unauthorized access or modification, and the receiver objects have to verify the source and the content of the message.