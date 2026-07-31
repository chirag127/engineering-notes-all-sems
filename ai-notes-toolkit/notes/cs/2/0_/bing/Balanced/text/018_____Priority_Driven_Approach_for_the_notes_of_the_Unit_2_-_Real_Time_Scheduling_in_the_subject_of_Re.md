### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur .
- In a priority-driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two types: static and dynamic.
- Static priority-driven scheduling assigns a fixed priority to each task at design time and does not change it during execution.
- Dynamic priority-driven scheduling assigns a variable priority to each task at run time and may change it depending on the system state.
- Priority-driven scheduling can be applied to both periodic and aperiodic tasks.
- Periodic tasks have a fixed inter-arrival time and a fixed deadline.
- Aperiodic tasks have a variable inter-arrival time and a variable deadline.
- Priority-driven scheduling can also handle mixed-criticality tasks, which have different levels of importance and different requirements for timeliness.
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, which is a framework for developing robotic applications.
- ROS 2 uses a middleware layer that supports priority-driven scheduling and allows users to specify the priority of each task.