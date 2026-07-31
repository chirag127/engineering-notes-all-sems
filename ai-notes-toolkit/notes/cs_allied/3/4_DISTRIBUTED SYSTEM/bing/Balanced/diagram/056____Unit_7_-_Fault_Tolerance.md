## Unit 7 - Fault Tolerance

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.
- Fault tolerance can be classified into two types: hardware fault tolerance and software fault tolerance.
- Hardware fault tolerance is the ability of a system to tolerate failures of physical components, such as processors, memory, disks, or network devices.
- Hardware fault tolerance can be achieved by using techniques such as:
  - RAID (Redundant Array of Independent Disks): a technique that uses multiple disks to store data in a way that improves performance and reliability.
  - N-modular redundancy: a technique that uses multiple identical components to perform the same function, and uses a voting mechanism to select the correct output.
  - Hot swapping: a technique that allows replacing a faulty component with a spare one without shutting down the system.
- Software fault tolerance is the ability of a system to tolerate failures of software components, such as processes, threads, or messages.
- Software fault tolerance can be achieved by using techniques such as:
  - Checkpointing and rollback: a technique that periodically saves the state of a process, and restores it to a previous state in case of a failure.
  - Exception handling: a technique that allows a process to detect and handle errors that occur during its execution, and resume normal operation or terminate gracefully.
  - Fault masking: a technique that hides the occurrence of a fault from the rest of the system, and provides a correct output despite the fault.
  - Fault injection: a technique that deliberately introduces faults into a system to test its fault tolerance and identify potential vulnerabilities.