 Here is the content in markdown format for the topic ### Internet and Resource Reservation Protocols for the notes of the Unit 4 - Real Time Communication in the subject of Real Time System:

## Internet and Resource Reservation Protocols

- The Internet was designed for best-effort service and does not provide guarantees on bandwidth or delay. This makes it challenging to support real-time applications that have strict requirements on quality of service.
- To address this, various resource reservation protocols have been proposed for reserving network resources to provide QoS guarantees to real-time applications. Some of the major resource reservation protocols are:
- RSVP (Resource Reservation Protocol): RSVP is a signaling protocol that allows applications to reserve resources across a network path. RSVP-capable routers establish and maintain bindings between senders and receivers to allow resources to be reserved for data flows. RSVP can be used with both multicast and unicast data delivery.
- SIP (Session Initiation Protocol): SIP is a signaling protocol used to establish, modify, and terminate real-time multimedia sessions over the Internet. SIP can be used to reserve network resources for real-time media sessions. While SIP handles session control, it relies on RSVP or another resource reservation protocol to reserve resources.
- ST-II (Stream Control Transmission Protocol - Integrated Services): ST-II extends the TCP protocol to support QoS by reserving resources and providing guarantees on bandwidth, delay, jitter, and loss. However, ST-II has seen limited deployment due to complexity and lack of router support.

Advantages of resource reservation protocols:
- Allow applications to reserve network resources to meet QoS requirements
- Can provide guarantees on bandwidth, delay, jitter, and packet loss

Disadvantages of resource reservation protocols:
- Require support from routers and other network devices, which can increase cost and complexity
- Scalability can be a challenge due to the amount of state that needs to be maintained
- The fundamentally best-effort nature of the Internet can make absolute QoS guarantees difficult to achieve in practice

Example applications that can benefit from resource reservation:
- VoIP and video conferencing (require low delay and jitter)
- Online gaming (require low latency and minimal packet loss)
- Streaming media (require guarantees on bandwidth and delay)