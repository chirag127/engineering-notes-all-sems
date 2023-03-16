### Internet and Resource Reservation Protocols

Real-time communication is essential for many applications, such as audio and video streaming, online gaming, and video conferencing. To support real-time communication, the Internet must provide Quality of Service (QoS) guarantees, such as bounded delay and jitter, and guaranteed bandwidth. Resource reservation protocols are used to reserve resources in the network to provide these QoS guarantees.

1. **Resource Reservation Protocol (RSVP):** RSVP is a signaling protocol used to reserve resources in the network for a particular data flow. It operates at the transport layer and is used by both the sender and receiver of the data flow to request and reserve resources in the network.

2. **Integrated Services (IntServ):** IntServ is a QoS architecture that uses RSVP to reserve resources in the network. It provides two types of services: Guaranteed Service, which provides a firm bound on delay, and Controlled Load Service, which provides a QoS level similar to that of an unloaded network.

3. **Differentiated Services (DiffServ):** DiffServ is another QoS architecture that provides QoS guarantees by classifying and prioritizing traffic. It uses a 6-bit field in the IP header, called the Differentiated Services Code Point (DSCP), to classify traffic into different classes. Each class is assigned a different level of priority, and the network provides different levels of service to each class.

These are some of the protocols and architectures used to provide QoS guarantees for real-time communication in the Internet. They are essential for ensuring that real-time applications can function properly and provide a good user experience.