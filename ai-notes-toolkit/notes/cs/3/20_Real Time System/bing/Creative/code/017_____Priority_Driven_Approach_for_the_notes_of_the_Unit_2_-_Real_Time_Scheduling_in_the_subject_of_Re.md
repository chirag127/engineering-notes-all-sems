### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur .
- In a priority-driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two categories: static priority and dynamic priority.
- Static priority means that the priority of each task is fixed and does not change during the execution.
- Dynamic priority means that the priority of each task can vary depending on the system state and the task characteristics.
- Some examples of static priority algorithms are rate-monotonic scheduling (RMS) and deadline-monotonic scheduling (DMS).
- Some examples of dynamic priority algorithms are earliest deadline first (EDF) and least laxity first (LLF).
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, which is a framework for developing robotic applications.
- ROS 2 can leverage the priority-driven scheduling approach to handle different types of real-time tasks, such as sensor data processing, control, and communication.
- However, priority-driven scheduling also faces some challenges in ROS 2, such as priority inversion, priority inheritance, and priority ceiling.