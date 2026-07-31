### Process identification information

- Process identification information is a part of the process control block (PCB), which is a data structure used by the operating system to store all the information about a process.
- Process identification information includes a unique number called the process identifier (PID), which is used by the operating system to uniquely identify an active process .
- The PID is assigned by the operating system when a process is created and is usually an integer value that increments with each new process .
- The PID is used by the operating system and other programs to perform various operations on the process, such as terminating, suspending, resuming, signaling, or debugging .
- The PID is also used by the operating system to maintain the process table, which is a data structure that keeps track of all the processes in the system and their attributes.
- The PID is usually visible to the user through various tools, such as the Task Manager in Windows, the ps command in Unix, or the tasklist command in Windows command prompt.
- The PID is not a permanent or global identifier, as it is reused over time and can only identify a process during its lifetime. Therefore, it does not identify processes that are no longer running or processes on other machines .