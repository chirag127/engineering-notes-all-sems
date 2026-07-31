
### Atomic Commit Protocols

1. Atomic commit protocols are used to ensure that all participants in a distributed transaction agree to a single outcome. 
2. The protocol ensures that all participants either commit or rollback the transaction, and no intermediate states are allowed. 
3. The two-phase commit protocol is the most commonly used atomic commit protocol. It has two phases: the prepare phase and the commit phase.
4. In the prepare phase, all participants agree to either commit or rollback the transaction. 
5. In the commit phase, all participants agree to the outcome of the transaction and the transaction is either committed or rolled back. 
6. The three-phase commit protocol is a more robust version of the two-phase commit protocol. It has three phases: the prepare phase, the commit phase, and the finish phase. 
7. In the finish phase, all participants agree to the outcome of the transaction and the transaction is either committed or rolled back. 
8. The three-phase commit protocol is more reliable than the two-phase commit protocol, as it ensures that all participants agree to the outcome of the transaction.