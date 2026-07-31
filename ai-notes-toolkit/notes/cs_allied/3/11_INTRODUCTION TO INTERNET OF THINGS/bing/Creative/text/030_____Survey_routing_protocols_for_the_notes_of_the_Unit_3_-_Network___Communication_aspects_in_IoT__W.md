### Survey routing protocols for IoT

- Routing protocols are responsible for finding and maintaining routes between nodes in a network, especially in wireless and dynamic environments such as IoT.
- Routing protocols for IoT must consider the characteristics and requirements of IoT devices, such as low power, low memory, low bandwidth, mobility, heterogeneity, scalability, and security   .
- Routing protocols for IoT can be classified into three categories based on the network structure: flat, hierarchical, and location-based .
  - Flat routing protocols treat all nodes equally and use flooding or gossiping techniques to disseminate data. Examples of flat routing protocols are SPIN, Directed Diffusion, and Flooding .
  - Hierarchical routing protocols organize nodes into clusters and use cluster heads or gateways to aggregate and forward data. Examples of hierarchical routing protocols are LEACH, PEGASIS, and HEED .
  - Location-based routing protocols use the geographic position of nodes to make routing decisions. Examples of location-based routing protocols are GEAR, GPSR, and GAF .
- Routing protocols for IoT can also be classified into three categories based on the routing strategy: proactive, reactive, and hybrid .
  - Proactive routing protocols maintain routes to all destinations at all times, regardless of the traffic demand. Examples of proactive routing protocols are OLSR, DSDV, and RIP .
  - Reactive routing protocols establish routes on demand, when there is a need to send data. Examples of reactive routing protocols are AODV, DSR, and TORA .
  - Hybrid routing protocols combine the advantages of both proactive and reactive routing protocols. Examples of hybrid routing protocols are ZRP, EIGRP, and CORMAN .
- Routing protocols for IoT can also be classified into three categories based on the protocol layer: network layer, transport layer, and application layer .
  - Network layer routing protocols operate at the IP layer and are responsible for finding the best path between source and destination nodes. Examples of network layer routing protocols are RPL, LOADng, and 6LoWPAN .
  - Transport layer routing protocols operate at the TCP/UDP layer and are responsible for providing reliable and efficient data delivery. Examples of transport layer routing protocols are CoAP, MQTT, and AMQP .
  - Application layer routing protocols operate at the HTTP layer and are responsible for providing semantic and contextual information for data exchange. Examples of application layer routing protocols are XMPP, DDS, and LWM2M .
- Routing protocols for IoT must also consider the security and privacy issues that arise from the open and distributed nature of IoT networks. Some of the security challenges for IoT routing protocols are authentication, confidentiality, integrity, availability, and resilience .
- Some of the security solutions for IoT routing protocols are encryption, digital signatures, certificates, key management, trust management, and intrusion detection .