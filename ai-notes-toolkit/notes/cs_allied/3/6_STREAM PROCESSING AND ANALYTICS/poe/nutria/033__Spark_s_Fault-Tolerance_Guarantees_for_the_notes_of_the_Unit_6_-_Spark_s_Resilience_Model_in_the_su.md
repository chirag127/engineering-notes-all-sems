
### Spark’s Fault-Tolerance Guarantees

* Spark is designed to be fault-tolerant, meaning that it is able to recover from failures without data loss.
* Spark’s resilience model is based on the concept of lineage, which is a record of how a dataset was created.
* Spark stores the lineage information in a distributed log, and uses it to reconstruct lost data in case of failure.
* Spark also uses replicas to ensure that data is not lost in case of failure.
* Spark also uses a combination of checkpointing and logging to ensure that data is not lost in case of failure.
* Spark also provides fault-tolerance for streaming applications, by using a combination of checkpointing and logging.