### Use of self in messages

- In object-oriented system design, a message is a request from one object to another object to perform some action or return some information.
- A message consists of a sender, a receiver, a selector, and optional arguments.
- A self message is a special type of message where the sender and the receiver are the same object.
- A self message indicates that the object is invoking one of its own methods or accessing one of its own attributes.
- A self message is represented by a U-shaped arrow in a sequence diagram .
- A self message can be used to model recursive calls, internal state changes, or delegation of responsibilities within an object.
- For example, a device object may send a self message to access its webcam or to check its battery level .