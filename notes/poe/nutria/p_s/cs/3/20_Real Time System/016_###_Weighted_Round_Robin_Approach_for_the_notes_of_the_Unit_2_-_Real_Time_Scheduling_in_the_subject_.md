
### Weighted Round Robin Approach
Weighted Round Robin (WRR) is a scheduling algorithm used in real-time systems. It is an extension of the Round Robin algorithm, where each process is assigned a relative weight based on its priority. The scheduler then allocates a time slice proportional to the weight assigned to each process. 

**Advantages** 
- WRR is a simple and efficient scheduling algorithm, as it requires minimal overhead for the scheduler. 
- It is also fair, as each process is allocated a time slice proportional to its weight. 
- WRR is also dynamic, as the weights assigned to each process can be changed during runtime.

**Disadvantages**
- WRR may not be suitable for systems with a large number of processes, as the scheduler has to keep track of the weights assigned to each process.
- WRR may also suffer from starvation, as processes with lower priority may not get enough time to complete their tasks.

**Examples** 
- WRR can be used in real-time systems where the tasks have different priorities, such as in a multimedia system. 
- WRR can also be used in embedded systems, where tasks have to be completed in a certain time frame.

**Applications** 
- WRR can be used in embedded systems, such as in car navigation systems, where tasks have to be completed in a certain time frame. 
- WRR can also be used in multimedia systems, where tasks have different priorities. 
- WRR can also be used in real-time operating systems, such as Linux, where tasks have to be completed in a certain time frame.