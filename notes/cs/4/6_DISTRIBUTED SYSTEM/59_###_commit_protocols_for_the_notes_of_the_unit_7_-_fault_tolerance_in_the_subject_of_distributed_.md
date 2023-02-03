### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM
Commit protocols ensure that transactions in a distributed system are executed atomically and consistently. They are used to maintain data integrity in the event of failures.

Two common commit protocols are 2PC (Two-Phase Commit) and 3PC (Three-Phase Commit).

2PC:
1. Coordinator sends a "prepare to commit" message to all participants.
2. Participants respond with either "commit" or "abort".
3. Coordinator sends a "commit" or "abort" message to all participants based on the responses.

3PC:
1. Coordinator sends a "prepare to commit" message to all participants.
2. Participants respond with either "ready to commit" or "abort".
3. Coordinator sends a "commit" or "abort" message to all participants based on the responses.
4. Participants send an "ack" message to the coordinator.
