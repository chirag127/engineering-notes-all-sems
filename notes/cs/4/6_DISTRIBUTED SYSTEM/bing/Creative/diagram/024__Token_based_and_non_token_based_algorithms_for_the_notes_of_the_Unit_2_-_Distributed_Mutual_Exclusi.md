The following is a detailed ASCII diagram for token based and non token based algorithms for distributed mutual exclusion.

Token based algorithm:

In this algorithm, a unique token is shared among all the sites in the distributed system. A site can enter the critical section only if it has the token. The token is passed from one site to another in a logical ring. The token contains a queue of requests for the critical section. When a site receives the token, it checks if its request is at the head of the queue. If yes, it enters the critical section and removes its request from the queue. If not, it passes the token to the next site in the ring.

The diagram below shows an example of four sites (S1, S2, S3, S4) in a logical ring, where S1 has the token and wants to enter the critical section. S2 and S4 have also requested the critical section and their requests are in the token queue. S3 has not requested the critical section.

+-----+    +-----+    +-----+    +-----+
| S1  |    | S2  |    | S3  |    | S4  |
+-----+    +-----+    +-----+    +-----+
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   v          v          v          v
+-----+    +-----+    +-----+    +-----+
| CS  |    |     |    |     |    |     |
+-----+    +-----+    +-----+    +-----+
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   +----------+          +----------+
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       v                         v
+-----+---------------------+-----+
|     | Token queue: S2, S4 |     |
+-----+---------------------+-----+

Non token based algorithm:

In this algorithm, there is no token and each site communicates with a set of other sites to determine who should enter the critical section next. The algorithm uses timestamps to order the requests and resolve conflicts. There are two types of messages: REQUEST and REPLY. A site sends a REQUEST message to all other sites when it wants to enter the critical section. A site sends a REPLY message to the requesting site when it grants permission. A site can enter the critical section only when it has received REPLY messages from all other sites.

The diagram below shows an example of four sites (S1, S2, S3, S4), where S1 and S2 have requested the critical section at the same time with timestamps T1 and T2 respectively. S3 and S4 have not requested the critical section. S1 and S2 compare their timestamps and S1 has the smaller timestamp, so it has higher priority. S3 and S4 send REPLY messages to both S1 and S2, but S2 defers its request and waits for S1 to finish. S1 enters the critical section after receiving all REPLY messages.

+-----+    +-----+    +-----+    +-----+
| S1  |    | S2  |    | S3  |    | S4  |
+-----+    +-----+    +-----+    +-----+
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |          |          |          |
   |<---------|          |          |
   | REQUEST  |          |          |
   | T1       |          |          |
   |          |<---------|          |
   |          | REQUEST  |          |
   |          | T2       |          |
   |          |          |<---------|
   |          |          | REQUEST  |
   |          |          | T3       |
   |