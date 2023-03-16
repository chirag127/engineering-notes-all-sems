# Unit 2 - Real Time Scheduling

- Real time scheduling is the process of allocating CPU time to tasks that have strict timing constraints and deadlines.
- Real time scheduling aims to ensure that tasks are completed within their deadlines, without compromising the quality of service or the system performance.
- Real time scheduling can be classified into two categories: hard real time and soft real time.
  - Hard real time scheduling requires that tasks meet their deadlines without any exceptions. Missing a deadline can result in catastrophic consequences for the system or the environment. Examples of hard real time systems are nuclear reactors, air traffic control, and pacemakers.
  - Soft real time scheduling allows some tasks to miss their deadlines occasionally, as long as the system can recover from the delay. Missing a deadline can result in degraded performance or quality of service, but not in fatal errors. Examples of soft real time systems are multimedia applications, online gaming, and voice over IP.
- Real time scheduling can also be classified into two types: static and dynamic.
  - Static real time scheduling assigns priorities to tasks before the system starts running, and does not change them during the execution. Static scheduling is simpler and faster, but less flexible and adaptable to changing conditions. Examples of static scheduling algorithms are rate monotonic, deadline monotonic, and earliest deadline first.
  - Dynamic real time scheduling assigns priorities to tasks at run time, based on their current state and the system conditions. Dynamic scheduling is more complex and slower, but more flexible and adaptable to changing conditions. Examples of dynamic scheduling algorithms are least laxity first, least slack time, and earliest deadline first with deadline inheritance.
- Real time scheduling involves the following components:
  - Tasks: the units of work that need to be executed by the system. Tasks can be periodic, aperiodic, or sporadic, depending on their arrival pattern and frequency.
  - Scheduler: the component that decides which task to execute next, based on their priorities and deadlines. The scheduler can be preemptive or non-preemptive, depending on whether it can interrupt a running task or not.
  - Clock: the component that provides the time reference for the system and the tasks. The clock can be internal or external, depending on whether it is synchronized with the environment or not.
  - Processor: the hardware element that executes the tasks. The processor can be single or multiple, depending on whether the system has one or more CPUs.