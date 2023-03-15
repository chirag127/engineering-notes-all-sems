### Use of self in messages

- In object-oriented system design, a message is a request from one object to another object to perform some action or return some information.
- A message consists of a sender, a receiver, a method name, and optional arguments.
- A self message is a special type of message where the sender and the receiver are the same object .
- A self message indicates that the object is invoking one of its own methods, either to perform some internal computation or to access some of its own attributes.
- A self message is represented by a U-shaped arrow that points back to the same lifeline in a sequence diagram .
- For example, consider a scenario where a device object wants to access its webcam object. The device object can send a self message to itself to get a reference to the webcam object, and then send another message to the webcam object to start the camera .
- The following sequence diagram illustrates this example:

```sequence
Device->Device: getWebcam()
Device->Webcam: startCamera()
```

- Self messages are useful for modeling recursive or nested method calls, as well as internal state changes or behaviors of an object .