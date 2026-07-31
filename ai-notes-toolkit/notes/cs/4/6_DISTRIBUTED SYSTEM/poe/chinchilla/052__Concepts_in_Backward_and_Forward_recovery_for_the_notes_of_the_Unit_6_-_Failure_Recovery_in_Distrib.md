### Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

In distributed systems, failure recovery is an essential aspect to ensure the system's reliability and availability. Backward and forward recovery are two techniques used for failure recovery in distributed systems. Let's understand these concepts in detail:

#### 1. Backward Recovery
- Backward recovery is a technique used to recover from a failure by restoring the system to a previous checkpoint.
- Checkpoints are created periodically in the system to capture the system's state at a particular time.
- In case of a failure, the system is rolled back to the last checkpoint and re-executes the operations from that point onwards.
- Backward recovery is useful when the system can restore its state quickly and efficiently.

#### 2. Forward Recovery
- Forward recovery is a technique used to recover from a failure by continuing the execution from the point of failure.
- In forward recovery, the system identifies the failed process and takes corrective actions to repair the system and continue its execution.
- This technique ensures that the system can continue to function even when some of its components fail.
- Forward recovery is useful when the system cannot restore its state quickly and efficiently.

#### 3. Comparison between Backward and Forward Recovery
- Backward recovery is a roll-back technique, while forward recovery is a roll-forward technique.
- Backward recovery requires the system to restore its state to a previous checkpoint, while forward recovery requires the system to continue its execution from the point of failure.
- Backward recovery is useful when the system can restore its state quickly and efficiently, while forward recovery is useful when the system cannot restore its state quickly and efficiently.

In conclusion, both backward and forward recovery techniques are essential for failure recovery in distributed systems. These techniques ensure that the system can recover from failures and continue to function without compromising its reliability and availability.