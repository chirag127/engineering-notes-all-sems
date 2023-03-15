### Prevention for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is the process of deciding which process will own the CPU to use while another process is suspended.
- CPU scheduling algorithms are the methods of choosing the next process to run on the CPU based on some criteria, such as priority, burst time, arrival time, etc.
- CPU scheduling algorithms can be classified into two modes: pre-emptive and non-pre-emptive.
  - Pre-emptive scheduling allows the CPU to switch from one process to another before the current process finishes its execution.
  - Non-pre-emptive scheduling does not allow the CPU to switch from one process to another until the current process finishes its execution.
- CPU scheduling algorithms can face some challenges, such as starvation, aging, and deadlock  .
  - Starvation is a phenomenon in which a low-priority process can wait indefinitely for the CPU because of a steady stream of higher-priority processes .
  - Aging is a technique to prevent starvation by gradually increasing the priority of a waiting process over time .
  - Deadlock is a situation in which a set of processes are blocked because each process is holding a resource and waiting for another resource held by another process.
- CPU scheduling algorithms can prevent these challenges by following some principles, such as:
  - Eliminating mutual exclusion, which means allowing multiple processes to share the same resource at the same time.
  - Eliminating hold and wait, which means requiring a process to request all the resources it needs at once and releasing them when done.
  - Eliminating circular wait, which means imposing a total order on the resources and requiring a process to request them in that order.
  - Eliminating no preemption, which means allowing the system to take away a resource from a process if another process needs it more urgently.