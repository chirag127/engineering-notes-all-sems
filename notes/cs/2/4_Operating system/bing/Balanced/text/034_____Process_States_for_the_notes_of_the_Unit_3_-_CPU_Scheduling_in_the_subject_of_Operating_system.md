### Process States

- A process is a program in execution that requires resources such as CPU, memory, disk, and I/O devices.
- A process state is a condition of the process at a specific instant of time.
- Every process is represented in the operating system by a process control block (PCB), which contains information such as process ID, priority, CPU registers, memory pointers, etc.
- A process can be in one of the following states:

  - **New**: The process is being created but not yet loaded into the main memory. It is the program that is present in the secondary memory that will be picked up by the OS to create the process .
  - **Ready**: The process is loaded into the main memory and is waiting for the CPU to be allocated. It is placed in the ready queue, which is a data structure that holds all the ready processes .
  - **Running**: The process is chosen for execution and is running on one of the CPUs or cores of the system. There can be at most one running process per CPU or core. A process can run in either user mode or kernel mode, depending on the type of instructions it is executing .
  - **Waiting**: The process is waiting for some event to occur, such as an I/O operation, a signal, or a resource availability. It is placed in the waiting queue, which is a data structure that holds all the waiting processes .
  - **Terminated**: The process has completed its execution and is removed from the system. The OS releases the resources allocated to the process and updates the PCB .

- A process can change its state due to various events, such as CPU scheduling, I/O interrupts, signals, system calls, etc. The following diagram shows the possible state transitions of a process :

![Process State Diagram](https://media.geeksforgeeks.org/wp-content/uploads/Process-State-Diagram.png)

- Different operating systems may have different names or additional states for the processes, such as suspended, zombie, or blocked. However, the basic states and transitions are similar in most operating systems.