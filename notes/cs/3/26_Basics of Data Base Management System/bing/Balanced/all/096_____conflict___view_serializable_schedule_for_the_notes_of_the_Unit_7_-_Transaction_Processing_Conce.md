# Conflict and View Serializable Schedule

## Conflict Serializability

- A schedule is called **conflict serializable** if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations are said to be **conflicting** if all conditions satisfy:
  - They belong to different transactions
  - They operate on the same data item
  - At least one of them is a write operation
- A schedule is **conflict serializable** if it preserves the order of conflicting operations of every pair of transactions in a serial schedule.
- Conflict serializability can be checked by using a **precedence graph** or a **conflict graph**  .
  - A precedence graph is a directed graph where the nodes represent the transactions and the edges represent the conflicts between them.
  - An edge from Ti to Tj means that Ti must precede Tj in any serial schedule that is conflict equivalent to the given schedule.
  - A schedule is conflict serializable if and only if its precedence graph is **acyclic** .

## View Serializability

- A schedule is called **view serializable** if it is view equal to a serial schedule.
- Two schedules are said to be **view equal** if the order of initial read, final write and update operations is the same in both the schedules .
- A schedule is **view serializable** if it preserves the following three conditions for every data item in a serial schedule:
  - **Initial read condition**: If a transaction Ti reads the initial value of a data item X in S, then the same transaction must read the initial value of X in S'.
  - **Final write condition**: If a transaction Ti performs the final write on a data item X in S, then the same transaction must perform the final write on X in S'.
  - **Update read condition**: If a transaction Ti reads the value of a data item X written by another transaction Tj in S, then the same transaction must read the value of X written by the same transaction in S'.
- View serializability can be checked by using a **polygraph** or a **view graph**.
  - A polygraph is a directed graph where the nodes represent the read and write operations and the edges represent the dependencies between them.
  - An edge from Ri(X) to Wj(X) means that Ti must read the initial value of X before Tj writes the final value of X.
  - An edge from Wi(X) to Rj(X) means that Ti must write the value of X that is read by Tj.
  - An edge from Wi(X) to Wj(X) means that Ti must write the value of X before Tj overwrites it.
  - A schedule is view serializable if and only if its polygraph is **acyclic**.

## Difference between Conflict and View Serializability

- Conflict serializability is a **subset** of view serializability.
- Every conflict serializable schedule is also view serializable, but the converse is not true.
- A view serializable schedule may contain **blind writes**, which are write operations that do not depend on any previous read operations.
- A conflict serializable schedule does not contain any blind writes, as they are considered as conflicting operations.
- Conflict serializability is **easier** to check and implement than view serializability.
- View serializability is **more general** and allows more concurrency than conflict serializability.