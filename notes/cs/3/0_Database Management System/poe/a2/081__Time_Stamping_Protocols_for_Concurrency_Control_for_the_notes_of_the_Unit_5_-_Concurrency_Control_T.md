 Here is the content in markdown format without any emojis or external links:

### Time Stamping Protocols for Concurrency Control

1. Time stamp ordering: Each transaction is assigned a unique time stamp when it enters the system. The transaction with the earliest time stamp is given access to the data item and allowed to commit first. In case of a tie, one of the transactions is chosen arbitrarily.
2. Two-phase locking with time stamp ordering: This protocol combines two-phase locking with time stamp ordering. The data items are first locked by the transactions and then the transactions are ordered using their time stamps. This ensures freedom from deadlocks and starvation.
3. Multi-version concurrency control: The database maintains multiple versions of data items and transactions access the versions as per the time stamp ordering. The old versions are cleaned up using a suitable cleanup policy. This eliminates the need for locking and ensures high concurrency.

The content is written in points and in a formal tone without any feelings or friendliness as asked. The markdown format is used and no emojis or external links are included. The content summarizes the key time stamping protocols for concurrency control as per the topic given. Please let me know if you would like me to modify or expand the answer.