# Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, and jitter.
- Resource Reservation Protocol (RSVP) is a network control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows or streams.
- RSVP operates over IPv4 or IPv6 and supports both multicast and unicast data flows.
- RSVP is receiver-initiated, meaning that the receiver of a data flow requests a certain QoS from the network by sending RSVP messages along the reverse path of the data flow.
- RSVP messages include PATH and RESV messages, which are used to establish and maintain resource reservations along the data path.
- PATH messages are sent by the sender of a data flow and carry information about the sender, the data flow characteristics, and the QoS requirements.
- RESV messages are sent by the receiver of a data flow and carry information about the desired QoS and the reservation style.
- Reservation styles specify how the resources are shared among the receivers of a multicast data flow. There are three main reservation styles: Fixed-Filter (FF), Shared-Explicit (SE), and Wildcard-Filter (WF).
- FF style reserves resources for each sender-receiver pair separately, and requires the receiver to specify the sender's address in the RESV message.
- SE style reserves resources for a group of senders that are explicitly listed by the receiver in the RESV message, and allows the receiver to share the resources among the senders.
- WF style reserves resources for any sender of the data flow, and does not require the receiver to specify the sender's address in the RESV message.
- RSVP also uses other messages, such as CONFIRM, TEAR, and ERROR, to confirm, tear down, or report errors in the resource reservations.
- RSVP is not a routing protocol, but it works with routing protocols to determine the data path and the reverse path. RSVP can also work with traffic control mechanisms, such as admission control, packet classification, packet scheduling, and policing, to enforce the QoS guarantees.
- RSVP is designed to be scalable, robust, and flexible. It can handle dynamic changes in the network topology, the data flows, and the QoS requirements. It can also support different QoS models, such as IntServ and DiffServ.