Remote login is a service that allows an authorized user to access and interact with a remote computer over a network. It is an example of an application layer service in the OSI model or the TCP/IP model. The application layer is the topmost layer of the network stack that provides the interface between the user and the network protocols.

A possible ASCII diagram for remote login in application layer is:

### Remote login in application layer

```
+----------------+             +----------------+
|                |             |                |
|  User terminal |             | Remote computer|
|                |             |                |
+----------------+             +----------------+
|                |             |                |
|Application layer|<---------->|Application layer|
|                |             |                |
+----------------+             +----------------+
|                |             |                |
|Transport layer |<---------->|Transport layer |
|                |             |                |
+----------------+             +----------------+
|                |             |                |
|Network layer   |<---------->|Network layer   |
|                |             |                |
+----------------+             +----------------+
|                |             |                |
|Data link layer |<---------->|Data link layer |
|                |             |                |
+----------------+             +----------------+
|                |             |                |
|Physical layer  |<---------->|Physical layer  |
|                |             |                |
+----------------+             +----------------+
```

The diagram shows the communication between the user terminal and the remote computer at different layers of the network stack. The application layer is responsible for initiating and terminating the remote login session, as well as sending and receiving the user commands and responses. The lower layers are responsible for ensuring the reliable and secure transmission of the data packets across the network.