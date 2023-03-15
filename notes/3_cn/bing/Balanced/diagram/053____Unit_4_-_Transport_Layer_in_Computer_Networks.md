Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a detailed ASCII diagram for Unit 4 - Transport Layer in Computer Networks.

## Unit 4 - Transport Layer in Computer Networks

```
+-----------------+    +-----------------+    +-----------------+
| Application     |    | Application     |    | Application     |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
| Transport       |    | Transport       |    | Transport       |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
| Network         |    | Network         |    | Network         |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
| Data Link       |    | Data Link       |    | Data Link       |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
| Physical        |    | Physical        |    | Physical        |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Host A       |    |    Router       |    |    Host B       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The transport layer is a conceptual division of methods in the layered architecture of protocols in the network stack in the Internet protocol suite and the OSI model. The protocols of this layer provide end-to-end communication services for applications.

The transport layer takes data from the application layer and then breaks it into smaller size segments, numbers each byte, and hands over to the network layer for delivery. The transport layer also provides error-checking mechanisms and data flow controls.

The transport layer interacts with the functions of the session layer and provides the user address which is specified as a station or port. The port variable represents a specific process running on a host. The transport layer protocols need to know the port number of the destination process to deliver the data correctly.

Some of the common transport layer protocols are TCP (Transmission Control Protocol), UDP (User Datagram Protocol), and SCTP (Stream Control Transmission Protocol).
