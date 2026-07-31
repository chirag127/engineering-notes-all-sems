### Process identification information for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- Each process in an operating system is assigned a unique identifier known as the **Process ID (PID)**.
- The PID is used by the operating system to track and manage the process.
- The operating system maintains a table known as the **Process Table** which contains information about all the processes in the system.
- The Process Table contains information such as the PID, process state, priority, and other information required for scheduling and managing the process.
- When a new process is created, the operating system assigns it a unique PID and adds an entry for the process in the Process Table.
- The PID is used by the operating system and other system utilities to reference and manipulate the process.
- The PID is also used by the user to interact with the process, for example, to send signals to the process or to terminate it.
- In addition to the PID, processes may also have other identification information such as the **Parent Process ID (PPID)** which identifies the process that created the process.
- The PPID is used by the operating system to maintain the process hierarchy and to manage the relationship between parent and child processes.
- Processes may also have other identification information such as the **User ID (UID)** and **Group ID (GID)** which identify the user and group that own the process.
- The UID and GID are used by the operating system to enforce access control and to determine the privileges of the process.