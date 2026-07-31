### Depicting Asynchronous Messages with/without Priority

In the context of Object Oriented System Design, asynchronous messages are used to represent communication between objects that does not require an immediate response. This means that the sender of the message can continue its execution without waiting for a response from the receiver.

Asynchronous messages can be depicted in a sequence diagram using a line with an open arrowhead. The arrowhead points from the sender to the receiver, indicating the direction of the message.

Asynchronous messages can also have a priority associated with them. This priority determines the order in which messages are processed by the receiver. Messages with a higher priority are processed before messages with a lower priority.

To depict an asynchronous message with a priority, the priority value can be included in the message label. For example, a message with a priority of 1 can be depicted as `message [1]`.

In summary:
- Asynchronous messages are used to represent communication that does not require an immediate response.
- They can be depicted in a sequence diagram using a line with an open arrowhead.
- Asynchronous messages can have a priority associated with them, which determines the order in which they are processed.
- The priority value can be included in the message label to depict an asynchronous message with a priority.
