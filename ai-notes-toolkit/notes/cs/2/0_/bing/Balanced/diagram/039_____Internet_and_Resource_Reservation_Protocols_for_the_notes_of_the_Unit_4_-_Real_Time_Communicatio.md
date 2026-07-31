### Internet and Resource Reservation Protocols

- Internet applications have different network performance requirements, such as reliability, timeliness, and quality of service (QoS).
- Resource Reservation Protocol (RSVP) is a network control protocol that enables Internet applications to obtain specific QoS for their data flows or streams  .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses resource reservation and admission control mechanisms as key building blocks to establish and maintain QoS.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver. It is generally used by the receiver side for the fast delivery of the transmission packets from the sender to the receiver.
- RSVP messages are sent as IP datagrams with protocol number 46. There are two types of RSVP messages: PATH and RESV.
- PATH messages are sent by the sender to the receiver along the data path, carrying information about the sender and the data flow characteristics.
- RESV messages are sent by the receiver to the sender along the reverse data path, carrying information about the receiver and the desired QoS parameters.
- RSVP uses soft state, which means that the reservations are periodically refreshed by sending PATH and RESV messages. If a reservation is not refreshed, it is timed out and removed.
- RSVP supports various QoS models, such as the integrated services model (IntServ) and the differentiated services model (DiffServ).
- IntServ defines three service classes: guaranteed service, controlled load service, and best effort service. Guaranteed service provides a firm bound on end-to-end delay and packet loss. Controlled load service provides a QoS close to that of an unloaded network. Best effort service provides no QoS guarantees.
- DiffServ defines a set of per-hop behaviors (PHBs) that specify how packets are treated at each node along the data path. PHBs are indicated by the differentiated services code point (DSCP) field in the IP header. Examples of PHBs are expedited forwarding (EF), assured forwarding (AF), and default forwarding (DF).
- RSVP can be integrated with DiffServ by using the RSVP/DiffServ mapping (RDM) approach, which maps RSVP reservations to DiffServ PHBs. RDM enables end-to-end QoS provisioning across heterogeneous networks that support both RSVP and DiffServ.