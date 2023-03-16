# Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, and delay.
- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows or streams .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses soft state approach, which means that the reservations are periodically refreshed and can be easily modified or deleted.
- RSVP supports both Integrated Services (IntServ) and Differentiated Services (DiffServ) models of QoS.
- IntServ uses RSVP to explicitly signal the QoS needs of an application's traffic along the devices in the end-to-end path through the network.
- DiffServ uses RSVP to aggregate the QoS requirements of multiple flows into a single reservation and mark the packets with different priorities.
- RSVP messages include PATH, RESV, PATHERR, RESVERR, PATHTEAR, and RESVTEAR.
- PATH messages are sent by the sender to establish the route and QoS parameters for the data flow.
- RESV messages are sent by the receiver to request a reservation along the path established by the PATH messages.
- PATHERR and RESVERR messages are sent by the intermediate nodes to report errors or failures in the reservation process.
- PATHTEAR and RESVTEAR messages are sent by the sender or the receiver to tear down the reservation and release the resources.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver.
- RSVP is useful for applications that require timely but not necessarily reliable data delivery, such as videoconferencing, IP telephony, and other forms of multimedia communications.