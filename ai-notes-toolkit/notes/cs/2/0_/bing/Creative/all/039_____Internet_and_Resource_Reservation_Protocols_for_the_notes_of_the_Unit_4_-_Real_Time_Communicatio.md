# Internet and Resource Reservation Protocols

- Internet applications have different network performance requirements, such as reliability, timeliness, and quality of service (QoS)  .
- Resource Reservation Protocol (RSVP) is a transport layer protocol that enables Internet applications to obtain specific QoS for their data flows or streams  .
- RSVP operates over IPv4 or IPv6 and supports both multicast and unicast data flows .
- RSVP is receiver-initiated, meaning that the receiver of a data flow requests a certain QoS from the network and the sender adapts to the available resources  .
- RSVP uses soft state, meaning that the reservations are periodically refreshed and can be easily modified or deleted  .
- RSVP uses two types of messages: PATH and RESV. PATH messages are sent by the sender to inform the receivers and intermediate routers about the characteristics of the data flow. RESV messages are sent by the receiver to request a certain QoS and reserve resources along the path  .
- RSVP can work with two service models: integrated services (IntServ) and differentiated services (DiffServ). IntServ provides end-to-end QoS guarantees by reserving resources for each data flow. DiffServ provides aggregate QoS by classifying and marking data packets into different service classes .