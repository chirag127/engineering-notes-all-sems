Internet addressing is the process of assigning unique identifiers to devices on a network. The most common protocol for internet addressing is TCP/IP, which stands for Transmission Control Protocol/Internet Protocol. TCP/IP uses a hierarchical structure of addresses, consisting of four levels: network, subnetwork, host, and socket.

The following diagram illustrates the basic architecture of internet addressing in TCP/IP:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Network 1      |      |  Network 2      |      |  Network 3      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Subnet 1.1     |      |  Subnet 2.1     |      |  Subnet 3.1     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Subnet 1.2     |      |  Subnet 2.2     |      |  Subnet 3.2     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Host 1.1.1     |      |  Host 2.1.1     |      |  Host 3.1.1     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Host 1.1.2     |      |  Host 2.1.2     |      |  Host 3.1.2     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Host 1.2.1     |      |  Host 2.2.1     |      |  Host 3.2.1     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Host 1.2.2     |      |  Host 2.2.2     |      |  Host 3.2.2     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Socket 1.1.1.1 |      |  Socket 2.1.1.1 |      |  Socket 3.1.1.1 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Socket 1.1.1.2 |      |  Socket 2.1.1.2 |      |  Socket 3.1.1.2 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Socket 1.1.2.1 |      |  Socket 2.1.2.1 |      |  Socket 3.1.2.1 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Socket 1.1.2.2 |      |  Socket 2.1.2.2 |      |  Socket 3.1.2.2 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Socket 1.2.1.1 |      |  Socket 2.2.1.1 |      |  Socket 3.2.1.1 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |