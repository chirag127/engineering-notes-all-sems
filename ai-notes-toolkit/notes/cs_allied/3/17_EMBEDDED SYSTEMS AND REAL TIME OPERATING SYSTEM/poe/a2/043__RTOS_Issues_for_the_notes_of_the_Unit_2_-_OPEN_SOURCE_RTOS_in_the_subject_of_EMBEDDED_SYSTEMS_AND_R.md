 Here is the content in markdown format without any emojis or external links:

### RTOS Issues for the notes of the Unit 2 - OPEN SOURCE RTOS

1. Priority Inversion: When a high priority task is waiting for a low priority task to release a resource, leading to delay in execution of high priority task. It can be avoided using priority inheritance protocol.
2. Deadlock: When two or more tasks are waiting for each other to release resources, leading to all the tasks being blocked indefinitely. It can be avoided using resource allocation graphs and resource hierarchy.
3. Starvation: When a task is not getting enough CPU cycles to execute and complete its function leading to indefinite postponement of its execution. It can be avoided using aging, resource reservation etc.
4. Thrashing: When the context switching overhead due to fully preemptive scheduler leads to most of the CPU time being spent in switching between tasks rather than actual execution of tasks. It can be reduced using less preemptive scheduling.
5. Scheduler activations: When a real time task becomes ready to execute but is not scheduled by the RTOS leading to deadline misses. It can be avoided using server activations by the tasks.

The content is written in points and in a formal tone without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content.