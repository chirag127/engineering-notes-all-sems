 Here is the content in markdown format as per your instructions:

#### Multithread programming in Core Java.

1. Threads - A thread is a lightweight process that executes within a program and is used to multitask. Java supports multithreading that allows a program to perform multiple tasks simultaneously.
2. Creating Threads - There are two ways to create a thread in Java:
- Extending the Thread class: Create a class that extends Thread class and override the run() method.
- Implementing the Runnable interface: Create a class that implements Runnable interface and override the run() method. Then pass an instance of the class to the Thread constructor to create and start the thread.
3. Starting Threads - Once a thread is created, it will not start executing automatically. The start() method of Thread class is used to start the execution of a thread.
4. Thread State - A thread always exists in one of the following states:
- New: When a thread is instantiated, it is in new state.
- Runnable: A thread is in runnable state after start() is called but the thread scheduler has not selected it yet for running.
- Running: The thread scheduler has selected the thread and it is currently running.
- Blocked: A thread is blocked waiting for a lock, I/O, etc.
- Waiting: A thread is waiting for some condition to occur.
- Terminated: A thread has completed its task.

[No emojis or external links have been included as per the instructions.]