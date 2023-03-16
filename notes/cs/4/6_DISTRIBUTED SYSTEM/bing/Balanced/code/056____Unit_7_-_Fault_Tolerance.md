## Unit 7 - Fault Tolerance

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.
- Fault tolerance can be classified into two types: hardware fault tolerance and software fault tolerance.
- Hardware fault tolerance is the ability of a system to tolerate failures of physical components, such as processors, memory, disks, or network devices.
- Hardware fault tolerance can be achieved by using techniques such as:
  - Static redundancy: using multiple identical components that perform the same function in parallel, and selecting the correct output from a majority vote.
  - Dynamic redundancy: using spare components that can replace failed ones on the fly, and transferring the state and workload of the failed component to the spare one.
  - Error detection and correction: using mechanisms such as parity bits, checksums, or error-correcting codes to detect and correct errors in data transmission or storage.
- Software fault tolerance is the ability of a system to tolerate failures of software components, such as modules, processes, or threads.
- Software fault tolerance can be achieved by using techniques such as:
  - Exception handling: using mechanisms such as try-catch blocks, signals, or interrupts to handle errors or exceptions that occur during the execution of a program.
  - Checkpointing and rollback: using mechanisms such as logs, snapshots, or backups to save the state of a program at regular intervals, and restoring the state from the most recent checkpoint in case of a failure.
  - Process replication: using mechanisms such as forks, threads, or distributed systems to create multiple copies of a process that execute the same or similar tasks, and coordinating the results among them.
  - Rejuvenation: using mechanisms such as restarts, reboots, or garbage collection to refresh the state of a program or a system periodically, and prevent the accumulation of errors or resource leaks.