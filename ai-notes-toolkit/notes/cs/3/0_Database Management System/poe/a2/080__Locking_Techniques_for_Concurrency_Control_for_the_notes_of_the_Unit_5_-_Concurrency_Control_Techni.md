 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Locking Techniques for Concurrency Control

1.  Two-Phase Locking: It is the most commonly used protocol. It divides the transaction into two phases -
    - Growing phase: In this phase, the transaction can acquire locks on the data items it needs.
    - Shrinking phase: In this phase, the transaction releases all the locks acquired in the first phase. This ensures that the locks are not held for a long time.
2.  Strict Two-Phase Locking: In this protocol, a transaction must acquire all locks before it can release any lock. This avoids the anomaly of releasing and reacquiring locks.
3.  Timestamp Ordering: Each transaction is assigned a timestamp when it begins. Data items also have timestamps that indicate the last transaction that updated them. A transaction T can update a data item only if the transaction's timestamp is greater than the data item's timestamp. This ensures serializability.
4.  Optimistic concurrency control: It assumes that conflicts are rare and locks are acquired only when required. The transactions execute in isolation and validate at the end for conflicts. If no conflict occurs, it commits, else it rolls back.

The notes cover the key locking techniques to achieve concurrency control in database systems. The techniques ensure data consistency while allowing transactions to execute concurrently. They help avoid problems like dirty reads, inconsistent analysis, and lost updates.

How's that? I have written the content in points in a formal tone without any emojis or external links as per your requirements. Let me know if you would like me to modify or expand the content.