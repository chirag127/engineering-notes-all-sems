 Here is the content in markdown format for the topic - 
### Reference Models for Real Time Systems

The following are the reference models commonly used for Real Time Systems:

1. Rate Monotonic Model:
- Tasks are scheduled based on their period (task with shorter period has higher priority)
- Utilizes static priority scheduling
- Works well for periodic tasks with constrained deadlines
- Suffers from priority inversion

2. Earliest Deadline First Model:
- Tasks are scheduled based on their deadline (task with earliest deadline has highest priority)
- Dynamic priority scheduling
- Handles aperiodic tasks well along with periodic tasks
- Requires more overhead for scheduling

3. Priority Ceiling Protocol:
- Associates a priority ceiling with each shared resource
- Prevents priority inversion by blocking lower priority tasks if they try to access a shared resource currently used by a higher priority task
- Additional complexity of managing priority ceilings

4. Sporadic Server Model:
- Reserves CPU bandwidth for handling aperiodic tasks
- Periodic tasks are scheduled using RMS/EDF
- Aperiodic tasks are scheduled using bandwidth left over by periodic tasks
- Handles mixed workloads of periodic and aperiodic tasks
- Difficult to determine optimal bandwidth reservation for sporadic server

Advantages and disadvantages of each model can be discussed in detail. Examples and applications of the models in real time systems can also be included. Detailed ASCII diagrams showing scheduling of tasks as per different models may also be added to make the concepts more understandable. The content can be extended with more details and points as required for the notes.