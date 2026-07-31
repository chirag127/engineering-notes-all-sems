# Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling aims to achieve predictable and deterministic behavior of the system, and to avoid missing deadlines or violating timing constraints .
- Real time scheduling can be classified into two categories: **hard real time** and **soft real time** .
  - Hard real time scheduling requires that every task must meet its deadline, otherwise the system may fail or cause severe consequences .
  - Soft real time scheduling allows some tasks to miss their deadlines occasionally, without causing significant harm to the system or the user .
- Real time scheduling can also be classified into two types: **static** and **dynamic** .
  - Static real time scheduling assigns priorities and schedules to tasks before the system starts running, and does not change them during the execution .
  - Dynamic real time scheduling assigns priorities and schedules to tasks at run time, based on the current state and behavior of the system .
- Real time scheduling algorithms can be divided into two groups: **preemptive** and **non-preemptive** .
  - Preemptive real time scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently running, and resume it later when the higher priority task finishes or is blocked .
  - Non-preemptive real time scheduling does not allow a higher priority task to interrupt a lower priority task that is currently running, and waits until the lower priority task completes or yields .
- Some examples of real time scheduling algorithms are: **Rate Monotonic Scheduling (RMS)**, **Earliest Deadline First (EDF)**, **Least Laxity First (LLF)**, **Fixed Priority Scheduling (FPS)**, **Round Robin Scheduling (RRS)**, **Deadline Monotonic Scheduling (DMS)**, etc .
- Real time scheduling can be applied to various domains and applications, such as: **embedded systems**, **robotics**, **multimedia**, **industrial control**, **aerospace**, **medical devices**, **telecommunications**, etc  .
- Real time scheduling can be supported by various tools and platforms, such as: **real time operating systems (RTOS)**, **real time schedulers**, **real time programming languages**, **real time middleware**, **real time simulators**, **real time analyzers**, etc   .
- Real time scheduling can also be integrated with other techniques and methods, such as: **resource management**, **fault tolerance**, **quality of service (QoS)**, **energy efficiency**, **security**, **adaptation**, etc  .
- Real time scheduling is a challenging and active research area, with many open problems and opportunities for improvement and innovation  .