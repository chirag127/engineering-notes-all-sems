### Depicting Asynchronous Messages with/without Priority for the Notes of the Unit 2 - Basic Structural Modeling in the Subject of Object Oriented System Design

- Asynchronous messages are messages that are sent from one object to another without waiting for a response.
- These messages are used when the sender does not need to wait for the receiver to complete its task before continuing.
- Asynchronous messages can be depicted in a sequence diagram using a half-arrowhead line with an open arrowhead.
- The arrowhead points in the direction of the message flow, from the sender to the receiver.
- Asynchronous messages can be sent with or without priority.
- If the messages are sent with priority, they are processed by the receiver in the order of their priority.
- If the messages are sent without priority, they are processed by the receiver in the order in which they are received.
- Priority can be depicted in a sequence diagram by adding a label to the message arrow with the priority level.
- For example, a message with a high priority can be labeled as "High Priority" or simply "High".
- A message with a low priority can be labeled as "Low Priority" or simply "Low".
- The use of priority in asynchronous messages can help to ensure that important messages are processed before less important messages.