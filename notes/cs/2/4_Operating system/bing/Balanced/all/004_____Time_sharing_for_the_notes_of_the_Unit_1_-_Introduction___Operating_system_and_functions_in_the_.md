# Time Sharing Operating System

- A time sharing operating system is a type of operating system that allows multiple users to share the same computer simultaneously .
- Each user gets a small slice of the CPU time, called a time quantum, to execute their program. The CPU switches between the users' programs so fast that it creates an illusion of parallel execution.
- A time sharing operating system uses multiprogramming and multitasking techniques to manage the multiple users and programs in the memory.
- A time sharing operating system has three main states for the users' programs: active, ready, and waiting.
  - Active state: The user's program is under the control of the CPU. Only one program can be in this state at a time.
  - Ready state: The user's program is ready to execute but it is waiting for its turn to get the CPU. More than one user can be in the ready state at a time.
  - Waiting state: The user's program is waiting for some input/output operation. More than one user can be in the waiting state at a time.
- A time sharing operating system has some advantages and disadvantages over other types of operating systems.
  - Advantages:
    - It makes more efficient use of the CPU time and resources.
    - It allows multiple users to interact with the same computer and share data and programs.
    - It provides faster response time and feedback to the users.
    - It improves the reliability and security of the system by isolating the users and programs from each other.
  - Disadvantages:
    - It requires more complex hardware and software to support the multiple users and programs.
    - It increases the overhead and cost of the system due to the frequent context switching and scheduling.
    - It may cause performance degradation and resource contention if the number of users and programs exceeds the capacity of the system.
    - It may compromise the privacy and confidentiality of the users and programs if the system is not properly secured.