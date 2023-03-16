# Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, and delay.
- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows or streams  .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses resource reservation and admission control mechanisms as key building blocks to establish and maintain QoS.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver. It is generally used by the receiver side for the fast delivery of the transmission packets from the sender to the receiver.
- RSVP has the following features and functions:
  - It supports both unicast and multicast communication.
  - It is receiver-oriented, meaning that the receiver of a data flow initiates and maintains the resource reservation.
  - It is simplex, meaning that it reserves resources in one direction only, from sender to receiver.
  - It is soft state, meaning that it periodically refreshes the reservation state in the network devices along the data path.
  - It is scalable, meaning that it does not require global network state information or per-flow processing at the core routers.
  - It is flexible, meaning that it can accommodate heterogeneous receivers with different QoS requirements and can adapt to dynamic network conditions and user preferences.
  - It is modular, meaning that it can interoperate with different QoS models, such as IntServ and DiffServ, and can use different signaling protocols, such as IPsec and MPLS.