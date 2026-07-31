# Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, and delay.
- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows or streams    .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver. It is generally used by the receiver side for the fast delivery of the transmission packets from the sender to the receiver.
- RSVP uses the integrated services model, which defines two QoS classes: guaranteed service and controlled-load service .
- Guaranteed service provides a firm bound on end-to-end delay and ensures that packets are delivered in order with minimal loss .
- Controlled-load service provides a QoS closely approximating the QoS that same flow would receive from an unloaded network element, but uses less resources than guaranteed service .
- RSVP uses soft state, which means that the reservations are periodically refreshed and automatically removed if not refreshed .
- RSVP messages are sent as IP datagrams with protocol number 46. There are four types of RSVP messages: PATH, RESV, PATHERR, and RESVERR .
- PATH messages are sent by the sender to establish the route and QoS requirements for the data flow. They carry information such as sender IP address, destination IP address, data flow identifier, QoS class, and traffic specification .
- RESV messages are sent by the receiver to request a resource reservation along the path established by the PATH messages. They carry information such as receiver IP address, data flow identifier, QoS class, and reservation specification .
- PATHERR and RESVERR messages are sent by intermediate nodes or receivers to report errors or failures in the reservation process. They carry information such as error code, error value, and error node .
- RSVP supports both unicast and multicast communication. For unicast, there is a single sender and a single receiver. For multicast, there is a single sender and multiple receivers. RSVP uses multicast routing protocols such as DVMRP, MOSPF, and PIM to establish and maintain multicast group membership and routing .
- RSVP is designed to be scalable, robust, and flexible. It can coexist with other protocols and applications that do not use RSVP. It can also adapt to changes in network topology, traffic load, and QoS requirements .