Protocols and standards in networks architecture are used to define the representation and interaction modes within a network and to make certain functions generally available. Protocols are a set of guidelines governing the exchange of information in a simple, dependable and secure way. Standards are formal specifications that ensure compatibility and interoperability among different devices and systems.

Network architecture is the design of a network that includes the hardware, software, transmission media, network topology, and communication protocols. There are two main types of network architecture: peer-to-peer (P2P) and client/server. P2P networks are decentralized and allow each node to communicate directly with each other without a central server. Client/server networks are centralized and rely on a server to provide services and resources to the clients.

The following diagram illustrates the basic architecture of a client/server network using the TCP/IP protocol suite, which is the most widely used network protocol in the internet. TCP/IP consists of four layers: application, transport, internet, and network interface. Each layer performs specific functions and communicates with the adjacent layers using well-defined interfaces.

```
+-----------------+      +-----------------+
|   Application   |      |   Application   |
|      Layer      |      |      Layer      |
+-----------------+      +-----------------+
|    Transport    |      |    Transport    |
|      Layer      |      |      Layer      |
+-----------------+      +-----------------+
|     Internet    |      |     Internet    |
|      Layer      |      |      Layer      |
+-----------------+      +-----------------+
| Network Interface|     | Network Interface|
|      Layer      |      |      Layer      |
+-----------------+      +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        +-----------------------+
                Network
```