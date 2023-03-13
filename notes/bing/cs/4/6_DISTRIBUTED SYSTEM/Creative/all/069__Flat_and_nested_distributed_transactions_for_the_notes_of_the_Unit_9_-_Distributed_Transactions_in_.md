### Flat and nested distributed transactions for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A **distributed transaction** is a flat or nested transaction that accesses objects managed by multiple servers .
- A distributed transaction must maintain the **atomicity** property, which means that either all of the servers involved in the transaction commit the transaction or all of them abort the transaction .
- Distributed transactions can be structured in two different ways: **flat transactions** and **nested transactions** .

#### Flat transactions
- A **flat transaction** has a single initiating point (Begin) and a single end point (Commit or Abort) .
- Flat transactions are usually simple and short-lived, and are suitable for activities that do not require complex coordination or recovery .
- Flat transactions use a **two-phase commit protocol** (2PC) to ensure atomicity across multiple servers .
- The two-phase commit protocol involves a **coordinator** and a set of **participants** .
- In the first phase, the coordinator asks the participants to prepare to commit or abort the transaction, and the participants reply with their votes .
- In the second phase, the coordinator decides whether to commit or abort the transaction based on the votes, and informs the participants of the decision .
- The two-phase commit protocol has some drawbacks, such as blocking, single point of failure, and lack of concurrency .

#### Nested transactions
- A **nested transaction** is a transaction that consists of a number of subtransactions, each of which may be distributed .
- A nested transaction has a hierarchical structure, with a **top-level transaction** and a number of **subtransactions** .
- A nested transaction can be initiated by a Begin statement, and can be terminated by a Commit or Abort statement, or by the end of the parent transaction .
- Nested transactions use a **saga** protocol to ensure atomicity across multiple servers .
- A **saga** is a sequence of subtransactions that can be interleaved with other transactions .
- Each subtransaction in a saga has a **compensating transaction**, which is used to undo the effects of the subtransaction in case of a failure .
- A saga commits by executing all of its subtransactions in order, and aborts by executing the compensating transactions in reverse order .
- The saga protocol has some advantages, such as non-blocking, fault-tolerance, and concurrency .

#### Mnemonics and learning tricks
- To remember the difference between flat and nested transactions, you can use the following mnemonics:
  - Flat transactions are **flat** like a **flat tire**, which means they are **simple** and **short-lived**, and they use **2PC** to **fix** the tire.
  - Nested transactions are **nested** like a **nest of birds**, which means they are **complex** and **long-lived**, and they use **sagas** to **fly** away.
- To remember the two phases of the two-phase commit protocol, you can use the following learning trick:
  - The first phase is **prepare**, which rhymes with **care**, which means the coordinator **cares** about the participants' votes.
  - The second phase is **commit/abort**, which rhymes with **omit/report**, which means the coordinator **omits** or **reports** the decision to the participants.
- To remember the concept of a saga, you can use the following learning trick:
  - A saga is like a **story**, which has a **sequence** of **events**, and each event has a **consequence**, which can be **undone** by a **reverse** event.