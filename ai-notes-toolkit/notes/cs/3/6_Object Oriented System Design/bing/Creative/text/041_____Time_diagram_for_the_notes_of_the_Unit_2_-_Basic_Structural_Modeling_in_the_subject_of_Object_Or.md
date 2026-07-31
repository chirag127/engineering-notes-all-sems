### Time diagram for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- Object Oriented System Design is a process of defining the architecture, modules, interfaces, and data for a system that uses objects and their relationships as the main components.
- Basic Structural Modeling is a part of Object Oriented System Design that focuses on the static structure of the system, such as the classes, attributes, operations, and associations that make up the system.
- A time diagram is a type of UML diagram that shows the behavior of individual objects and interactions of objects along a linear time axis.
- A time diagram can be used to model the timing constraints and performance requirements of a system, such as the response time, latency, throughput, and concurrency of events.
- A time diagram consists of the following elements:
  - Lifelines: vertical dashed lines that represent the existence of an object or a participant in the system over time.
  - States: horizontal rectangles that show the state or condition of a lifeline at a specific point in time.
  - Transitions: horizontal arrows that show the change of state or condition of a lifeline due to an event or a message.
  - Events: points or intervals on a lifeline that indicate the occurrence of something significant, such as a message, a signal, a change of value, or a constraint.
  - Messages: horizontal arrows that show the communication or interaction between lifelines, such as a method call, a return value, or a signal.
  - Constraints: expressions that specify the conditions or restrictions on the timing or ordering of events or messages.
- An example of a time diagram for a basic structural modeling of a system that manages online orders is shown below:

![Time diagram example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/what-is-timing-diagram/timing-diagram-example.png)

- The time diagram shows the lifelines of the customer, the order, the payment, and the delivery objects, and their states and transitions over time.
- The events and messages that occur between the lifelines are also shown, such as the customer placing an order, the order being processed, the payment being authorized, and the delivery being confirmed.
- The constraints on the timing or ordering of the events and messages are also shown, such as the order must be processed within 24 hours, the payment must be authorized before the delivery, and the delivery must be confirmed within 7 days.