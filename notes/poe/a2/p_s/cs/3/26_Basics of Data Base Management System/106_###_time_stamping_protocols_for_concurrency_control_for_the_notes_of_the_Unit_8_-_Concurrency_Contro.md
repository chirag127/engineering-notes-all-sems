 Here is the content in markdown format for the given topic:

### Time Stamping Protocols for Concurrency Control

Time stamping protocols use the time of transaction execution to ensure serializability and avoid conflicts between concurrent transactions. The basic idea is to assign a unique time stamp to each transaction when it starts execution. The transaction with the earlier time stamp is given priority in case of any conflict. The popular time stamping protocols are:

1. Timestamp Ordering Protocol: This protocol orders the transactions in the increasing order of their time stamps. If two transactions conflict, the one with the earlier time stamp is executed first while the other is aborted. For example, if T1(ts1) and T2(ts2) conflict and ts1 < ts2, then T1 is executed and T2 is aborted.

Advantages: Simple to implement. Ensures freedom from cascading aborts.
Disadvantages: May lead to starvation, i.e. a transaction may have to wait indefinitely for its turn.

2. Timestamp Based Commitment: In this protocol, for commit timestamp is assigned to each transaction after execution. The transactions are committed in the increasing order of their commit time stamps. After commit timestamp assignment, the commit operation of a transaction takes place only if commit time stamps of all transactions that it read are smaller than its own commit time stamp. This prevents read-write conflicts as well as write-write conflicts.

Advantages: Avoids starvation and cascading aborts.
Disadvantages: Complex to implement. Requires logging of read as well as write operations.

Diagrams and examples can be included to illustrate the working of the protocols. The advantages and disadvantages can be elaborated with suitable examples. Applications in different database systems can also be discussed. The content can be extended with more details and points as per the requirements.