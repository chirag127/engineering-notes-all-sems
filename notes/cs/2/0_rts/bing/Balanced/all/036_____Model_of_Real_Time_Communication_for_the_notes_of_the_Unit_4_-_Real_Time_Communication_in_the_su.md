# Model of Real Time Communication

- Real time communication (RTC) is any online communication that happens in real-time, with negligible latency and without storing data en route to the destination  .
- RTC can include voice, video, text, and data transmission over landlines, mobile phones, VoIP, or other internet-based platforms .
- RTC is important for applications that require timely and accurate delivery of information, such as online gaming, telemedicine, e-learning, video conferencing, etc .
- RTC can be modeled as a network of sources, destinations, hosts, and network interfaces that generate, transmit, and receive messages.
- A message is a stream of data that is sent from a source to a destination on a continuous basis.
- A message can be characterized by a tuple of inter-packet spacing (Pi), message length (ei), and reception deadline (Di), where Pi is the time interval between two consecutive packets of the same message, ei is the number of bits in a packet, and Di is the maximum allowable delay for a packet to reach its destination.
- This traffic model is called the peak rate model in RTC.
- The performance of RTC can be measured by metrics such as throughput, delay, and jitter.
- Throughput is the rate of successful message delivery over a communication channel.
- Delay is the time taken for a message to travel from the source to the destination.
- Jitter is the variation in delay among different packets of the same message.
- The goal of RTC is to maximize throughput, minimize delay, and reduce jitter.
- RTC can be achieved by using various techniques such as buffering, scheduling, routing, congestion control, error control, etc  .
- Buffering is the process of temporarily storing packets in a queue before sending or receiving them.
- Scheduling is the process of deciding the order and timing of packet transmission or reception.
- Routing is the process of finding the best path for a packet to travel from the source to the destination.
- Congestion control is the process of avoiding or reducing network congestion by regulating the traffic flow.
- Error control is the process of detecting and correcting errors in packet transmission or reception.