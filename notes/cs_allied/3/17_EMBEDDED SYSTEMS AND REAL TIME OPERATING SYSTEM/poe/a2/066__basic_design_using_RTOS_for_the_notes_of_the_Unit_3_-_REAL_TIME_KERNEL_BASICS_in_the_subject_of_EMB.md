 Here is the content in Markdown format without any emojis or external links:

### Basic design using RTOS for the notes of the Unit 3 - REAL TIME KERNEL BASICS

1. What is RTOS?
- RTOS stands for Real Time Operating System. It is an OS that serves the real time systems to respond to events within a strict time limit.
- It has a deterministic nature with predictable response time to events.
- It supports concurrent execution of multiple tasks.
- It provides real time services like scheduling, synchronization, communication, interrupt handling, etc.

2. Why RTOS?
- For precise and accurate control of a system.
- Where deadlines are critical for the correct operation.
- Situation demands fast response to events.
- Complex systems with multiple tasks running concurrently.

3. Key points in RTOS design:
- Preemptive and priority based scheduling: The scheduler allocates CPU to tasks based on priority to meet deadlines. It can preempt a low priority task with a high priority one.
- Event Flags: Used for synchronization between tasks or interrupt handlers through discrete signals.
- Semaphores: Used to protect shared resources through binary signals and resource counting.
- Message Queues: Used to send messages between tasks. The sender task sends a message to the queue and the receiver task receives it.
- Memory Management: RTOS provides memory partitioning and protection mechanisms.
- Device Drivers: RTOS provides APIs to write device drivers for peripherals.
- Timer Services: Provide tick interrupts at regular intervals to perform time related functionalities.

[Content continues in the same formal tone with points and sub-points...]