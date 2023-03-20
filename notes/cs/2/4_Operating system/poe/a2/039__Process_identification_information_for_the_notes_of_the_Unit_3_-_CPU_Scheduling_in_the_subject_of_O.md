 Here is the formal content in markdown format without any emojis or external links for the given topic:

### Process identification information for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

1. Process state: New, Ready, Running, Waiting, Terminated
- New: The process is being created
- Ready: The process is waiting to be assigned to a processor
- Running: Instructions are being executed
- Waiting: The process is waiting for some event to occur (such as I/O completion)
- Terminated: The process has finished execution

2. Process Control Block (PCB): Data structure containing information about a process
- Process state: New, Ready, Running, Waiting, Terminated
- Program Counter: Address of the next instruction to be executed
- CPU registers: Values of the CPU registers when the process was interrupted
- CPU-scheduling information:
    - Priority
    - Pointer to scheduling queue
    - Scheduling algorithm field
- Memory-management information:
    - Value of the base and limit registers
    - Page tables
- Accounting information:
    - Amount of CPU and real time used
    - Time limits
- I/O status information

3. Interprocess communication (IPC) mechanisms: Way for processes to exchange data and synchronize their execution
- Shared memory: Processes can access common regions of memory
- Message passing: Processes exchange messages through the kernel

[No emojis or external links included as instructed.]