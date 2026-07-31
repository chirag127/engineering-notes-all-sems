# Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, and jitter.
- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows  .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses soft state approach, which means that the reservations are periodically refreshed and can be easily modified or deleted.
- RSVP supports both IntServ and DiffServ models of QoS. IntServ uses RSVP to explicitly signal the QoS needs of an application's traffic along the devices in the end-to-end path through the network. DiffServ uses RSVP to aggregate traffic into classes and mark them with different DSCP values.
- RSVP messages are classified into two types: PATH and RESV. PATH messages are sent by the sender to inform the receivers and intermediate routers about the characteristics of the data flow. RESV messages are sent by the receivers to request and confirm the resource reservations along the path.
- RSVP uses filterspecs and flowspecs to specify the data flow and the QoS parameters. A filterpec identifies a data flow by its source address, destination address, and protocol. A flowspec defines the QoS requirements such as bandwidth, delay, and packet loss rate.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver. It is generally used by the receiver side for the fast delivery of the transmission packets from the sender to the receiver.
- RSVP can also support policy control, which allows the network administrators to enforce access control and resource allocation policies based on the identity and priority of the users and applications.