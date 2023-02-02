### Flat and nested distributed transactions for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM
Flat Distributed Transactions: 
- Involve multiple databases or resources that are coordinated in a single transaction 
- All participants must agree to commit or rollback the transaction 
- Uses 2-phase commit protocol to ensure atomicity 
- Can have performance issues due to network latency and possible bottlenecks 

Nested Distributed Transactions: 
- Transactions within transactions 
- Inner transactions can commit or rollback independently 
- Outer transaction can rollback inner transactions 
- Complex to implement and manage 
- Can lead to increased risk of data inconsistency.
