A dynamic voting protocol is a fault-tolerant technique for managing replicated files in a distributed system. It allows sites to dynamically adjust the number of votes assigned to each replica based on the availability and reliability of the sites. The goal is to ensure that a majority of votes can be collected to access or update a file, even in the presence of site or link failures.

The following diagram illustrates the basic architecture of a dynamic voting protocol using ASCII characters:

```
    +-----------------+        +-----------------+        +-----------------+
    | Site A          |        | Site B          |        | Site C          |
    | Vote: 1         |        | Vote: 1         |        | Vote: 1         |
    | Replica: R1     |        | Replica: R1     |        | Replica: R1     |
    +-----------------+        +-----------------+        +-----------------+
          |                        |                        |
          |                        |                        |
          |                        |                        |
          |                        |                        |
          |                        |                        |
          |                        |                        |
          |                        |                        |
          |                        |                        |
          |                        |                        |
          |                        |                        |
          |                        |                        |
          |                        |                        |
          |                        |                        |
          |                        |                        |
    +-----------------+        +-----------------+        +-----------------+
    | Site D          |        | Site E          |        | Site F          |
    | Vote: 1         |        | Vote: 1         |        | Vote: 1         |
    | Replica: R1     |        | Replica: R1     |        | Replica: R1     |
    +-----------------+        +-----------------+        +-----------------+
```

In this diagram, there are six sites (A, B, C, D, E, F) that have a replica of file R1. Each site has one vote initially. To access or update R1, a site needs to collect at least four votes (a majority of six) from other sites. If a site or a link fails, the remaining sites can reassign their votes to achieve a new majority. For example, if site A fails, site B can increase its vote to two, and site C can increase its vote to three, so that they can still access or update R1 with four votes. This way, the dynamic voting protocol can tolerate failures and maintain consistency of the replicated file.