### Scheduling Systems

Scheduling in real-time operating systems (RTOS) is the process of deciding which task to execute next based on their priority and other constraints. In this unit, we will discuss the different scheduling systems used in open-source RTOS.

#### 1. Preemptive Scheduling

Preemptive scheduling is a scheduling system in which the highest-priority task is executed first, and the lower-priority tasks are interrupted when a higher-priority task becomes ready to run. This scheduling system ensures that the most important tasks are executed first, and it is commonly used in real-time systems.

#### 2. Round Robin Scheduling

Round Robin Scheduling is a scheduling system in which each task is executed for a fixed amount of time, usually called a time slice or quantum. Once the time slice has elapsed, the task is preempted and the next task in the queue is executed. This scheduling system ensures that each task gets a fair share of the CPU time.

#### 3. Priority Inheritance Scheduling

Priority Inheritance Scheduling is a scheduling system in which the priority of a task is temporarily increased to prevent priority inversion. Priority inversion occurs when a low-priority task holds a resource that a higher-priority task needs to complete its execution. In this case, the low-priority task is temporarily given a higher priority to ensure that the high-priority task can access the resource and complete its execution.

#### 4. Earliest Deadline First Scheduling

Earliest Deadline First Scheduling is a scheduling system in which the task with the earliest deadline is executed first. This scheduling system is commonly used in soft real-time systems, where the deadlines are not hard but have to be met as soon as possible.

#### 5. Rate Monotonic Scheduling

Rate Monotonic Scheduling is a scheduling system in which the task with the shortest period or highest frequency is given the highest priority. This scheduling system is commonly used in hard real-time systems, where the deadlines are hard and must be met.

In conclusion, open-source RTOS uses different scheduling systems to manage the execution of tasks. The choice of scheduling system depends on the application requirements and the constraints of the system. Understanding the different scheduling systems is crucial for designing and developing real-time systems.