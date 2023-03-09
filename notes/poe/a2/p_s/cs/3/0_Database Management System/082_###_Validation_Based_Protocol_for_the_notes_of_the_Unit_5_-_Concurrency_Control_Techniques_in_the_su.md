 Here is the content in markdown format for the topic -

### Validation Based Protocol

Validation based protocol is a concurrency control technique that ensures serialized execution of transactions. It works as follows:

1. When a transaction Ti wants to read an item X, it sends a `read_validation` message to the site that manages X.
2. The site checks if there are any in-progress updates to X by other transactions. If not, it sends a `read_ok` message to Ti, allowing it to read X.
3. When Ti wants to update X, it sends an `update_validation` message to the site managing X.
4. The site checks if there are any in-progress updates/reads to X by other transactions. If not, it sends an `update_ok` message to Ti, allowing it to update X.
5. If another transaction Tj has updated X after Ti read it but before Ti updated it, the `update_validation` request by Ti will detect this and cause Ti to abort and retry.

Thus, validation ensures that transactions are executed one at a time, thereby maintaining consistency. However, it leads to higher abort rates and hence lower concurrency. It is suitable for applications where consistency is of prime importance.

Advantages:
- Ensures consistency and serializability

Disadvantages:
- Leads to higher abort rates and lower concurrency
- Involves multiple message exchanges leading to higher overheads

Applications: Database systems where consistency is critical (e.g. banking databases)

[Detailed diagrams and examples can be added here]