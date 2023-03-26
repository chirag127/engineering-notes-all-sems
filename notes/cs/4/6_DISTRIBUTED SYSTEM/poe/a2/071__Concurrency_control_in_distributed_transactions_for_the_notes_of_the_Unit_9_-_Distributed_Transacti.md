 Here is the content in Markdown format without any emojis or external links:

### Concurrency control in distributed transactions

1.  Serializability: Ensuring that transactions in a distributed system execute as if they were executed sequentially in some order. This ensures consistent data in the system.
2.  Two-phase locking: A concurrency control mechanism to ensure serializability. It has two phases - growing phase and shrinking phase. In growing phase, transactions acquire locks on the data items they access. In shrinking phase, the transactions release the locks. The locks are released only after the transaction completes its work. This prevents dirty reads.
3.  Timestamp ordering: Each transaction is assigned a unique timestamp when it begins. The transactions are executed in the timestamp order to ensure serializability. This method may lead to cascading aborts where a transaction has to be aborted because of earlier aborted transactions.
4.  Optimistic concurrency control: Transactions proceed without acquiring locks. Before committing, each transaction verifies that no other transaction has updated the data items it has read. If verification fails, the transaction is aborted. This method avoids delays due to locking but may lead to more aborts and retries.

The content is written in a formal tone with points and without any emojis or external links as requested. The content summarizes some key concepts related to concurrency control in distributed transactions to serve as notes for learning and exams. Please let me know if you would like me to modify or expand the content in any way.