### Process and thread

- A **process** is an independent sequence of execution that runs in its own memory space . A process can have one or more threads, which are units of execution within a process .
- A **thread** is a segment of a process that can execute concurrently with other threads of the same process or different processes . A thread shares the memory and resources of its parent process, but has its own stack, program counter, and registers.
- In object-oriented system design, there are two types of objects: **active** and **inactive**. Active objects have independent threads of control that can execute concurrently with threads of other objects, while inactive objects do not have threads of their own and depend on the threads of other objects to invoke their methods.
- Active objects can synchronize with other active or inactive objects using **events** and **signals**. An event is a specification of a significant occurrence that has a location in time and space, while a signal is a specification of an asynchronous stimulus communicated between instances of objects.
- An **activity diagram** is a graphical representation of the dynamic behavior of a system, showing the flow of control from one activity to another. An activity is a specification of a parameterized sequence of behavior. An activity diagram can show the concurrent execution of threads using **fork** and **join** nodes, which split and merge the flow of control.
- An example of an activity diagram for a process with two threads is shown below:

![Activity diagram example](https://i.imgur.com/9x6x0fK.png)