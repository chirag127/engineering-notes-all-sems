 Here is the content written in markdown format:

## Unit 2 - Real Time Scheduling

Real-time scheduling refers to the scheduling of tasks that have strict time constraints. These tasks must be completed within a certain deadline otherwise the system fails.

- Tasks are characterized by their period (how often they occur) and deadline (latest time by which they must complete).
- CPU utilization must be kept high while ensuring all deadlines are met. This is called utility optimal scheduling.
- Common real-time scheduling algorithms:

1. Rate Monotonic Scheduling (RMS): Assigns priorities based on task periods. Shorter periods get higher priority. Simple but does not maximize CPU utilization.

2. Deadline Monotonic Scheduling (DMS): Assigns priorities based on deadlines. Shorter deadlines get higher priority. Also simple but can cause some tasks to miss deadlines even if CPU is not fully utilized.

3. Earliest Deadline First (EDF): Highest priority given to task with earliest deadline. Maximizes CPU utilization but determining feasibility of schedule is NP-hard.

- Examples: Robot control, aircraft control systems, medical monitoring systems, etc. Require fast and consistent response times.
- Challenges: Dealing with unpredictable delays, ensuring all tasks meet deadlines, scheduling overhead should be small.

[Detailed diagrams and examples can be added here to aid learning]

Advantages: Critical tasks are given priority to meet deadlines. Maximizes number of deadlines met.
Disadvantages: Complex to determine feasibility of schedule. Overhead for assigning and reassigning priorities.

Applications: Missile tracking, computer numerically controlled machines, telecommunications switching systems, etc.