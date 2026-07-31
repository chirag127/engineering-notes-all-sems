# Quality of Service for the Notes of the Unit 6 - Transport Layer in the Subject of Computer Networks

- Quality of service (QoS) is the ability of a network to provide reliable service to the traffic over various technologies and applications.
- QoS is important for applications that require high performance, low latency, low jitter, and low packet loss, such as voice, video, and online gaming.
- The transport layer is responsible for providing end-to-end communication between applications on different hosts in a network.
- The transport layer also determines what type of service to provide to the applications, such as reliable or unreliable, connection-oriented or connectionless, and ordered or unordered delivery of data.
- Some techniques that can be used to improve the QoS at the transport layer are:

  - Scheduling: This is the process of deciding which packet to send next from a queue of packets waiting to be transmitted. Scheduling can be based on different criteria, such as priority, fairness, or deadline. Scheduling can help to avoid congestion, reduce delay, and ensure fairness among different flows.
  - Traffic shaping: This is the process of controlling the rate and burstiness of traffic sent by a source. Traffic shaping can be done by using token buckets, leaky buckets, or other algorithms. Traffic shaping can help to smooth out traffic fluctuations, reduce congestion, and match the traffic profile to the network capacity.
  - Admission control: This is the process of deciding whether to accept or reject a new flow request based on the current network conditions and the QoS requirements of the flow. Admission control can help to prevent overloading the network, ensure the QoS guarantees for the accepted flows, and reject the flows that cannot be satisfied.
  - Resource reservation: This is the process of allocating network resources, such as bandwidth, buffer, or CPU, to a flow based on its QoS requirements. Resource reservation can be done by using protocols, such as RSVP, IntServ, or DiffServ. Resource reservation can help to ensure the QoS guarantees for the reserved flows, and isolate them from the effects of other flows.