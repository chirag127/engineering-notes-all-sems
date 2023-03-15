### Depicting asynchronous messages with/without priority

- Asynchronous messages are messages that are sent from one object to another without waiting for a response.
- Asynchronous messages are useful for modeling concurrent or parallel activities, such as sending an email or printing a document.
- Asynchronous messages are depicted by a dashed arrow with an open arrowhead in a sequence diagram.
- Asynchronous messages can have a priority, which indicates the relative importance or urgency of the message.
- Priority can be shown by adding a label with a number or a symbol to the message arrow, such as `p=1` or `!`.
- Priority can also be shown by using different colors or styles for the message arrows, such as red or bold for high priority messages.
- The priority of an asynchronous message affects the order in which the messages are processed by the receiver object, but not the order in which they are sent by the sender object.
- The sender object can continue its execution after sending an asynchronous message, regardless of the priority of the message.
- The receiver object can process an asynchronous message at any time, depending on its availability and the priority of the message.
- The receiver object can process multiple asynchronous messages concurrently, if it has the capability and resources to do so.