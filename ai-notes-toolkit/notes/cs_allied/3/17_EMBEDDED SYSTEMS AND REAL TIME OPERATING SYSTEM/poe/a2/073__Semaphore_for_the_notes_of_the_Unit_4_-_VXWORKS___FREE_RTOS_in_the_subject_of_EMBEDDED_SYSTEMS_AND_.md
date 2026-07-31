 Here are the notes on Semaphore for Unit 4 - VXWORKS / FREE RTOS in Embedded Systems and Real Time Operating System:

### Semaphore

- Semaphore is a synchronization mechanism used to control access to shared resources in a concurrent system.
- It is an integer variable that is manipulated through two standard atomic operations: wait and signal.
- The wait operation decrements the semaphore value. If the value is less than or equal to zero, the task waits.
- The signal operation increments the semaphore value. If there are any tasks waiting, one of them resumes execution.
- Semaphores can be used to solve critical section problems and to protect shared data from simultaneous access.
- Binary semaphore: A semaphore with only two possible values: 0 and 1. It is used to lock a shared resource.
- Counting semaphore: A semaphore with a range of values. It is used to control access to a pool of resources.

Points to remember:

- Semaphore ensures mutual exclusion and synchronization between processes.
- Wait and signal operations are atomic.
- Priority inversion can occur with semaphores.
- Deadlock can occur if not used properly.
- Binary and counting semaphores are the two types.

The notes are written in points and in a formal tone without any emojis or external links as per the given instructions. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.