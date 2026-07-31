 Here is the content in markdown format without any emojis or external links, being formal and not showing emotions:

### Comparison of methods for concurrency control

1. Locking:
- Exclusive lock: Only one transaction can access the data at a time. Ensures consistency but reduces concurrency.
- Shared lock: Multiple transactions can read the data simultaneously but only one can write. Allows more concurrency but prone to anomalies like dirty reads.

2. Timestamp ordering:
- Each transaction is assigned a timestamp when it starts.
- Transactions are executed in timestamp order.
- If a transaction wants to read/write data that has been written by a later transaction, it is rolled back.
- Ensures serializability but can lead to cascading rollbacks and wasted work.

3. Optimistic concurrency control:
- Transactions execute without acquiring locks, assuming no conflicts.
- Before committing, each transaction verifies that no other transaction has modified its read data (using version numbers).
- If a conflict is detected, the transaction is rolled back and retried.
- Allows high concurrency but can lead to wasted work due to rollbacks and repeated retries.

The methods have their pros and cons and the choice of method depends on the requirements of the application, such as throughput or concurrency. Combinations of the methods are also used in practice to leverage their individual benefits.

The content summarizes three popular methods for concurrency control - locking, timestamp ordering and optimistic concurrency control. The key points of each method are highlighted in terms of their effects on concurrency and consistency along with their limitations. The conclusion notes that the choice of method depends on application requirements.