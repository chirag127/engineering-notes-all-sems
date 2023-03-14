## Unit 5 - Distributed Resource Management

Distributed resource management (DRM) is an evolving discipline that consists of a set of software, hardware, network tools, procedures and policies for enabling distributed enterprise systems to operate effectively in production. DRM involves solutions for the daily monitoring, resource planning, system administration, change management, operations, performance and other initiatives that are needed to maintain effective productivity in a distributed networked computing environment.

One of the types of databases that DRM deals with is distributed databases, which are databases that are replicated and distributed to network servers at a variety of sites. Distributed databases can improve database performance, protect valuable data, and reduce storage requirements at end-user worksites. However, they also pose challenges such as maintaining data accuracy, concurrency, security, and integrity.

The following diagram illustrates the basic architecture of a distributed database system:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Database 1   |      |   Database 2   |      |   Database 3   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Server 1     |      |   Server 2     |      |   Server 3     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Client 1     |      |   Client 2     |      |   Client 3     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

In this diagram, each database is stored on a different server, and each server can communicate with other servers and clients through a network. Each client can access any database in the system, depending on the permissions and queries. The distributed database system must ensure that the data in each database is consistent and up-to-date with the other databases, and that the queries from the clients are executed correctly and efficiently. This requires a distributed database management system (DDBMS) that coordinates the activities of the servers and clients, and implements the DRM policies and procedures.

: DRM (Distributed Resource Management) - Gartner
: Unit 5: Managing Data Resources - Genuine Notes