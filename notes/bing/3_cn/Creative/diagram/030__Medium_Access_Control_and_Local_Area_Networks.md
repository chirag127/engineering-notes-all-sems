#### Medium Access Control and Local Area Networks

Medium access control (MAC) is a sublayer of the data link layer that coordinates the access of multiple devices to a shared medium, such as a cable or a wireless channel. MAC protocols can be classified into two categories: contention-based and token-passing.

Contention-based MAC protocols allow any device to transmit data whenever the medium is idle, but they may cause collisions if two or more devices transmit at the same time. A common example of a contention-based MAC protocol is carrier sense multiple access/collision detection (CSMA/CD), which is used in Ethernet networks. In CSMA/CD, a device senses the medium before transmitting and backs off for a random time if a collision is detected.

Token-passing MAC protocols use a special frame, called a token, to grant the right to transmit to one device at a time. The token is passed from one device to another in a predefined order, and only the device that holds the token can transmit data. A common example of a token-passing MAC protocol is token ring, which uses a ring topology and a token that circulates around the ring.

A local area network (LAN) is a network that connects devices within a limited geographic area, such as a building or a campus. LANs typically use MAC protocols to coordinate the access of devices to a shared medium, such as a twisted-pair cable, a coaxial cable, a fiber-optic cable, or a wireless channel. LANs can have different physical and logical topologies, such as bus, star, ring, or mesh.

The following diagram illustrates the basic architecture of a LAN using a contention-based MAC protocol (CSMA/CD) and a bus topology:

```
    +------+      +------+      +------+      +------+
    |Device|      |Device|      |Device|      |Device|
    +------+      +------+      +------+      +------+
       |             |             |             |
       |             |             |             |
       |             |             |             |
       |             |             |             |
       +-------------+-------------+-------------+-------------+
                             Shared medium (bus)
```

The following diagram illustrates the basic architecture of a LAN using a token-passing MAC protocol (token ring) and a ring topology:

```
    +------+      +------+      +------+      +------+
    |Device|      |Device|      |Device|      |Device|
    +------+      +------+      +------+      +------+
       |             |             |             |
       |             |             |             |
       V             V             V             V
       +-------------+-------------+-------------+-------------+
       |             |             |             |             |
       |             |             |             |             |
       +-------------+-------------+-------------+-------------+
       ^             ^             ^             ^
       |             |             |             |
       |             |             |             |
    +------+      +------+      +------+      +------+
    |Device|      |Device|      |Device|      |Device|
    +------+      +------+      +------+      +------+
                             Shared medium (ring)
```