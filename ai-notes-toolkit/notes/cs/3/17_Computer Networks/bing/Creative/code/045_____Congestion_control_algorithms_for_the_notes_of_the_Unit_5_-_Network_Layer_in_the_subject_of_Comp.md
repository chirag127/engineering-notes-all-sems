# Congestion control algorithms

Congestion control algorithms are methods to regulate the flow of data packets in a network, in order to avoid congestion and improve the performance and efficiency of the network. Congestion occurs when the demand for network resources exceeds the available capacity, resulting in packet losses, delays, and reduced throughput. Congestion control algorithms aim to prevent or reduce congestion by adjusting the sending rate of the data sources, based on the feedback from the network or the receivers.

There are two main types of congestion control algorithms: open loop and closed loop.

## Open loop congestion control

Open loop congestion control algorithms try to prevent congestion before it happens, by applying some policies or rules at the data sources or the network routers. For example, some open loop congestion control algorithms are:

- Admission control: A data source must obtain permission from the network before sending data, based on the availability of network resources.
- Traffic shaping: A data source must limit its sending rate to a predefined value, or follow a certain pattern of sending data, such as the leaky bucket or the token bucket algorithms.
- Load shedding: A network router must drop some packets when the buffer is full or the load is high, based on some criteria such as priority, timestamp, or random selection.
- Resource reservation: A data source must reserve some network resources, such as bandwidth or buffer space, for its data transmission, using protocols such as RSVP (Resource Reservation Protocol).

## Closed loop congestion control

Closed loop congestion control algorithms try to reduce congestion after it happens, by adjusting the sending rate of the data sources based on the feedback from the network or the receivers. For example, some closed loop congestion control algorithms are:

- Backpressure: A network router must send a signal to the upstream data sources to slow down or stop sending data, when the buffer is full or the load is high.
- Choke packet: A network router must send a special packet to the data source that caused congestion, instructing it to reduce its sending rate.
- Explicit Congestion Notification (ECN): A network router must mark some packets with a special bit, indicating that there is congestion in the network, and the receivers must send this information back to the data sources, using protocols such as TCP (Transmission Control Protocol).
- Congestion window: A data source must maintain a variable that represents the amount of data that can be sent without causing congestion, and adjust it based on the feedback from the network or the receivers, using algorithms such as TCP Reno, TCP Tahoe, TCP Vegas, or TCP Cubic.