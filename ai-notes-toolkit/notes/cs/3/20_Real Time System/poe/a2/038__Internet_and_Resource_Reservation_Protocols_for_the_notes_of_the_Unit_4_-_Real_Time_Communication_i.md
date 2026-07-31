 Here is the content in markdown format without any emojis or external links, written in points and in a formal tone:

### Internet and Resource Reservation Protocols

- Internet does not guarantee Quality of Service (QoS) required for real-time applications. Real-time communications require guaranteed bandwidth, delay, jitter, etc.
- To achieve QoS, resource reservation protocols are used. Some examples are:
- RSVP (Resource Reservation Protocol): It is a signaling protocol that allows applications to reserve resources across a network and to obtain QoS on flows between two hosts. RSVP defines two types of messages - Path and Resv. Path messages establish a path between sender and receiver. Resv messages are used to reserve resources for the path.
- IntServ (Integrated Services): It works on the concept of reserving resources explicitly at every router on the path. It uses RSVP for resource reservation but has scalability issues due to per-flow state maintenance at every router.
- DiffServ (Differentiated Services): It works on classifying and marking packets at the edge of the network and providing Per Hop Behaviors (PHBs) at the core routers to provide differentiated QoS. It requires less state maintenance than IntServ and is more scalable.

The above points cover the key concepts and protocols related to resource reservation in the Internet for real-time communications. The content is written in a formal tone with headings and points as required. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.