## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.   
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.   
- A distributed transaction requires the following properties to ensure data consistency and reliability: atomicity, consistency, isolation, and durability (ACID).  
- Atomicity means that either all the operations in a distributed transaction are executed successfully, or none of them are. If any operation fails, the transaction manager should roll back the changes made by the other operations.  
- Consistency means that the distributed transaction preserves the integrity constraints and business rules of the data. The transaction manager should ensure that the data is in a valid state before and after the transaction.  
- Isolation means that the distributed transaction is executed independently from other concurrent transactions. The transaction manager should prevent interference and conflicts among the operations of different transactions.  
- Durability means that the effects of a distributed transaction are permanent and persistent, even in the case of failures. The transaction manager should ensure that the data is safely stored and replicated on the transactional resources.  
- A distributed transaction can be implemented using different protocols, such as two-phase commit (2PC), three-phase commit (3PC), or the saga pattern. Each protocol has its own advantages and disadvantages in terms of performance, availability, and fault tolerance.  
- Two-phase commit (2PC) is a protocol that involves two phases: prepare and commit. In the prepare phase, the transaction manager asks each transactional resource to vote on whether they are ready to commit or abort the transaction. In the commit phase, the transaction manager decides to commit or abort the transaction based on the votes, and informs each transactional resource to do the same.  
- Three-phase commit (3PC) is a protocol that involves three phases: prepare, pre-commit, and commit. In the prepare phase, the transaction manager asks each transactional resource to vote on whether they are ready to commit or abort the transaction. In the pre-commit phase, the transaction manager decides to commit or abort the transaction based on the votes, and informs each transactional resource to do the same. In the commit phase, the transaction manager confirms the commit decision to each transactional resource, and asks them to finalize the transaction.  
- The saga pattern is a protocol that involves a sequence of compensating actions. Each action is a local transaction that can be executed independently and can be undone by another action. The transaction manager coordinates the execution of the actions, and in case of a failure, it triggers the compensating actions to roll back the changes.  

: https://en.wikipedia.org/wiki/Distributed_transaction
: https://www.techopedia.com/definition/29166/distributed-transaction
: https://hazelcast.com/glossary/distributed-transaction/
: https://stackoverflow.com/questions/4217270/what-is-a-distributed-transaction