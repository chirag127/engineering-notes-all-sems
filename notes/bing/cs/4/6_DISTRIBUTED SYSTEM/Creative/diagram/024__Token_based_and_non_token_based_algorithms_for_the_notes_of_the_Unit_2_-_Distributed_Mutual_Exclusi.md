The following is a detailed ASCII diagram for token based and non token based algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM.

### Token based and non token based algorithms

Token based algorithms use a unique token that is shared among all the sites in a distributed system. Only the site that holds the token can enter the critical section. The token is passed from one site to another according to some protocol. An example of a token based algorithm is the Suzuki-Kasami algorithm.

Non token based algorithms do not use a token, but instead rely on message passing and coordination among the sites to achieve mutual exclusion. A site communicates with a set of other sites to determine who should execute the critical section next. An example of a non token based algorithm is the Ricart-Agrawala algorithm.

The following diagram illustrates the basic architecture of a token based and a non token based algorithm:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    Site 1      |     |    Site 2      |     |    Site 3      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+------+-----+         +-----+-----+         +-----+-----+
|            |         |           |         |           |
|   Token    |         |  Request  |         |  Reply    |
|            |         |           |         |           |
+------------+         +-----------+         +-----------+

Token based algorithm: Site 1 holds the token and can enter the critical section. Site 2 sends a request to Site 1 for the token. Site 1 passes the token to Site 2 after exiting the critical section. Site 2 can then enter the critical section.

Non token based algorithm: Site 2 wants to enter the critical section and sends a request to Site 1 and Site 3. Site 1 and Site 3 reply with a permission to Site 2. Site 2 waits for all the replies and then enters the critical section.
```