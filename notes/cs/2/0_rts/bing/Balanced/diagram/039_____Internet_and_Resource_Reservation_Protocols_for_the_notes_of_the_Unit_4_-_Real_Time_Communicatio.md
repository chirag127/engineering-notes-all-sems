### Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP, HTTP, FTP, etc.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, etc.
- Quality of Service (QoS) is the ability of a network to provide different levels of service to different applications or data flows, according to their needs and preferences.
- Resource Reservation Protocol (RSVP) is a network control protocol that enables Internet applications to obtain specific QoS for their data flows.
- RSVP operates over IPv4 or IPv6 and supports both multicast and unicast data flows.
- RSVP is receiver-initiated, meaning that the receiver of a data flow requests the desired QoS from the network and the sender adapts to the available resources.
- RSVP uses soft state, meaning that the reservations are periodically refreshed and can be easily modified or removed.
- RSVP uses PATH and RESV messages to establish and maintain reservations along the end-to-end path of a data flow.
- RSVP uses filterspecs and flowspecs to specify the characteristics of the data flow and the requested QoS, respectively.
- RSVP uses admission control and policy control mechanisms to determine whether a reservation request can be granted or not, based on the available resources and the authorization of the user.
- RSVP is integrated with the IntServ model, which defines a set of QoS classes that can be requested by applications, such as Guaranteed Service, Controlled Load Service, and Best Effort Service.
- RSVP can also interoperate with the DiffServ model, which uses packet marking and traffic conditioning to provide different levels of service to different classes of traffic.