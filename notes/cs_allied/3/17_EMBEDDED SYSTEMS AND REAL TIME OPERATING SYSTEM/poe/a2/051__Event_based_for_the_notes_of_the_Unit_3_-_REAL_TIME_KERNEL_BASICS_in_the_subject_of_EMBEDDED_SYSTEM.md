 Here are the notes for the topic "Event based for the notes of the Unit 3 - REAL TIME KERNEL BASICS" in formal markdown format without any emojis or external links:

### Event based for the notes of the Unit 3 - REAL TIME KERNEL BASICS

1. Events: Events are detectable changes in a system that affect the execution of processes or threads. For example, input from a device, expiration of a timer, completion of an I/O operation, etc.
2. Event-driven systems: In event-driven systems, processes are executed in response to events. The kernel executes the process that is waiting for an occurred event. This allows for efficient utilization of processor time and rapid response to events. Many real-time systems are event-driven.
3. Event variables: The state of an event is stored in an event variable. An event can be signaled by changing the value of its event variable. Processes can wait for an event by waiting for a particular value of the event variable. This is called event synchronization.
4. Event queues: The kernel maintains event queues to keep track of pending events. The kernel searches the event queue to determine which process to execute when an event occurs. The kernel can use different queues for different types of events. The scheduler can determine the priority of the events and handle high-priority events before low-priority events.
5. Event handlers: Event handlers are routines that are executed automatically by the kernel in response to events. The event handler performs the task required to respond to the event, such as reading input, sending output, or notifying processes. The event handler allows for a rapid and efficient response to events.

The notes summarize the key points about events, event-driven systems, event variables, event queues, and event handlers in a formal tone with markdown formatting and without any emojis or external links as requested. Please let me know if you would like me to explain or expand on any of the points.