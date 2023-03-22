 Here are the key points on Features of RTOS for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System:

### Features of RTOS

1. Preemptive scheduling: The RTOS allocates CPU time slices to tasks based on their priorities. It can preempt a lower priority task anytime and give CPU control to a higher priority task. This ensures timely completion of high priority tasks.
2. Fast context switching: The RTOS can save and restore the state of tasks very quickly allowing it to switch between multiple tasks efficiently. This enables it to meet tight deadlines.
3. Determinism: The behavior and timing of an RTOS are highly predictable. It does not suffer from unexpected delays or latencies allowing real-time applications to function correctly.
4. Priority based execution: The RTOS executes tasks based on assigned priorities. Higher priority tasks get preference over lower priority tasks in allocation of CPU time slices. This enables important tasks to be completed on time.
5. Multitasking: The RTOS supports concurrent execution of multiple tasks giving the impression that they are executing simultaneously. This allows efficient utilization of CPU time and achieving parallelism.
6. Memory management: The RTOS provides memory partitioning and protection features to prevent tasks from corrupting each other's memory spaces and ensure predictable performance.
7. Inter-task communication: The RTOS provides mechanisms like message passing and semaphores for tasks to communicate and synchronize with each other. This enables modular design of real-time systems.
8. Time management: The RTOS provides features like delay, sleep, timeout, alarm, etc. to schedule tasks at specific times or after specific time intervals. This is essential for time critical real-time systems.

The above points cover the key features of a Real-Time Operating System that enable it to handle concurrent tasks with strict time constraints in a predictable and efficient manner.