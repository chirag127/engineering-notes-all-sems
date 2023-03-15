# Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different quality of service (QoS) requirements, such as bandwidth, delay, jitter, and reliability.
- Resource reservation protocols are network protocols that enable Internet applications to request and obtain specific QoS guarantees from the network for their data flows.
- Resource reservation protocols can be classified into two categories: integrated services (IntServ) and differentiated services (DiffServ).
- IntServ is a QoS model that provides end-to-end QoS guarantees by reserving resources along the path of a data flow using a signaling protocol such as RSVP (Resource Reservation Protocol).
- RSVP is a transport layer protocol that allows a receiver to initiate and maintain resource reservations for a multicast or unicast data flow. RSVP uses PATH and RESV messages to exchange QoS parameters and reserve resources between the sender and the receiver.
- DiffServ is a QoS model that provides QoS differentiation by marking packets with different priority levels using a field called DSCP (Differentiated Services Code Point) in the IP header. DiffServ does not require signaling or reservation, but relies on the network devices to apply different QoS policies based on the DSCP value of each packet.
- DiffServ can be combined with RSVP to provide end-to-end QoS guarantees for selected data flows, while providing QoS differentiation for the rest of the traffic. This is called RSVP over DiffServ or DiffServ-aware RSVP.