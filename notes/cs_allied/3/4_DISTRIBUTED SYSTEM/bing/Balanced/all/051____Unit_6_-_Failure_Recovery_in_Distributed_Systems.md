## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring the normal operation of a distributed system after a failure occurs.
- Failures can be classified into different types, such as crash failures, omission failures, timing failures, response failures, Byzantine failures, etc.
- Failure recovery techniques can be categorized into different levels, such as process level, communication level, data level, and application level.
- Process level recovery involves restarting or replacing failed processes, using techniques such as checkpointing, rollback, replication, and fault tolerance.
- Communication level recovery involves ensuring reliable and ordered delivery of messages, using techniques such as acknowledgments, timeouts, retransmissions, sequence numbers, and logical clocks.
- Data level recovery involves maintaining the consistency and availability of distributed data, using techniques such as transactions, concurrency control, commit protocols, logging, and recovery protocols.
- Application level recovery involves adapting the application logic to cope with failures, using techniques such as exception handling, compensation, and retry.
- Failure recovery techniques can have different properties, such as correctness, completeness, efficiency, scalability, and transparency.