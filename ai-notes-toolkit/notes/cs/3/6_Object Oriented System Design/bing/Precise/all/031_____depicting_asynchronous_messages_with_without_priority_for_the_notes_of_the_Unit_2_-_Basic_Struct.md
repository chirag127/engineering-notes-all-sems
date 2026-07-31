### Depicting Asynchronous Messages with/without Priority

Asynchronous messages are messages that are sent from one object to another, but the sender does not wait for a response before continuing its execution. This is in contrast to synchronous messages, where the sender waits for a response before continuing.

In UML sequence diagrams, asynchronous messages are depicted using a line with an open arrowhead. The arrowhead points from the sender to the receiver, indicating the direction of the message.

Asynchronous messages can be sent with or without priority. When sent with priority, the message is placed at the front of the receiver's message queue, and is processed before other messages. When sent without priority, the message is placed at the back of the receiver's message queue, and is processed in the order it was received.

In UML sequence diagrams, priority can be indicated by adding a "P" to the message label. For example, a message labeled "doSomething()" would be sent without priority, while a message labeled "P: doSomething()" would be sent with priority.

Here are some key points to remember when depicting asynchronous messages with/without priority in UML sequence diagrams:

- Asynchronous messages are depicted using a line with an open arrowhead.
- The arrowhead points from the sender to the receiver, indicating the direction of the message.
- Asynchronous messages can be sent with or without priority.
- Priority can be indicated by adding a "P" to the message label.
- When sent with priority, the message is placed at the front of the receiver's message queue.
- When sent without priority, the message is placed at the back of the receiver's message queue.
