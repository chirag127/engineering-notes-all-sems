### Process and thread

- A **process** is an independent sequence of execution that runs in its own memory space . A process can have one or more threads, which are units of execution within a process .
- A **thread** is a segment of a process that can execute concurrently with other threads of the same or different processes . A thread shares the memory and resources of its parent process, but has its own stack, program counter, and registers.
- In object-oriented system design, there are two types of objects: **active** and **inactive**. Active objects have independent threads of control that can execute concurrently with threads of other objects, while inactive objects do not have threads of their own and depend on the threads of other objects to invoke their methods.
- Active objects can synchronize with other active or inactive objects using **events** and **signals**. An event is an occurrence of something of interest that triggers a reaction from an object, while a signal is a kind of event that represents a synchronous communication between objects.
- An **activity diagram** is a graphical representation of the dynamic behavior of a system, showing the flow of control and data among objects. An activity diagram can depict the concurrent execution of threads, the synchronization of events and signals, and the conditions and actions that govern the system.
- An example of an activity diagram for a simple banking system is shown below:

![Activity diagram for a simple banking system](https://i.imgur.com/0wzZx4F.png)