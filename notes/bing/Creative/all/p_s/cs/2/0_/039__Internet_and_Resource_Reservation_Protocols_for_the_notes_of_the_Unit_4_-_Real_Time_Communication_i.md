### Internet and Resource Reservation Protocols for Real Time Communication

- Real time communication (RTC) is the exchange of data, voice, or video over a network with minimal delay and high reliability.
- RTC requires certain quality of service (QoS) guarantees from the network, such as bandwidth, delay, jitter, and packet loss.
- Internet protocols for RTC include the following:

  - Real-time Transport Protocol (RTP): A protocol that provides end-to-end delivery of real-time data, such as audio and video, over IP networks. RTP supports features such as payload type identification, sequence numbering, timestamping, and synchronization .
  - Real-time Transport Control Protocol (RTCP): A protocol that works in conjunction with RTP to provide feedback on the quality and performance of the RTP streams. RTCP sends periodic reports on packet loss, delay, jitter, and bandwidth usage .
  - Real-time Streaming Protocol (RTSP): A protocol that enables the control of streaming media servers, such as play, pause, fast forward, and rewind. RTSP also supports session management, authentication, and encryption.
  - Session Initiation Protocol (SIP): A protocol that establishes, modifies, and terminates multimedia sessions, such as voice and video calls, over IP networks. SIP also supports features such as user location, presence, and mobility.
  - Session Description Protocol (SDP): A protocol that describes the characteristics and capabilities of the multimedia sessions, such as media formats, codecs, transport protocols, and addresses.
  - Resource Reservation Protocol (RSVP): A protocol that enables the reservation of network resources along the path of the multimedia sessions, such as bandwidth, buffers, and CPU cycles. RSVP provides new Internet services with higher quality than best-effort by means of resource reservations   .
  - Differentiated Services (DiffServ): A framework that classifies and prioritizes network traffic into different service classes, such as expedited forwarding (EF) and assured forwarding (AF). DiffServ marks the packets with a differentiated services code point (DSCP) in the IP header and relies on the network devices to provide the appropriate QoS treatment based on the DSCP value .
  - Integrated Services (IntServ): A framework that specifies the QoS requirements of the multimedia sessions using a service level specification (SLS). IntServ uses RSVP or successor protocols to explicitly signal the QoS needs of the sessions along the devices in the end-to-end path through the network. If every network device along the path can reserve the necessary resources, the originating application can begin transmitting  .

- Advantages of Internet and resource reservation protocols for RTC include the following:

  - They enable the delivery of real-time data with high quality and reliability over IP networks.
  - They support a variety of multimedia applications, such as voice over IP (VoIP), video conferencing, online gaming, and streaming media.
  - They provide flexibility and scalability for the network and the applications.
  - They enhance the user experience and satisfaction.

- Disadvantages of Internet and resource reservation protocols for RTC include the following:

  - They introduce additional complexity and overhead for the network and the applications.
  - They require cooperation and compatibility among the network devices and the applications.
  - They face challenges such as security, interoperability, and congestion control.

Some possible mnemonics and learning tricks for the topic are:

- To remember the order of the Internet protocols for RTC, you can use the acronym **RRTS SIP** (RTP, RTCP, RTSP, SIP).
- To remember the functions of the Internet protocols for RTC, you can use the following phrases:

  - RTP: **R**eal-time **T**ransport **P**rotocol delivers real-time data.
  - RTCP: **R**eal-time **T**ransport **C**ontrol **P**rotocol provides feedback on the quality and performance of the RTP streams.
  - RTSP: **R**eal-time **S**treaming **P**rotocol controls streaming media servers.
  - SIP: **S**ession **I**nitiation **P**rotocol establishes, modifies, and terminates multimedia sessions.
  - SDP: **S**ession **D**escription **P**rotocol describes the characteristics and capabilities of the multimedia sessions.
  - RSVP: **R**esource re**S**er**V**ation **P**rotocol reserves network resources along the path of the multimedia sessions.
- To remember the difference between DiffServ and IntServ, you can use the following analogy:

  - DiffServ is like a highway with different lanes for different types of vehicles, such as cars, buses, trucks, and motorcycles. The vehicles are marked with different colors or stickers to indicate their priority and service class. The traffic is managed by the signs and signals along the highway.
  - IntServ is like a railway with different trains for different types of passengers, such as business, economy, and first class. The passengers need to buy tickets and make reservations for their seats and compartments. The traffic is managed by the railway stations and controllers along the railway.