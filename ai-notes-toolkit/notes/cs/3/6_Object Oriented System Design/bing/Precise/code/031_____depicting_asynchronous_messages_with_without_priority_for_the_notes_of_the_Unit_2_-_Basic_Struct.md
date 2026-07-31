### Depicting Asynchronous Messages with/without Priority

Asynchronous messages are messages that are sent from one object to another, but the sender does not wait for a response before continuing its execution. This is in contrast to synchronous messages, where the sender waits for a response before continuing.

In UML sequence diagrams, asynchronous messages are depicted using a line with an open arrowhead. The arrowhead points from the sender to the receiver, indicating the direction of the message.

When depicting asynchronous messages with priority, the priority can be indicated using a label next to the message arrow. For example, a high-priority message could be labeled with "high" or "urgent", while a low-priority message could be labeled with "low" or "non-urgent".

It is important to note that the priority of an asynchronous message only affects the order in which the messages are processed by the receiver. The sender does not wait for a response, regardless of the priority of the message.

Here are some key points to remember when depicting asynchronous messages with/without priority in UML sequence diagrams:

- Asynchronous messages are depicted using a line with an open arrowhead.
- The arrowhead points from the sender to the receiver.
- The priority of an asynchronous message can be indicated using a label next to the message arrow.
- The priority only affects the order in which the messages are processed by the receiver.
- The sender does not wait for a response, regardless of the priority of the message.
