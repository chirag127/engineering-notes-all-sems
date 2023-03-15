 Here is the content in markdown format:

### Dynamic voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Dynamic voting protocols are used to mask faults and ensure consistency in replicated databases. They work on the principle of majority voting.
- The key types of dynamic voting protocols are:
	- Quorum consensus: A read/write quorum (subset of servers) is chosen dynamically. The request is processed if the quorum agrees. This ensures high availability but can lead to conflicting writes.
	- Primary-backup: One server (primary) handles writes. Backups mirror the primary and can handle reads. If the primary fails, one backup is elected as the new primary. This avoids conflicting writes but can lead to short periods of unavailability during primary failure and election.
	- Leader election: Servers elect a leader dynamically. The leader handles all requests. If the leader fails, a new leader is elected. This also avoids conflicting writes but can lead to unavailability.
- Advantages: High availability, fault tolerance.
- Disadvantages: Additional overheads of monitoring servers and electing leaders/primaries, possibility of temporary conflicts or unavailability.
- Applications: Replicated, highly available databases.

Here are some mnemonics and tips to remember:

- Think of a quorum as a majority committee. A quorum consensus protocol gets things done if the majority agrees.
- Imagine leaders emerging in a group of people. The leader handles all the work until they are unable to, and then a new leader emerges. This maps to the leader election protocol.
- The primary-backup protocol is like a manager-employee relationship. The manager (primary) handles all the work and the employees (backups) mirror the manager, with one employee temporarily taking over if the manager is unavailable.

Does this help? Let me know if you would like me to elaborate on any part of the content or modify/add anything.