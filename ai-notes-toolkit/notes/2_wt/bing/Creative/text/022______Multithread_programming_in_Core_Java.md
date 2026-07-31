#### Multithread programming in Core Java

- Multithreading is a feature of Java that allows multiple threads of execution to run concurrently within a single program.
- A thread is a lightweight sub-process that can perform a specific task independently or in parallel with other threads.
- Threads share the same memory space and resources of the program, but have their own stack, program counter, and local variables.
- Threads can communicate with each other using shared variables, synchronization mechanisms, or inter-thread communication methods such as wait, notify, and notifyAll.
- Multithreading can improve the performance and responsiveness of a program by utilizing the available CPU cores and reducing the idle time of the processor.
- Multithreading can also create challenges such as concurrency issues, deadlock, starvation, race conditions, and memory consistency errors.
- To create and manage threads in Java, there are two main ways: extending the Thread class or implementing the Runnable interface.
- The Thread class provides methods to start, stop, suspend, resume, join, interrupt, and set the priority of a thread.
- The Runnable interface defines a single method run() that contains the logic of the thread.
- To start a thread, an instance of the Thread class or a class that implements the Runnable interface must be created and the start() method must be invoked on it.
- The start() method creates a new thread of execution and calls the run() method of the corresponding object.
- The run() method defines the behavior of the thread and can be overridden by subclasses of the Thread class or classes that implement the Runnable interface.
- The main thread of a Java program is the one that executes the main() method and can create and control other threads.
- The main thread can wait for the completion of other threads by using the join() method of the Thread class.
- The main thread can also terminate the program by calling the System.exit() method or by returning from the main() method.