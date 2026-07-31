### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally. A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur .
- In a priority-driven approach, tasks are executed based on their priority level. Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two types: static and dynamic.
  - Static priority-driven scheduling assigns a fixed priority to each task at design time and does not change it during execution.
  - Dynamic priority-driven scheduling assigns a variable priority to each task at run time and may change it depending on the system state and events.
- Priority-driven scheduling can also be classified into two categories: preemptive and non-preemptive.
  - Preemptive priority-driven scheduling allows a higher-priority task to interrupt a lower-priority task that is currently executing and resume it later.
  - Non-preemptive priority-driven scheduling does not allow a higher-priority task to interrupt a lower-priority task that is currently executing and waits until it finishes.
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, a framework for developing robotic applications, by leveraging the priority inheritance and priority ceiling protocols to avoid priority inversion and deadlock problems.