 Here is the content in markdown format for the topic ### Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM:

## Issues in Fault Tolerance

- **Detection**: Faults must be detected, either externally by the user or client, or internally by the system itself. Detection can be expensive and difficult.
- **Diagnosis**: Determining what has gone wrong and/or what component(s) have failed. This could require monitoring multiple parameters simultaneously and performing complex analysis.
- **Confinement**: Isolating faulty components to limit damage. This is particularly challenging for software faults.
- **Recovery**: The system must make a transition from a faulty state to a fault-free state. This often requires replication or redundancy, and may involve checkpointing and rollback recovery.
- **Validation**: Checking that the recovery process was successful and the system is now fault-free. Additional faults could have been triggered by the recovery process itself.

Some potential approaches to addressing these issues:

- Heartbeat monitoring: Components periodically announce they are functioning to detect faults if messages stop
- Watchdog timers: Components monitor other components and detect faults if expected events don't occur within a set time
- Exception handling: Software detects and can attempt to recover from internal errors
- Checkpointing: Periodically saving state so that the system can roll back to a previous correct state after a fault
- Redundancy: Having multiple replicas of components so that others can take over if one fails
- Consensus protocols: Algorithms to ensure replicas agree on values/state, crucial for recovery

[Detailed diagrams and examples can be added here if required.]

The advantages of fault tolerance are availability and reliability, while disadvantages include increased complexity, cost, and performance overhead. Fault tolerance is important for safety-critical and mission-critical systems where failures cannot be tolerated.