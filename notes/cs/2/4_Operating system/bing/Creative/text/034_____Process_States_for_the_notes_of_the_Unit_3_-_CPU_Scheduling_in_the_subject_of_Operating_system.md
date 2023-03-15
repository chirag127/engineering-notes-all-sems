### Process States

- A process is a program in execution that requires resources such as CPU, memory, disk, and I/O devices.
- A process state is a condition of the process at a specific instant of time. 
- A process can be in one of the following states:    
  - New: The process is being created but not yet loaded into the main memory. It is the program that is present in the secondary memory that will be picked up by the OS to create the process. 
  - Ready: The process is loaded into the main memory and is waiting for the CPU to be allocated. The process is placed in the ready queue, which is a data structure that holds all the ready processes.   
  - Running: The process is selected by the CPU scheduler and is executing on the CPU. The process can run in either user mode or kernel mode, depending on the type of instructions it is executing.   
  - Waiting: The process is blocked and cannot run until some event occurs, such as an I/O completion, a signal, or a timer expiration. The process is placed in the waiting queue, which is a data structure that holds all the blocked processes.   
  - Terminated: The process has completed its execution and is removed from the system. The process releases all the resources it was using and returns the exit status to its parent process.   
- A process can change its state due to various events, such as:   
  - Admission: The OS creates a new process and moves it from the new state to the ready state.  
  - Dispatch: The CPU scheduler selects a process from the ready queue and moves it from the ready state to the running state.   
  - Interrupt: The CPU is preempted by a higher-priority process or by a timer, and the current process is moved from the running state to the ready state.   
  - I/O or event wait: The process requests an I/O operation or waits for an event, and the process is moved from the running state to the waiting state.   
  - I/O or event completion: The I/O operation or the event is completed, and the process is moved from the waiting state to the ready state.   
  - Exit: The process finishes its execution and is moved from the running state to the terminated state.   
- A process is represented in the operating system by a process control block (PCB), which is also called a task control block. The PCB contains all the information about the process, such as:   
  - Process ID: A unique identifier for the process.
  - Process state: The current state of the process.
  - Program counter: The address of the next instruction to be executed by the process.
  - CPU registers: The values of the CPU registers used by the process.
  - CPU scheduling information: The priority, quantum, and other parameters used by the CPU scheduler for the process.
  - Memory management information: The base and limit addresses, page tables, and other information used by the memory manager for the process.
  - Accounting information: The CPU time, I/O time, and other statistics used for accounting and performance monitoring of the process.
  - I/O status information: The list of I/O devices, files, and other resources allocated to the process.
  - Interprocess communication information: The signals, messages, pipes, and other mechanisms used for communication and synchronization with other processes.
- The PCB is created and maintained by the OS for each process. The PCB is updated whenever the process changes its state or performs any operation. The PCB is deleted when the process is terminated.   

: https://