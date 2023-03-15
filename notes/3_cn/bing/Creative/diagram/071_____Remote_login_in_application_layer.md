Remote login is a service that allows an authorized user to access and interact with a remote computer over a network. It is an example of an application layer service in the OSI model or the TCP/IP model. The application layer is the topmost layer of the network stack that provides the interface between the user and the network protocols.

A possible ASCII diagram for remote login in application layer is:

```
+-----------------+      +-----------------+
|                 |      |                 |
|  User terminal  |      |  Remote host    |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  Application    |      |  Application    |
|  layer          |      |  layer          |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  Transport      |      |  Transport      |
|  layer          |      |  layer          |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  Network        |      |  Network        |
|  layer          |      |  layer          |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  Data link      |      |  Data link      |
|  layer          |      |  layer          |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  Physical       |      |  Physical       |
|  layer          |      |  layer          |
|                 |      |                 |
+-----------------+      +-----------------+
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       +------------------------+
              Network
```