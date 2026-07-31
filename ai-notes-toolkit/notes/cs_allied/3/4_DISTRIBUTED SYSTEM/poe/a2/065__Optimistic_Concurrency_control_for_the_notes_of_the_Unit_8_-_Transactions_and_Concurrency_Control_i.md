 Here is the content in markdown format without any emojis or external links and in formal tone:

### Optimistic Concurrency control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM.

1. Optimistic concurrency control assumes that concurrent transactions will not conflict with each other and allows them to execute concurrently without locking.
2. Each transaction keeps a copy of the data item it accessed and at commit time verifies that no other transaction has modified its data.
3. If no conflict is detected, the transaction commits, otherwise it aborts and retries.
4. The key advantage is increased concurrency since data items are not locked. However, it may lead to excessive aborts and retries.
5. The concurrency control is done through validation rather than prevention of conflicts. Validation is done at transaction commit time by comparing the original data values copied by the transaction with the current data values. If they are the same, the commit succeeds, otherwise the transaction is aborted.
6. The performance of optimistic methods depends on the frequency of conflicts. If conflicts are rare, optimistic methods lead to high throughput. When conflicts are common, the performance degrades due to excessive aborts and retries.

The above points cover the key highlights of Optimistic concurrency control which assumes no conflicts and allows parallel execution and validates for conflicts at commit to either commit or abort and retry. The advantages and disadvantages along with the dependency on frequency of conflicts have been summarized.