 Here is the content in markdown format without any emojis or external links and in a formal tone:

## Unit 2 - Real Time Scheduling

1. Real-time systems: Systems where correct system response depends on not just producing correct outputs, but producing them within strict time constraints. Missing deadlines can lead to system failures.
2. Hard real-time systems: Missing deadlines is unacceptable. Examples: Flight control systems, industrial control systems.
3. Soft real-time systems: Missing occasional deadlines is tolerable. Examples: Multimedia systems.
4. Real-time scheduling: Algorithms to determine the order of execution of tasks to meet deadlines. Important metrics:
- Response time: Time taken to execute a task.
- Deadline: Latest time by which a task must complete.
- Period: Frequency with which a task repeats.
- Utilization: Ratio of total execution time of all tasks to the scheduler capacity. For hard real-time, should be < 100% to allow for worst-case scenarios.
5. Fixed priority preemptive scheduling: Each task assigned a unique priority. Higher priority tasks preempt lower priority tasks. Good for hard real-time as critical tasks get priority. Example: Rate monotonic scheduling.
6. Earliest deadline first: Prioritize tasks based on nearest deadline. Favors meeting deadlines of short tasks over long tasks. Suited for soft real-time.

The content covers the key points around real time scheduling in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.