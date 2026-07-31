# Internet and Resource Reservation Protocols

Unit 4 - Real Time Communication in the subject of Real Time System

1. **Introduction:** The Internet is a global network of interconnected computer networks that use the standard Internet Protocol Suite (TCP/IP) to link devices worldwide. Resource reservation protocols are used to reserve resources such as bandwidth, processing power, and memory in a network to ensure that real-time communication can take place.

2. **Resource Reservation Protocol (RSVP):** RSVP is a protocol used to reserve resources in a network for real-time communication. It operates at the transport layer of the OSI model and is used to request a specific quality of service (QoS) from the network for a particular data flow.

3. **RSVP Operation:** RSVP operates by sending messages between the sender and receiver of a data flow, as well as the intermediate routers. The sender sends a PATH message to the receiver, which contains information about the data flow and the desired QoS. The receiver then sends a RESV message back to the sender, which contains the QoS requirements and the resources that need to be reserved.

4. **RSVP and Integrated Services:** RSVP is often used in conjunction with the Integrated Services (IntServ) model, which provides QoS guarantees for individual data flows. IntServ uses RSVP to reserve resources in the network and to ensure that the desired QoS is provided for the data flow.

5. **Differentiated Services (DiffServ):** DiffServ is another approach to providing QoS in a network. Unlike IntServ, which provides QoS guarantees for individual data flows, DiffServ provides QoS guarantees for classes of traffic. DiffServ uses a mechanism called "per-hop behavior" (PHB) to classify traffic into different classes and to provide different levels of QoS for each class.

6. **Multi-Protocol Label Switching (MPLS):** MPLS is a protocol used to improve the performance of networks by using labels to forward packets instead of using the traditional IP routing mechanism. MPLS can be used in conjunction with RSVP and DiffServ to provide QoS guarantees in a network.

7. **Conclusion:** Resource reservation protocols such as RSVP, in conjunction with QoS models such as IntServ and DiffServ, can be used to provide QoS guarantees for real-time communication in a network. MPLS can also be used to improve the performance of the network and to provide QoS guarantees. These protocols and models are essential for ensuring that real-time communication can take place in a network.