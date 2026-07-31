### Transaction Recovery

Transaction recovery is the procedure of eliminating the adverse effects of faulty transactions in a distributed database system. In distributed databases, recovery is the most difficult procedure. It is extremely difficult to recover a communication network system that has failed.

There are instances in which a transaction may fail for a variety of causes such as system failure, hardware failure, network error, inaccurate or invalid data, application problems, etc. Failures in the midst of a transaction processing, such as the failure of a site where a subtransaction is being processed, may lead to an inconsistent database. As such, a recovery subsystem is an essential component of a distributed database system.

A distributed transaction is a transaction that affects several resources. For a distributed transaction to commit, all participants must guarantee that any change to data will be permanent. Changes must persist despite system crashes or other unforeseen events.