### Internet and Resource Reservation Protocols

- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain different qualities of service (QoS) for their data flows     .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP is designed to support the integrated services model, which defines two classes of QoS: guaranteed service and controlled-load service .
- Guaranteed service provides a firm bound on end-to-end delay and packet loss, while controlled-load service provides a close approximation of best-effort service under unloaded conditions .
- RSVP uses soft state, which means that the reservations are periodically refreshed and automatically removed if not refreshed .
- RSVP messages are sent as IP datagrams with protocol number 46 and can be classified into two types: PATH and RESV .
- PATH messages are sent by the sender to inform the receivers and intermediate routers about the QoS requirements and the characteristics of the data flow .
- RESV messages are sent by the receivers to request a specific QoS level and to reserve resources along the path .
- RSVP also supports modification and deletion of reservations, as well as error reporting and confirmation .
- RSVP can coexist with other routing protocols, such as OSPF, RIP, or BGP, and can adapt to changes in the network topology or traffic conditions .
- RSVP can also interoperate with other resource reservation protocols, such as ST-II or ATM signaling, using protocol translation or encapsulation .
- RSVP is suitable for real-time systems that require timely and reliable delivery of data, such as videoconferencing, IP telephony, or multimedia streaming   .