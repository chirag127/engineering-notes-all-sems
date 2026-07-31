
### Basic Priority-Inheritance and Priority-Ceiling Protocols

1. Priority-Inheritance Protocol (PIP): This protocol is used to prevent priority inversion in real-time systems. It is used to ensure that a low-priority task does not prevent a higher-priority task from executing. When a task is blocked, the priority of the blocking task is raised to the priority of the blocked task. This ensures that the higher-priority task is no longer blocked and can execute.

2. Priority-Ceiling Protocol (PCP): This protocol is used to prevent priority inversion in real-time systems. It is used to ensure that a low-priority task does not prevent a higher-priority task from executing. When a task is blocked, the priority of the blocking task is raised to the ceiling priority of the resource that the task is trying to access. This ensures that the higher-priority task is no longer blocked and can execute.

3. Priority inheritance and priority ceilings protocols are used to ensure that tasks with higher priority can execute without being blocked by tasks with lower priority. In addition, these protocols also help to prevent priority inversion, which can occur when a low-priority task blocks a higher-priority task from executing.