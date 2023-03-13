### Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- For a system to have this property, many separate issues are involved:
  - Fault confinement: the ability to isolate and contain the effects of a fault within a limited region of the system.
  - Fault detection: the ability to identify and report the occurrence of a fault.
  - Fault masking: the ability to hide the existence of a fault from the rest of the system and the users.
  - Retry: the ability to repeat a failed operation or request until it succeeds.
  - Diagnosis: the ability to determine the cause and location of a fault.
  - Reconfiguration: the ability to change the structure or behavior of the system to cope with a fault.
  - Recovery: the ability to restore the system to a consistent and correct state after a fault.
  - Restart: the ability to restart the system or a part of it from a known initial state after a fault.
  - Repair: the ability to fix or replace the faulty component or resource.
  - Reintegration: the ability to reintegrate the repaired component or resource into the system without disrupting its operation.
- Fault tolerance is a main subject regarding the design of distributed systems. When a hardware or software failure occurs in the system, it causes a failure and we call it, in this case, a fault.
- Fault tolerance in distributed systems can be achieved by using various techniques, such as redundancy, replication, checkpointing, rollback, logging, message passing, consensus, etc.
- Fault tolerance in distributed systems can be classified into two categories:
  - Static fault tolerance: the system is designed to tolerate a fixed number of faults, and the system configuration does not change during the execution.
  - Dynamic fault tolerance: the system is designed to tolerate a variable number of faults, and the system configuration can change during the execution.
- Fault tolerance in distributed systems can be evaluated by using various metrics, such as reliability, availability, dependability, resilience, etc.