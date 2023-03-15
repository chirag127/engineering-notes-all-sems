### Use of self in messages

- In object-oriented system design, a message is a request from one object to another object to perform some action or return some information.
- A self message is a special type of message that an object sends to itself, usually to invoke another operation or change its own state.
- A self message is represented by a U-shaped arrow that starts and ends at the same lifeline in a sequence diagram.
- A self message can be synchronous or asynchronous, depending on whether the sender waits for the response or not.
- A self message can be useful for modeling scenarios where an object needs to access its own attributes or methods, or delegate some responsibility to another part of itself .
- For example, consider a scenario where a device object wants to access its webcam object. The device object can send a self message to its webcam object to request the video stream. This is shown in the following sequence diagram:

```sequence
Device->Device: self message
Device->Webcam: request video stream
Webcam->Device: return video stream
```