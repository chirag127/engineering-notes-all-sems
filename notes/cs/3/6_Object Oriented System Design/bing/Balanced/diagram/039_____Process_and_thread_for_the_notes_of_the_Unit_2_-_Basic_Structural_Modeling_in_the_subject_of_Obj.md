Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on process and thread for the notes of the unit 2 - basic structural modeling in the subject of object oriented system design.

### Process and thread

- A process is an independent sequence of execution that runs in its own memory space.
- A thread is a segment of a process that shares the memory space with other threads of the same process.
- A process can have multiple threads, all executing at the same time.
- Threads of the same process can communicate with each other through shared variables, whereas processes need inter-process communication mechanisms to communicate with each other.
- Processes are more expensive to create, terminate, and switch than threads.

### Process and thread in object oriented system design

- In object oriented system design, objects are the basic units of abstraction and encapsulation.
- Objects can be classified into active and inactive objects.
- Active objects have independent threads of control that can execute concurrently with threads of other objects.
- Inactive objects do not have threads of control and depend on the threads of other objects to invoke their operations.
- Active objects can synchronize with each other as well as with purely sequential objects using events and signals.
- Events are occurrences that trigger changes in the state or behavior of an object.
- Signals are messages that carry information about events from one object to another.
- Activity diagrams are graphical representations of the dynamic behavior of objects in terms of events, signals, actions, and transitions.