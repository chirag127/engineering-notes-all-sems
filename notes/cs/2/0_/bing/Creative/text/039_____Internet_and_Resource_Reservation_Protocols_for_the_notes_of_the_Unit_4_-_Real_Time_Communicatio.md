### Internet and Resource Reservation Protocols

- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain differing qualities of service (QoS) for their data flows  .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses resource reservation and admission control mechanisms as key building blocks to establish and maintain QoS.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver.
- RSVP supports the following features :
  - Dynamic and soft state: RSVP can adapt to changing network conditions and user requirements by periodically refreshing the reservations and allowing them to time out if not refreshed.
  - Receiver-oriented: RSVP allows the receiver to specify the QoS parameters for the data flow, rather than the sender. This enables heterogeneous receivers to request different levels of QoS for the same data flow.
  - Scalability: RSVP can scale to large multicast groups by using local decision making and aggregation of reservation state. RSVP also supports shared reservations and wildcard filters to reduce the state information in routers.
  - Policy control: RSVP can enforce network policies based on the identity and credentials of the users and applications that request the reservations. RSVP can also communicate the admission decisions and the allocated resources to the users and applications.
  - Interoperability: RSVP can interoperate with different network layer protocols, such as IPv4, IPv6, and MPLS. RSVP can also interoperate with different QoS models, such as IntServ and DiffServ.