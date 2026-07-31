Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of event and signals for the unit 2 - basic structural modeling in the subject of object oriented system design.

### Event and signals

- An event is something that happens and has significance for the system or its actors .
- Events can be classified into four kinds :
  - Signal events: These are events that represent the asynchronous transmission of information from one object to another . For example, a button click, a sensor reading, or a message notification.
  - Call events: These are events that represent the synchronous invocation of an operation from one object to another . For example, a method call, a function call, or a procedure call.
  - Time events: These are events that occur after a specified period of time has elapsed . For example, a timer, a deadline, or a schedule.
  - Change events: These are events that occur when a condition becomes true or false . For example, a state change, a threshold crossing, or a trigger.
- A signal is an object that carries information and is dispatched by one object and received by another  .
- A signal can have attributes that specify the data carried by the signal .
- A signal can be sent or received by an object using the following notation :

![signal notation](https://www.pvpsiddhartha.ac.in/dep_it/lecturenotes/OOAD/images/fig4.1.jpg)

- The sender object is connected to the signal by a dashed line with an open arrowhead pointing to the signal .
- The receiver object is connected to the signal by a dashed line with a filled arrowhead pointing from the signal .
- The name of the signal is written above or below the signal symbol .
- The attributes of the signal are written in parentheses after the name of the signal .
- A signal can be sent or received by an actor using the same notation, except that the actor is represented by a stick figure .
- A signal can also be sent or received by the system boundary using the same notation, except that the system boundary is represented by a rectangle with the name of the system .
- A signal can be used to model external events that pass between the system and its actors, or internal events that pass among the objects that live within the system .
- A signal can be used to model asynchronous communication, where the sender does not wait for a response from the receiver  .
- A signal can also be used to model acknowledgement, where the receiver sends a separate signal back to the sender to confirm the receipt of the original signal.
