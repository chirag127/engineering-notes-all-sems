Security in Hadoop consists of four main components: Authentication, Authorization, Auditing, and Encryption. Authentication is the process of verifying the identity of the users or services that interact with Hadoop. Authorization is the process of granting or denying access to resources or operations based on the authenticated identity. Auditing is the process of recording and reviewing the actions performed by users or services on Hadoop. Encryption is the process of protecting the confidentiality and integrity of data stored or transmitted on Hadoop.

One of the most common ways to implement security in Hadoop is to use Kerberos, a network authentication protocol that uses tickets to prove the identity of users or services. Kerberos can be used to authenticate users or services before they access Hadoop services such as HDFS, MapReduce, YARN, Hive, HBase, etc. Kerberos can also be used to encrypt the communication between Hadoop services and clients.

A simplified diagram of security in Hadoop using Kerberos is shown below:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hadoop User   |    |   Hadoop Client |    |   Hadoop Server |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       | 1. Request ticket   |                      |
       |--------------------->|                      |
       |                      |                      |
       |                      | 2. Request ticket   |
       |                      |--------------------->|
       |                      |                      |
       |                      | 3. Return ticket    |
       |                      |<---------------------|
       |                      |                      |
       | 4. Return ticket    |                      |
       |<---------------------|                      |
       |                      |                      |
       | 5. Request service  |                      |
       |--------------------->|                      |
       |                      |                      |
       |                      | 6. Request service  |
       |                      |--------------------->|
       |                      |                      |
       |                      | 7. Return service   |
       |                      |<---------------------|
       |                      |                      |
       | 8. Return service   |                      |
       |<---------------------|                      |
       |                      |                      |
```

The steps are as follows:

1. The Hadoop user requests a ticket from the Hadoop client, which acts as a proxy for the user.
2. The Hadoop client requests a ticket from the Hadoop server, which acts as a Kerberos server.
3. The Hadoop server returns a ticket to the Hadoop client, after verifying the identity of the user and the client.
4. The Hadoop client returns the ticket to the Hadoop user, after verifying the identity of the server and the ticket.
5. The Hadoop user requests a service from the Hadoop client, using the ticket as a proof of identity.
6. The Hadoop client requests a service from the Hadoop server, using the ticket as a proof of identity.
7. The Hadoop server returns the service to the Hadoop client, after verifying the identity of the client and the ticket.
8. The Hadoop client returns the service to the Hadoop user, after verifying the identity of the server and the service.

This diagram is based on the information from the search results  . It is not a complete representation of all the aspects of security in Hadoop, but a simplified one for illustration purposes. There are other security mechanisms and tools that can be used in Hadoop, such as SSL/TLS, ACLs, Ranger, Sentry, etc. For more details, please refer to the official documentation of Hadoop and its related projects.