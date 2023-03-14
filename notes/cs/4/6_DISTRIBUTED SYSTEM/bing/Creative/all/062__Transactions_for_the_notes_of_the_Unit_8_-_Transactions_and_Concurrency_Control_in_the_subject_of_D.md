### Transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a logical unit of work that consists of one or more operations on data, such as reading, writing, inserting, deleting, etc. 
- A transaction has four properties, known as ACID: Atomicity, Consistency, Isolation, and Durability.  
  - Atomicity means that either all the operations in a transaction are executed successfully, or none of them are. If any operation fails, the transaction is aborted and the data is restored to its original state.  
  - Consistency means that a transaction preserves the integrity and validity of the data. A transaction must not violate any constraints or rules that apply to the data, such as primary keys, foreign keys, triggers, etc.  
  - Isolation means that a transaction is executed independently of other concurrent transactions. The intermediate results of a transaction are not visible to other transactions, and vice versa. A transaction must not interfere with or be affected by other transactions.  
  - Durability means that the effects of a committed transaction are permanent and persist even in the case of system failures or power outages. The data is not lost or corrupted after a transaction completes.  
- A distributed transaction is a transaction that involves two or more network hosts, such as servers, clients, or coordinators.    
  - A distributed transaction may access or modify data that is stored on different hosts, or that is replicated or partitioned across multiple hosts.    
  - A distributed transaction requires a distributed transaction manager, which is responsible for coordinating the execution and commitment of the transaction across all the hosts.    
  - A distributed transaction must ensure that the ACID properties are maintained across all the hosts, despite the possibility of network failures, communication delays, or host crashes.    
- A distributed transaction can be structured in two different ways: flat or nested. 
  - A flat distributed transaction has a single begin point and a single end point, where the transaction is either committed or aborted. A flat distributed transaction can be implemented using the two-phase commit protocol, which consists of two phases: prepare and commit.  
    - In the prepare phase, the coordinator asks all the participants (servers or clients) to vote on whether they are ready to commit the transaction. If all the participants vote yes, the coordinator moves to the commit phase. If any participant votes no, or fails to respond, the coordinator aborts the transaction.  
    - In the commit phase, the coordinator informs all the participants of the final decision, which is to commit the transaction. If the coordinator fails to communicate with some participants, it uses a recovery protocol to ensure that they eventually receive the decision.  
  - A nested distributed transaction is a transaction that contains subtransactions, which can be committed or aborted independently. A nested distributed transaction can be implemented using the nested two-phase commit protocol, which extends the two-phase commit protocol to handle subtransactions. 
    - In the nested two-phase commit protocol, each subtransaction has its own coordinator, which is a participant of the parent transaction. The subtransaction coordinator follows the two-phase commit protocol with its own participants, and then reports the outcome to the parent transaction coordinator. 
    - The parent transaction coordinator collects the outcomes of all the subtransactions, and then follows the two-phase commit protocol with its own participants, which include the subtransaction coordinators. The parent transaction coordinator can commit the transaction only if all the subtransactions are committed. 

: https://www.cockroachlabs.com/blog/distributed-transactions-what-why-and-how-to-build-a-distributed-transactional-application/
: https://www.geeksforgeeks.org/flat-nested-distributed-transactions/
: https://learn.microsoft.com