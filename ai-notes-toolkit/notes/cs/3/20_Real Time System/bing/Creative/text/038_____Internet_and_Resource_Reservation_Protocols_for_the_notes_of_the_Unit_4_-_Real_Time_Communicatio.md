### Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, and delay.
- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows or streams  .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses soft state approach, which means that the reservations are periodically refreshed and can be easily modified or deleted.
- RSVP supports both unicast and multicast communication, and can handle heterogeneous receivers with different QoS requirements.
- RSVP uses two types of messages: PATH and RESV. PATH messages are sent by the sender to inform the routers and receivers about the characteristics and requirements of the data flow. RESV messages are sent by the receivers to request and confirm the resource reservations along the path .
- RSVP can work with two service models: Integrated Services (IntServ) and Differentiated Services (DiffServ). IntServ uses RSVP to explicitly signal the QoS needs of an application's traffic along the devices in the end-to-end path through the network. DiffServ uses RSVP to aggregate the QoS requests of multiple flows and map them to a predefined service class.