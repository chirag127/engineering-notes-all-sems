 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Basic Concepts in Real time Communication

1. Real-time: Data or information is delivered with consistent low latency. The time delay between the arrival of input data and the output is very small and predictable.
2. Soft real-time: The time constraints are probabilistic in nature. Meeting all deadlines is desirable but not mandatory. Few missed deadlines are tolerable. Eg: Video conferencing.
3. Hard real-time: The time constraints are mandatory. Missing a deadline is a complete failure. Eg: Aircraft control system.
4. Determinism: The behaviour is predictable and the output is determined by the input. The same input conditions will always lead to the same output conditions and time-dependent changes are strictly controlled.
5. Concurrency: Multiple tasks run simultaneously and compete for shared resources. Real-time systems are inherently concurrent systems.
6. Priority: A priority scheme is used to arbitrate among concurrent tasks. Higher priority tasks get preference over lower priority tasks.
7. Preemption: A higher priority task can preempt a lower priority task. The lower priority task is suspended and resumed later.
8. Resource sharing: Shared resources like CPU, memory, buses, etc. introduce non-determinism and make analysis and guarantee of timeliness challenging.
9. Scheduling: Scheduling is critical for ensuring timeliness and selects which task to execute among ready tasks based on priorities, deadlines, resource availability, etc.

The content covers the key basic concepts related to real-time communication in a formal tone with points and without any emojis or external links as per your instructions. Please let me know if you would like me to modify or expand the content in any way.