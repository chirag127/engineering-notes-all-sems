### Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, and delay.
- Resource reservation protocols are network control protocols that enable Internet applications to obtain specific qualities of service (QoS) for their data flows or streams.
- QoS is the ability of a network to provide different levels of service to different applications or users, based on their needs and preferences.
- Resource reservation protocols use resource reservation and admission control mechanisms to establish and maintain QoS.
- Resource reservation is the process of allocating network resources (such as bandwidth, buffer, CPU, etc.) to a data flow along its end-to-end path through the network.
- Admission control is the process of deciding whether a new data flow can be admitted to the network without violating the QoS guarantees of the existing flows.
- Resource reservation protocols can be classified into two categories: sender-initiated and receiver-initiated.
- Sender-initiated protocols are initiated by the sender of the data flow, who specifies the QoS requirements and requests the network to reserve resources accordingly.
- Receiver-initiated protocols are initiated by the receiver of the data flow, who specifies the QoS requirements and requests the network to reserve resources accordingly.
- An example of a sender-initiated protocol is the Integrated Services (IntServ) model, which uses the Resource Reservation Protocol (RSVP) to signal the QoS needs of a data flow along the devices in the end-to-end path through the network.
- An example of a receiver-initiated protocol is the Differentiated Services (DiffServ) model, which uses the Differentiated Services Code Point (DSCP) field in the IP header to mark the packets of a data flow with a certain QoS level, and relies on the network devices to provide the appropriate QoS treatment based on the DSCP value.
- Resource reservation protocols can be used for both multicast and unicast data flows.
- Multicast data flows are data flows that are sent from one sender to multiple receivers, such as videoconferencing or online gaming.
- Unicast data flows are data flows that are sent from one sender to one receiver, such as IP telephony or video streaming.
- Resource reservation protocols can be used for both real-time and non-real-time data flows.
- Real-time data flows are data flows that have strict QoS requirements, such as timeliness, jitter, and delay, and cannot tolerate significant variations in network performance, such as videoconferencing or IP telephony.
- Non-real-time data flows are data flows that have less strict QoS requirements, such as reliability and throughput, and can tolerate some variations in network performance, such as web browsing or file transfer.