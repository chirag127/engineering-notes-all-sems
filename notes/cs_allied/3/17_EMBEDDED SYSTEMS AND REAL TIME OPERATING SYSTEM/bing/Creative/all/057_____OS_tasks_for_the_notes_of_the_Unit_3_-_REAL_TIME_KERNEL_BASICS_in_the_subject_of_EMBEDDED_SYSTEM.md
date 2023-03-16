# OS Tasks for Embedded Systems

- An **embedded system** is a computer that supports a machine and performs one specific task in the bigger machine .
- An **embedded operating system** is a specialized OS that runs the code that allows the device to do its job and makes the device's hardware accessible to software that is running on top of the OS  .
- An **OS task** (also called a process or a thread) is a unit of execution that encapsulates all the information that is involved in the executing of a program, such as stack, program counter, source code, data, etc. .
- A **real-time kernel** is a type of embedded OS that guarantees a certain capability within a specified time constraint, such as responding to an event within a fixed amount of time.
- Some of the basic concepts and functions of a real-time kernel are:
  - **Task creation and deletion**: The kernel can create and delete tasks dynamically, depending on the application requirements. Each task has a unique identifier, a priority, and a set of attributes that define its behavior .
  - **Task scheduling and dispatching**: The kernel can decide which task to run next, based on the task priorities and the scheduling algorithm. The kernel can also switch from one task to another, saving and restoring the task context .
  - **Task synchronization and communication**: The kernel can provide mechanisms for tasks to coordinate their actions and exchange data, such as semaphores, mutexes, message queues, event flags, etc. .
  - **Task management and monitoring**: The kernel can provide functions for tasks to query and modify their own or other tasks' attributes, such as status, priority, stack usage, etc. The kernel can also detect and handle task errors, such as deadlock, overflow, etc. .
  - **Interrupt handling and timing services**: The kernel can handle hardware and software interrupts, and provide services for tasks to measure and control time, such as timers, delays, timeouts, etc. .