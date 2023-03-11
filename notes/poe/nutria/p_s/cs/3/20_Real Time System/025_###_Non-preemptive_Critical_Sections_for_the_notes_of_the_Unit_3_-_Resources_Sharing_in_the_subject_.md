
### Non-preemptive Critical Sections for the Notes of Unit 3 - Resources Sharing in the Subject of Real Time System

Non-preemptive Critical Sections (NPCS) are a type of resource sharing technique used in Real Time Systems. This technique is used to ensure that a single process or thread does not access a shared resource at the same time as another process or thread.

NPCS works by allowing a process to request access to a shared resource, and then wait until the resource becomes available. Once the resource is available, the process can access it without interruption.

Advantages of using NPCS:

* It ensures that a single process or thread does not access a shared resource at the same time as another process or thread.
* It is relatively easy to implement.
* It does not require any additional synchronization primitives.

Disadvantages of using NPCS:

* It is not suitable for time-critical applications, as the process or thread requesting access to the shared resource may have to wait for an indefinite amount of time.
* It can lead to resource starvation, as the process or thread requesting access to the shared resource may have to wait for an indefinite amount of time.

Examples of applications that use NPCS:

* Operating systems: NPCS can be used to ensure that multiple threads do not access the same memory location at the same time.
* Database systems: NPCS can be used to ensure that multiple processes do not access the same data at the same time.
* Networking systems: NPCS can be used to ensure that multiple processes do not access the same network device at the same time.

NPCS can be implemented using semaphores, monitors or message passing.

Semaphores:

* A semaphore is a synchronization primitive that can be used to implement NPCS.
* A semaphore is a variable that is shared between multiple processes or threads.
* A process or thread can request access to a shared resource by decrementing the semaphore.
* If the semaphore is greater than zero, the process or thread can access the shared resource.
* When the process or thread is finished with the shared resource, it can increment the semaphore.

Monitors:

* A monitor is a synchronization primitive that can be used to implement NPCS.
* A monitor is a data structure that is shared between multiple processes or threads.
* A process or thread can request access to a shared resource by entering the monitor.
* If the monitor is free, the process or thread can access the shared resource.
* When the process or thread is finished with the shared resource, it can exit the monitor.

Message Passing:

* Message passing is a synchronization primitive that can be used to implement NPCS.
* A process or thread can request access to a shared resource by sending a message to another process or thread.
* If the message is received, the process or thread can access the shared resource.
* When the process or thread is finished with the shared resource, it can send a message to the other process or thread.