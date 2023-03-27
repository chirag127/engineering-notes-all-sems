### Event based for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

In this unit, we will learn about event-based systems and how they are used in real-time operating systems. Here are some key points to keep in mind:

- An event-based system is one in which the system responds to events or interrupts that occur in the system. These events can be external, such as a user input or a sensor reading, or they can be internal, such as a timer interrupt.

- Real-time operating systems (RTOS) are designed to handle these events in a timely and deterministic manner. This means that the system must respond to events within a specific time frame, usually measured in microseconds or milliseconds.

- The kernel of an RTOS is responsible for managing these events and ensuring that they are handled in a timely manner. The kernel must also prioritize events based on their importance and ensure that higher-priority events are handled before lower-priority events.

- In an event-based system, the system is designed to be reactive rather than proactive. This means that the system only responds to events as they occur, rather than constantly polling for new data. This can help to conserve system resources and reduce power consumption.

- One common use of event-based systems is in embedded systems, where the system must respond to external events such as sensor readings or user inputs. In these systems, the kernel must be able to handle multiple events simultaneously, while still maintaining real-time performance.

- To implement an event-based system, the kernel must provide a mechanism for registering and handling events. This can be done using event queues or message passing mechanisms.

- In summary, event-based systems are an important aspect of real-time operating systems and are essential in many embedded systems. Understanding how events are handled by the kernel is crucial for designing and implementing real-time systems.