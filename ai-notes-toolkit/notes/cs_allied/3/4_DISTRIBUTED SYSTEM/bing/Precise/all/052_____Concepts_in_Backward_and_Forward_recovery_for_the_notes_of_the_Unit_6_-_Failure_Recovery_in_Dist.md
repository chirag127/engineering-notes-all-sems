### Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- **Backward recovery** is a technique used to restore the system to a consistent state after a failure has occurred. This is done by undoing the changes made by the failed transaction and restoring the system to its previous state.

- **Forward recovery** is a technique used to restore the system to a consistent state after a failure has occurred by redoing the changes made by the failed transaction. This is done by applying the changes made by the failed transaction to the system again.

- Both backward and forward recovery techniques are used to ensure the consistency and reliability of the system in the event of a failure.

- Backward recovery is also known as **rollback recovery**. It is commonly used in database systems where transactions are used to ensure the consistency of the data.

- Forward recovery is also known as **rollforward recovery**. It is commonly used in systems where the data is continuously updated and the changes made by the failed transaction are still valid.

- The choice between backward and forward recovery depends on the nature of the system and the type of failure that has occurred. In some cases, a combination of both techniques may be used to ensure the consistency and reliability of the system.

- In distributed systems, failure recovery is more complex due to the presence of multiple nodes and the need for coordination between them. Techniques such as **checkpointing** and **message logging** may be used to facilitate failure recovery in distributed systems.

- Checkpointing involves periodically saving the state of the system to a stable storage so that it can be restored in the event of a failure. Message logging involves recording the messages exchanged between the nodes in the system so that they can be replayed to restore the system to a consistent state after a failure.

- Failure recovery is an important aspect of distributed systems and various techniques and protocols have been developed to ensure the consistency and reliability of these systems in the event of a failure. Backward and forward recovery are two such techniques that are commonly used in distributed systems.