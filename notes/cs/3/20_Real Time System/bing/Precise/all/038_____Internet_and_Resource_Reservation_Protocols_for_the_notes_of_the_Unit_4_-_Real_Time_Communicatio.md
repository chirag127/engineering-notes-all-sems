### Internet and Resource Reservation Protocols

Unit 4 - Real Time Communication in the subject of Real Time System

1. **Introduction:** The Internet is a global network of interconnected computer networks that use the standard Internet Protocol Suite (TCP/IP) to link devices worldwide. Resource reservation protocols are used to reserve resources such as bandwidth, processing power, and memory in advance to ensure that real-time communication can take place.

2. **Resource Reservation Protocol (RSVP):** RSVP is a protocol used to reserve resources for real-time communication over the Internet. It operates at the transport layer of the OSI model and is used to request specific Quality of Service (QoS) from the network for a particular data flow.

3. **RSVP Operation:** RSVP operates by sending PATH and RESV messages between the sender and receiver of a data flow. The PATH message is sent by the sender to the receiver, and contains information about the data flow and the desired QoS. The RESV message is sent by the receiver to the sender, and contains the receiver's reservation request.

4. **RSVP and Integrated Services:** RSVP is often used in conjunction with the Integrated Services (IntServ) model, which provides QoS guarantees for individual data flows. IntServ uses RSVP to reserve resources along the path of a data flow, and to ensure that the desired QoS is provided.

5. **Differentiated Services (DiffServ):** DiffServ is another approach to providing QoS guarantees over the Internet. Unlike IntServ, which provides QoS guarantees for individual data flows, DiffServ provides QoS guarantees for aggregates of data flows. DiffServ uses a system of traffic classification and traffic conditioning to provide different levels of QoS to different data flows.

6. **Conclusion:** Resource reservation protocols, such as RSVP, are used to reserve resources in advance to ensure that real-time communication can take place over the Internet. These protocols are often used in conjunction with QoS models, such as IntServ and DiffServ, to provide QoS guarantees for data flows.