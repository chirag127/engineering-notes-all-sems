Network architecture is the design of a computer network. It is a framework for the specification of a network's physical components and their functional organization and configuration, its operational principles and procedures, as well as communication protocols used.

There are different types of network architectures based on the network's size and purpose, such as LAN, WLAN, WAN, MAN, PAN, etc. Each type of network architecture has its own advantages and disadvantages, such as speed, security, cost, scalability, etc.

A common way to represent network architecture is by using a diagram that shows the network devices, such as computers, routers, switches, etc, and the connections between them, such as cables, wireless links, etc. The diagram also shows the network topology, which is the shape or layout of the network, such as bus, star, ring, mesh, etc. The diagram may also show the network protocols, which are the rules or standards that govern the communication between the network devices, such as TCP/IP, Ethernet, Wi-Fi, etc.

Here is an example of a network architecture diagram for a LAN using a star topology and Ethernet protocol:

#### Network architecture diagram

```
    +--------+        +--------+        +--------+
    |        |        |        |        |        |
    |Computer|        |Computer|        |Computer|
    |        |        |        |        |        |
    +---+----+        +---+----+        +---+----+
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        +-----------------+-----------------+
                          |
                          |
                          |
                          |
                      +---+----+
                      |        |
                      | Switch |
                      |        |
                      +---+----+
                          |
                          |
                          |
                          |
                      +---+----+
                      |        |
                      | Router |
                      |        |
                      +---+----+
                          |
                          |
                          |
                          |
                      +---+----+
                      |        |
                      | Modem  |
                      |        |
                      +---+----+
                          |
                          |
                          |
                          |
                      +---+----+
                      |        |
                      |Internet|
                      |        |
                      +--------+
```