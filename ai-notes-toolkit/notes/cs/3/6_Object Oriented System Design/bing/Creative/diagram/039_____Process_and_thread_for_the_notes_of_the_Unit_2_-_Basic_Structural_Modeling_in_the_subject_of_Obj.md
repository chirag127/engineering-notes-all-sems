Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of process and thread for the unit 2 - basic structural modeling in the subject of object oriented system design.

### Process and thread

- A **process** is an independent sequence of execution that runs in its own memory space.
- A **thread** is a segment of a process that shares the same memory space with other threads of the same process.
- A process can have multiple threads, all executing at the same time.
- Threads of the same process can communicate with each other more easily than processes, as they share the same data and resources.
- Processes are more isolated and secure than threads, as they do not interfere with each other's memory.
- Threads are more lightweight and efficient than processes, as they take less time and resources to create, terminate and switch.

### Process and thread in object oriented system design

- In an object oriented system design, there are **active** and **inactive** objects.
- The active objects have independent threads of control that can execute concurrently with threads of other objects.
- The inactive objects do not have threads of control, and they only respond to requests from other objects.
- The active objects synchronize with one another as well as with purely sequential objects.
- The active objects can be modeled as **processes** or **threads**, depending on the level of abstraction and the design goals.
- The processes or threads can be represented by **activity diagrams**, which show the flow of control and the synchronization of events among the objects.
- The activity diagrams can also show the **events** and **signals** that trigger the transitions and actions of the objects.
- An event is an occurrence that changes the state of an object or a system.
- A signal is a type of event that carries information from one object to another.
- Events and signals can be used to model the communication and coordination among the processes or threads.