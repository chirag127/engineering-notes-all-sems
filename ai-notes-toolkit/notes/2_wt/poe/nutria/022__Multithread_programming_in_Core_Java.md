

#### Multithread programming in Core Java

* Multithreading is a programming technique that allows a program to execute multiple tasks simultaneously. 
* In Core Java, multithreading is implemented using the `Thread` class and related classes. 
* To create a thread, you must create a class that extends the `Thread` class and override the `run()` method. 
* The `run()` method is the entry point for the thread, and it is where the code for the thread should be placed. 
* To start the thread, you must call the `start()` method. 
* Once the thread is started, it will execute until the `run()` method returns or the thread is interrupted. 
* To ensure that threads can access shared resources safely, you should use synchronization to ensure that only one thread can access a resource at a time. 
* To make sure that threads are properly terminated, you should use the `join()` method to wait for the thread to finish. 
* In addition to the `Thread` class, the `Runnable` interface can also be used to create threads. 
* The `Runnable` interface provides a single method, `run()`, which is the entry point for the thread. 
* The `Runnable` interface is preferred over the `Thread` class when creating threads because it makes the code more modular and easier to maintain.