According to the search results, there are three fundamental models for distributed systems: interaction models, failure models, and security models. Interaction models deal with the communication and coordination of processes in a distributed system, such as the timing, ordering, and reliability of messages. Failure models specify the types of faults that can occur in processes and communication channels, such as omission, crash, or arbitrary failures. Security models describe the threats and countermeasures for protecting the distributed system from malicious attacks, such as confidentiality, integrity, and availability.

One possible way to draw a detailed ASCII diagram for these models is:

```
+---------------------+  +---------------------+  +---------------------+
| Interaction Models  |  |  Failure Models     |  |  Security Models    |
+---------------------+  +---------------------+  +---------------------+
|                     |  |                     |  |                     |
|  Synchronous        |  |  Omission           |  |  Confidentiality    |
|                     |  |                     |  |                     |
|  Asynchronous       |  |  Crash              |  |  Integrity          |
|                     |  |                     |  |                     |
|  Logical Ordering   |  |  Arbitrary          |  |  Availability       |
|                     |  |                     |  |                     |
+---------------------+  +---------------------+  +---------------------+
```