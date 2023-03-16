### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur.
- In a priority-driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two categories: static and dynamic.
- Static priority-driven scheduling assigns a fixed priority to each task at design time and does not change it during execution.
- Dynamic priority-driven scheduling assigns a variable priority to each task at run time and may change it depending on the system state.
- Priority-driven scheduling can improve the real-time performance and predictability of dynamic real-time systems with a mix of time-based and event-based activities, where the system must adapt to changing conditions and events .
- Priority-driven scheduling can also support different types of real-time tasks, such as periodic, sporadic, aperiodic, and mixed tasks.
- Priority-driven scheduling can be implemented using different algorithms, such as rate-monotonic, earliest deadline first, least laxity first, etc.
- Priority-driven scheduling can be applied to different types of resources, such as processors, communication channels, memory, etc.
- Priority-driven scheduling can be combined with other techniques, such as resource reservation, admission control, overload handling, etc.
- Priority-driven scheduling can be integrated with different frameworks, such as ROS 2, to enable real-time applications in robotics, autonomous vehicles, etc.