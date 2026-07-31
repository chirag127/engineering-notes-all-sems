### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally. A resource becomes idles only when job does not require the resource for execution .
- It is a event driven approach for job scheduling and scheduling decision are made only when release and completion of job occur.
- In a priority-driven approach, tasks are executed based on their priority level. Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two types: static priority and dynamic priority.
- Static priority means that the priority of each task is fixed and does not change during the execution. Examples of static priority algorithms are Rate Monotonic (RM) and Deadline Monotonic (DM).
- Dynamic priority means that the priority of each task can vary depending on the current state of the system. Examples of dynamic priority algorithms are Earliest Deadline First (EDF) and Least Laxity First (LLF).
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, which is a framework for developing robotic applications.
- ROS 2 can leverage the priority-driven scheduling approach to handle different types of real-time tasks, such as sensor data processing, control, and communication.
- However, priority-driven scheduling also faces some challenges in ROS 2, such as priority inversion, resource contention, and interference from non-real-time tasks.