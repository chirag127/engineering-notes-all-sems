# Concurrency control in distributed transactions

- Concurrency control in distributed transactions refers to the synchronization of distributed transactions in such a way that their interleaved execution does not violate the ACID properties  .
- These transactions are performed in a distributed database system where relevant data is hosted by a group of linked data servers .
- There are several approaches to achieve distributed concurrency control, including locking-based concurrency control protocols, timestamp-based concurrency control algorithms, and optimistic concurrency control algorithms.
- An example of a distributed transaction control protocol is 2PC*, which is an optimized protocol based on the traditional 2PC that can extract more concurrent processing capabilities under high-intensity competitive workloads for a multi-microservice.