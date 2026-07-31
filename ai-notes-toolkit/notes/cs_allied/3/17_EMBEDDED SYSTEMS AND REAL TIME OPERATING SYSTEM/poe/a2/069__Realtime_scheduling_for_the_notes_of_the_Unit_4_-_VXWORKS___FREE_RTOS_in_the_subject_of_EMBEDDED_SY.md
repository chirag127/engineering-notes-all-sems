 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Realtime scheduling for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

1. Real-time systems: Systems where the correctness of the system depends not only on the logical correctness of the outputs but also on the time at which the outputs are produced.
2. Hard real-time systems: Missing a deadline leads to a system failure. Examples: Aircraft control systems, Industrial control systems.
3. Soft real-time systems: Missing a deadline leads to degradation in performance but not a catastrophic failure. Examples: Multimedia systems.
4. Scheduling: The order in which the processes/tasks are executed by the processor.
5. Scheduling criteria:
- Throughput - Number of processes completed per unit time
- Turnaround time - Time between submission and completion of a process
- Waiting time - Time a process waits in the ready queue
- Latency - Time elapsed between an event and the start of the corresponding process. Important for hard real-time systems.
6. Scheduling algorithms:
- First Come First Served (FCFS)
- Shortest Job First (SJF)
- Priority based scheduling
- Round Robin (RR)
- Earliest Deadline First (EDF) - Optimal for hard real-time systems with deadlines
7. Dispatch latency: Time taken by the scheduler to stop one process and start another process. Should be very small for real-time systems.
8. Resources: CPU, Memory, I/O devices. Resource utilization should be optimum and resources should be allocated based on priorities in real-time systems.
9. Scheduling in VxWorks and FreeRTOS (Popular real-time operating systems). Explain their scheduling frameworks and algorithms.