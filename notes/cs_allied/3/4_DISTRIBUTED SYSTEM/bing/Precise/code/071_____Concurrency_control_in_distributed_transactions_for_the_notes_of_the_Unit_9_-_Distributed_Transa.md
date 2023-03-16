### Concurrency control in distributed transactions

Concurrency control in distributed transactions refers to the mechanism used to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution. These transactions are performed in a distributed database system where relevant data is hosted by a group of linked data servers.

- **Distributed concurrency control** provides concepts and technologies to synchronize distributed transactions in a way that their interleaved execution does not violate the ACID properties.
- **Distributed transactions** are executed in a distributed database environment, where a set of connected data servers host related data.
- **Locking-based concurrency control protocols** use the concept of locking data.
- **Timestamp-based concurrency control algorithms** use a transaction’s timestamp.
- **Optimistic concurrency control** is another approach to concurrency control.
- **2PC*** is a novel distributed transaction control protocol that can extract more concurrent processing capabilities under high-intensity competitive workloads than previous approaches for a multi-microservice.