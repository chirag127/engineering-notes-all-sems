### Locking Techniques for Concurrency Control

Concurrency control is provided in a database to enforce isolation among transactions, preserve database consistency through consistency preserving execution of transactions, and resolve read-write and write-read conflicts .

Various concurrency control techniques are:

1. **Two-phase locking Protocol**: Locking is an operation which secures permission to read or write a data item. The algorithm has two phases: (a) Locking (Growing) and (b) Unlocking (Shrinking). In the Locking (Growing) Phase, a transaction applies locks (read or write) on desired data items one at a time. In the Unlocking (Shrinking) Phase, a transaction unlocks its locked data items one at a time .

2. **Time stamp ordering Protocol** .

3. **Multi version concurrency control** .

4. **Validation concurrency control** .
