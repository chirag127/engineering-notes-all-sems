### Internet and Resource Reservation Protocols for Real Time Communication

- Internet protocols are the set of rules and standards that enable communication and data exchange over the Internet.
- Real time communication is the transmission and reception of data with minimal delay and high reliability, such as voice, video, or multimedia applications.
- Internet protocols for real time communication need to provide quality of service (QoS) guarantees, such as bandwidth, delay, jitter, and packet loss, to meet the requirements of real time applications.
- Some of the Internet protocols for real time communication are:

  - Real-time Transport Protocol (RTP): A protocol that provides end-to-end delivery of real time data, such as audio and video, over IP networks. RTP supports features such as payload type identification, sequence numbering, timestamping, and synchronization.
  - Real-time Transport Control Protocol (RTCP): A protocol that works in conjunction with RTP to provide feedback and control information, such as sender and receiver reports, source description, and bye messages.
  - Real-time Streaming Protocol (RTSP): A protocol that enables the establishment and control of media sessions between a client and a server, such as play, pause, fast forward, and rewind.
  - Session Initiation Protocol (SIP): A protocol that enables the initiation, modification, and termination of multimedia sessions, such as voice and video calls, over IP networks. SIP supports features such as user location, user availability, session negotiation, and session management.
  - Session Description Protocol (SDP): A protocol that describes the characteristics and parameters of a multimedia session, such as media type, codec, format, and transport protocol.

- Resource reservation protocols are the protocols that enable the reservation of network resources, such as bandwidth and buffer space, along the path of a data flow, to provide QoS guarantees for real time communication.
- Resource reservation protocols can be classified into two categories:

  - Integrated services (IntServ): A model that provides QoS guarantees by reserving resources for each individual flow at each router along the path. IntServ requires the use of the Resource Reservation Protocol (RSVP) to signal and maintain the reservations .
  - Differentiated services (DiffServ): A model that provides QoS guarantees by classifying and marking packets into different service classes at the edge routers, and applying different forwarding policies based on the service classes at the core routers. DiffServ does not require per-flow reservation or signaling, but relies on traffic engineering and network provisioning to allocate resources.

- Resource Reservation Protocol (RSVP) is a protocol that enables the reservation of network resources for real time communication. RSVP has the following features :

  - Receiver-oriented: The reservation requests are initiated by the receivers, based on the QoS requirements of the application and the network conditions.
  - Soft state: The reservations are maintained by periodic refresh messages, and are automatically removed if the refresh messages stop or the network topology changes.
  - Scalable: The reservations are aggregated at the routers, and only the routers along the path of the data flow need to maintain the reservation state.
  - Flexible: The reservations can be made for unicast or multicast flows, and can be modified or canceled at any time.
  - QoS-aware: The reservations can specify the QoS parameters, such as bandwidth, delay, and packet loss, using the IntServ service models, such as guaranteed service or controlled load service.