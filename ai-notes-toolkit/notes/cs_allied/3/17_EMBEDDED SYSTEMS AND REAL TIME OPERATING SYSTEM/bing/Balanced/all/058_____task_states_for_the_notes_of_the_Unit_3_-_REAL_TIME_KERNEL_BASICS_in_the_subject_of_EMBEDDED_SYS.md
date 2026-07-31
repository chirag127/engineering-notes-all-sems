# Task States for the Notes of the Unit 3 - Real Time Kernel Basics

- A task is a unit of execution in a real time operating system (RTOS) that can be scheduled and preempted by the kernel .
- A task state is the condition of a task at a given point of time, which determines its readiness and eligibility to run on the processor  .
- The task state consists of a snapshot of all the processor registers, along with an individual heap and stack memory allocation for each task.
- The task state can change due to various events, such as system timer interrupts, task creation and deletion, task synchronization and communication, task priority changes, etc .
- The common task states in a real time kernel are:

  - **Running**: The task is currently executing on the processor or is ready to execute on the processor as soon as it gets the opportunity  . This is the only possible state for a task executing in user space. It can also apply to a task in kernel space that is actively running.
  - **Ready**: The task is not running but is eligible to run as soon as the processor becomes available or a higher priority task finishes its execution . The ready tasks are usually maintained in a run queue according to their priorities .
  - **Blocked**: The task is not running and is not eligible to run until a certain event occurs, such as a timer expiration, a semaphore release, a message arrival, etc . The blocked tasks are usually maintained in a wait queue according to the event they are waiting for .
  - **Suspended**: The task is not running and is not eligible to run until another task explicitly resumes it . The suspended tasks are usually maintained in a separate list . Suspension is a way of temporarily disabling a task without deleting it .
  - **Terminated**: The task is not running and is not eligible to run ever again, as it has completed its execution or has been deleted by another task . The terminated tasks are usually removed from the system and their resources are freed .

- The task state diagram shows the possible transitions between the task states and the events that cause them:

![Task State Diagram](https://i.imgur.com/0y0x0yC.png)

: https://forum.arduino.cc/t/what-is-task-state-in-real-time-operating-system/651877
: http://www.on-time.com/rtkernel-dos.htm
: https://www.humblec.com/proccess-states-in-linux-kernel/
: https://www.redhat.com/sysadmin/real-time-kernel
: https://en.wikipedia.org/wiki/Sun#:~:text=The%20core%20of%20the%20Sun%20extends%20from%20the,the%20Sun%27s%20surface%20temperature%20is%20approximately%205800%20K.
: https://www.freertos.org/a00015.html