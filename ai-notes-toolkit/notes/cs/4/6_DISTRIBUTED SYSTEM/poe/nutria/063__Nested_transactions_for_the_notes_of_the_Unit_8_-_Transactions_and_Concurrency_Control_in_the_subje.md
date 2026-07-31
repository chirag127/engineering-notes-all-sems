
### Nested Transactions 

* Nested transactions are a type of transaction that occurs when a transaction is started within the scope of another transaction. 
* Nested transactions can be used to ensure that a set of operations is executed atomically, even if the operations occur within multiple transactions. 
* Nested transactions can be used when a transaction needs to be rolled back due to an error, but the inner transactions should remain intact. 
* Nested transactions are also useful for providing a consistent view of data across multiple transactions. 
* Nested transactions can be implemented using two-phase commit protocols, or by using software that supports nested transactions. 
* When using nested transactions, it is important to consider the possibility of deadlocks, which can occur when two transactions are waiting for each other to complete. 
* The ACID properties of a nested transaction are similar to those of a single transaction, with the exception that the atomicity of the transaction is not guaranteed. 
* Finally, nested transactions should be used with care, as they can be complex and difficult to debug.