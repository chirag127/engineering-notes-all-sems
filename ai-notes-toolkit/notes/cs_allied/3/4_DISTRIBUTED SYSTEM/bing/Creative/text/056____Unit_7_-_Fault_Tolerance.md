## Unit 7 - Fault Tolerance

- Fault tolerance is the property that enables a system to continue operating properly in the event of the failure of one or more faults within some of its components.
- The objective of creating a fault-tolerant system is to prevent disruptions arising from a single point of failure, ensuring the high availability and business continuity of the system.
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, backup, recovery, error detection and correction, etc.
- Fault tolerance can be classified into different levels, such as:
  - Active fault tolerance: The system detects and corrects faults without interrupting the normal operation.
  - Passive fault tolerance: The system switches to a backup or standby mode when a fault occurs, and resumes the normal operation after the fault is repaired or isolated.
  - Graceful degradation: The system reduces its functionality or performance in the presence of faults, but maintains the essential services.
  - Fail-safe: The system shuts down or enters a safe state when a fault occurs, to prevent further damage or harm.
- Fault tolerance can be applied to different aspects of a system, such as:
  - Hardware fault tolerance: The system uses redundant or resilient hardware components, such as processors, memory, disks, power supplies, etc., to tolerate hardware failures.
  - Software fault tolerance: The system uses redundant or resilient software components, such as processes, threads, modules, etc., to tolerate software failures.
  - Data fault tolerance: The system uses redundant or resilient data structures, such as databases, files, caches, etc., to tolerate data corruption or loss.
  - Network fault tolerance: The system uses redundant or resilient network components, such as routers, switches, links, etc., to tolerate network failures.
  - Human fault tolerance: The system uses redundant or resilient human operators, such as administrators, users, etc., to tolerate human errors or malicious actions.