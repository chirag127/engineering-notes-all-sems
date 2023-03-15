### Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, and delay.
- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows or streams  .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses resource reservation and admission control mechanisms as key building blocks to establish and maintain QoS.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver. It is generally used by the receiver side for the fast delivery of the transmission packets from the sender to the receiver.
- RSVP supports both soft state and hard state reservation models. Soft state reservation is dynamic and requires periodic refresh messages to maintain the reservation. Hard state reservation is static and requires explicit teardown messages to release the reservation.
- RSVP messages are classified into two types: PATH and RESV. PATH messages are sent by the sender to inform the receiver and the intermediate routers about the characteristics and requirements of the data flow. RESV messages are sent by the receiver to request and confirm the resource reservation along the path.
- RSVP uses filterspecs and flowspecs to specify the data flow and the QoS parameters. Filterspecs identify the sender and the receiver of the data flow. Flowspecs define the QoS requirements such as bandwidth, delay, and reliability.
- RSVP can interoperate with different QoS models such as Integrated Services (IntServ) and Differentiated Services (DiffServ). IntServ provides end-to-end QoS guarantees by reserving resources for each data flow. DiffServ provides QoS differentiation by classifying and marking data packets into different service classes.