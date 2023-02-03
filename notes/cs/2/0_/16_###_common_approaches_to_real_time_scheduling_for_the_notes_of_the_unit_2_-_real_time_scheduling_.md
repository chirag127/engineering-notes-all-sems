### Common Approaches to Real Time Scheduling for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

1. Rate Monotonic Scheduling (RMS): assigns priority based on the period of a task, with shorter periods having higher priority. 

2. Earliest Deadline First (EDF): assigns priority based on the closest deadline of a task. 

3. Least Laxity First (LLF): assigns priority based on the difference between a task's deadline and its expected completion time. 

4. Hybrid Scheduling: combines aspects of multiple scheduling algorithms to balance various factors such as responsiveness and resource utilization. 

5. Priority Inheritance: temporarily boosts the priority of a task when it holds a resource required by a higher priority task. 

6. Priority Ceiling: assigns a ceiling priority to each resource, with tasks requesting that resource executing at the ceiling priority. 

7. Global EDF: schedules tasks across multiple processors, taking into account the deadlines of tasks on all processors. 

8. Partitioned Scheduling: divides tasks into groups and assigns each group to a separate processor, with scheduling algorithms applied within each group.
