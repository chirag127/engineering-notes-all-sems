### Priority Driven Approach

Priority driven approach is a scheduling method used in real-time systems. In this approach, tasks are assigned priorities based on their importance and urgency. The scheduler then selects the highest priority task to execute at any given time.

Some key points to note about priority driven approach are:

1. Priorities can be assigned statically or dynamically. Static priorities are assigned at design time and do not change during the execution of the system. Dynamic priorities, on the other hand, can change during the execution of the system based on various factors such as deadlines, resource availability, etc.

2. Priority driven approach can be preemptive or non-preemptive. In preemptive scheduling, a higher priority task can interrupt the execution of a lower priority task. In non-preemptive scheduling, a task once started, must run to completion before another task can be scheduled.

3. Priority inversion is a problem that can occur in priority driven approach. It happens when a low priority task holds a resource that is required by a higher priority task. This can cause the higher priority task to be blocked and miss its deadline.

4. Priority inheritance and priority ceiling protocols are two methods used to solve the priority inversion problem.

5. Priority driven approach is widely used in real-time systems due to its simplicity and effectiveness in meeting deadlines.
