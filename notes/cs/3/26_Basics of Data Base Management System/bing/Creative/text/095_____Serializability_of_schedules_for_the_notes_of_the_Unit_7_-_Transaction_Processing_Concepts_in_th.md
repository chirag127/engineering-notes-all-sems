### Serializability of schedules

- Serializability is a property of a transaction schedule (history) that relates to the isolation property of a database transaction .
- Serializability of a schedule means equivalence (in the outcome, the database state, data values) to a serial schedule (i.e., sequential with no transaction overlap in time) with the same transactions .
- Serializability of schedules ensures that a non-serial schedule is equivalent to a serial schedule. It helps in maintaining the transactions to execute simultaneously without interleaving one another.
- Serializability is a way to check if the execution of two or more transactions are maintaining the database consistency or not.
- There are two methods widely used to check serializability: conflict equivalent and view equivalent .
- Conflict equivalent: Two schedules are conflict equivalent if they have the same set of transactions and the order of any two conflicting operations is the same in both schedules .
- View equivalent: Two schedules are view equivalent if they have the same set of transactions and the following three conditions hold for each data item in the database :
  - The same transaction reads the initial value of the data item in both schedules.
  - The same transaction writes the final value of the data item in both schedules.
  - The set of transactions that read the value of the data item written by a transaction is the same in both schedules.