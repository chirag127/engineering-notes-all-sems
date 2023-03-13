The following is a detailed ASCII diagram for QoS in Ad Hoc Networks for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing.

QoS in Ad Hoc Networks is the performance level of service offered by a network to the user. The goal of QoS is to achieve a more deterministic network behavior so that the information carried by the network can be better delivered and the resources can be better utilized.

QoS in Ad Hoc Networks is challenging due to the fluctuations in channel quality, the interference from non-neighboring nodes, the random mobility of nodes, and the unreliability of wireless channels  .

QoS in Ad Hoc Networks requires QoS-aware routing protocols that can find feasible routes that satisfy the QoS requirements of the applications. Some of the QoS metrics that are commonly studied are bandwidth, delay, jitter, packet loss, and reliability  .

The following diagram illustrates the basic architecture of a QoS-aware routing protocol in Ad Hoc Networks:

```
+----------------+  +----------------+  +----------------+
| Application    |  | Application    |  | Application    |
| Layer          |  | Layer          |  | Layer          |
+----------------+  +----------------+  +----------------+
| QoS Routing    |  | QoS Routing    |  | QoS Routing    |
| Layer          |  | Layer          |  | Layer          |
+----------------+  +----------------+  +----------------+
| MAC Layer      |  | MAC Layer      |  | MAC Layer      |
+----------------+  +----------------+  +----------------+
| Physical Layer |  | Physical Layer |  | Physical Layer |
+----------------+  +----------------+  +----------------+
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       +------------------+------------------+
                  Wireless Channel
```

The QoS Routing Layer is responsible for finding and maintaining feasible routes that meet the QoS requirements of the applications. It interacts with the Application Layer to obtain the QoS parameters, the MAC Layer to obtain the link quality information, and the Physical Layer to send and receive packets.

The QoS Routing Layer can be further divided into two sub-layers: the QoS Routing Control Sub-Layer and the QoS Routing Data Sub-Layer.

The QoS Routing Control Sub-Layer is responsible for performing QoS route discovery, QoS route maintenance, and QoS route selection. It uses QoS routing messages, such as QoS route request, QoS route reply, QoS route error, and QoS route update, to exchange QoS information among the nodes.

The QoS Routing Data Sub-Layer is responsible for forwarding data packets along the QoS routes. It uses QoS routing tables, QoS routing caches, and QoS routing queues to store and manage the QoS routes and the data packets.

The following diagram illustrates the structure of the QoS Routing Layer:

```
+----------------+  +----------------+  +----------------+
| Application    |  | Application    |  | Application    |
| Layer          |  | Layer          |  | Layer          |
+----------------+  +----------------+  +----------------+
| QoS Routing    |  | QoS Routing    |  | QoS Routing    |
| Layer          |  | Layer          |  | Layer          |
+----------------+  +----------------+  +----------------+
| QoS Routing    |  | QoS Routing    |  | QoS Routing    |
| Control Sub-   |  | Control Sub-   |  | Control Sub-   |
| Layer          |  | Layer          |  | Layer          |
+----------------+  +----------------+  +----------------+
| QoS Routing    |  | QoS Routing    |  | QoS Routing    |
| Data Sub-Layer |  | Data Sub-Layer |  | Data Sub-Layer |
+----------------+  +----------------+  +----------------+
|