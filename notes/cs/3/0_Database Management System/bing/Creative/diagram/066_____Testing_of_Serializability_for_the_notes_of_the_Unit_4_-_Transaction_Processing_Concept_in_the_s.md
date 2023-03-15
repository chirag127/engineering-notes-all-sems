### Testing of Serializability

- Serializability is the property of a schedule that ensures the same outcome as if the transactions were executed serially, one after the other.
- Serializability is important to maintain the consistency and correctness of the database in concurrent transactions.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that preserves the order of conflicting operations in a schedule. Two operations are conflicting if they belong to different transactions, access the same data item, and at least one of them is a write operation.
- View serializability is a weaker form of serializability that preserves the final state of the database and the read-write dependencies in a schedule. Two schedules are view equivalent if they have the same initial read, final write, and read-after-write operations for each data item.
- Testing of serializability involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- We can use below two techniques to test serializability in DBMS: serialization graph and precedence graph.
- A serialization graph is a directed graph of the entire transactions of a schedule. Each node represents a transaction and each edge represents a conflict between two transactions. A schedule is conflict serializable if and only if its serialization graph is acyclic.
- A precedence graph is a directed graph of the conflicting operations of a schedule. Each node represents an operation and each edge represents a precedence relationship between two operations. A schedule is conflict serializable if and only if its precedence graph is acyclic.
- A schedule is view serializable if and only if it is view equivalent to a serial schedule. There is no simple algorithm to test view serializability, but one possible method is to check all the possible serial schedules for view equivalence with the given schedule.
- Example: Consider the following schedule S of three transactions T1, T2, and T3:

| T1 | T2 | T3 |
|----|----|----|
| R(A) | | |
| | R(B) | |
| W(A) | | |
| | W(B) | |
| | | R(A) |
| | | R(B) |
| | | W(A) |
| | | W(B) |

- To test the conflict serializability of S, we can construct the serialization graph as follows:

![Serialization graph](https://i.imgur.com/4w4wQ8n.png)

- The serialization graph has a cycle T1 -> T2 -> T3 -> T1, which means that S is not conflict serializable.
- To test the view serializability of S, we can compare it with all the possible serial schedules of T1, T2, and T3, which are:

| T1 | T2 | T3 |
|----|----|----|
| R(A) | | |
| W(A) | | |
| | R(B) | |
| | W(B) | |
| | | R(A) |
| | | R(B) |
| | | W(A) |
| | | W(B) |

| T1 | T3 | T2 |
|----|----|----|
| R(A) | | |
| W(A) | | |
| | R(A) | |
| | R(B) | |
| | W(A) | |
| | W(B) | |
| | | R(B) |
| | | W(B) |

| T2 | T1 | T3 |
|----|----|----|
| R(B) | | |
| W(B) | | |
| | R(A) | |
| | W(A) | |
| | | R(A) |
| | | R(B) |
| | | W(A) |
| | | W(B) |

| T2 | T3 | T1 |
|----|----|----|
| R(B) | | |
| W(B) | | |
| | R(A) | |
| | R(B) | |
| | W(A) | |
| | W(B) | |
| | | R(A) |
| | | W(A) |

| T3 | T1 | T2 |
|----|----|----|
| R(A) | | |
| R(B) | | |
| W(A) | | |
| W(B) | | |
| | R(A) | |
| | W(A) | |
| | | R(B