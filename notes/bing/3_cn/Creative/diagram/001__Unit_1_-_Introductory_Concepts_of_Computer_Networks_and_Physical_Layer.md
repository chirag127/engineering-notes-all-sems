## Unit 1 - Introductory Concepts of Computer Networks and Physical Layer

A computer network is any group of interconnected computing devices capable of sending or receiving data. A computing device can be a computer, a tablet, a phone, or a smart sensor. Computer networks can be classified by their size, topology, architecture, and protocols.

The physical layer is the lowest layer of the OSI model of computer networking . It is responsible for the actual physical connection between the devices . It defines the hardware equipment, cabling, wiring, frequencies, pulses, and binary signals used to transmit and receive data. It also coordinates the functions required to carry a bit stream over a physical medium. It provides its services to the data-link layer, which is the next higher layer in the OSI model .

The following diagram illustrates the basic architecture of a computer network and the physical layer using ASCII art:

```
+--------+    +--------+    +--------+    +--------+
| Device |----| Device |----| Device |----| Device |
+--------+    +--------+    +--------+    +--------+
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
+--------+    +--------+    +--------+    +--------+
| Router |----| Router |----| Router |----| Router |
+--------+    +--------+    +--------+    +--------+
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
+--------+    +--------+    +--------+    +--------+
| Switch |----| Switch |----| Switch |----| Switch |
+--------+    +--------+    +--------+    +--------+
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
+--------+    +--------+    +--------+    +--------+
| Hub    |----| Hub    |----| Hub    |----| Hub    |
+--------+    +--------+    +--------+    +--------+
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
+--------+    +--------+    +--------+    +--------+
| Cable  |----| Cable  |----| Cable  |----| Cable  |
+--------+    +--------+    +--------+    +--------+
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
+--------+    +--------+    +--------+    +--------+
| Device |----| Device |----| Device |----| Device |
+--------+    +--------+    +--------+    +--------+

```

The devices can be any computing devices that can send or receive data. The routers, switches, hubs, and cables are examples of physical layer devices that facilitate the data transmission and reception . The routers are responsible for routing the data packets to the correct destination. The switches are responsible for connecting multiple devices in a network and forwarding the data packets to the appropriate device. The hubs are responsible for connecting multiple devices in a network and broadcasting the data packets to all the devices. The cables are responsible for carrying the electrical or optical signals between the devices.