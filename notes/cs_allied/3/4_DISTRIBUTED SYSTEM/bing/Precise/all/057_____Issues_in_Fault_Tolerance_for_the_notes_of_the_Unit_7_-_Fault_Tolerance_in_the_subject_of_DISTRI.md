# Issues in Fault Tolerance

Fault tolerance is the realization that we will have faults in our system (hardware and/or software) and we have to design the system in such a way that it will be tolerant of those faults. That is, it should compensate for the faults and continue to function.

Some of the issues in fault tolerance are:

1. **Partial failure**: A major difference between distributed systems and single machine systems is that with the former, partial failure is possible, i.e., when one component in a distributed system fails.
2. **Process resilience**: Techniques by which one or more processes can fail without seriously disturbing the rest of the system.
3. **Reliable multicasting**: To keep processes synchronized by which message transmission to a collection of processes is guaranteed to succeed.
4. **Error containment**: Fault tolerance consists of noticing active faults and component subsystem failures, and doing something helpful in response. One such helpful response is error containment, which is another close relative of modularity and the building of systems out of subsystems.
5. **Cost**: A fault tolerant system can be costly, as it requires the continuous operation and maintenance of additional, redundant components.
