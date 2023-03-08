### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols are mechanisms that allow several users or transmitters to access a common medium or channel.
- MAC protocols play an important role in the development of both wired and wireless networks, especially for real-time communication.
- MAC protocols can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based.
- Probabilistic contention protocols, such as carrier sense multiple access/collision detection (CSMA/CD), are based on a first-come, first-serve approach, where each user tries to access the channel with a certain probability and backs off if a collision is detected.
- Deterministic contention protocols, such as time division multiple access (TDMA) or frequency division multiple access (FDMA), are based on a predefined order or allocation of the channel resources, where each user is assigned a time slot or a frequency band to access the channel.
- Reservation-based protocols, such as polling or token passing, are based on a centralized or distributed control of the channel access, where each user requests or obtains a permission to access the channel.
- The choice of the MAC protocol depends on the characteristics and requirements of the network, such as the number of users, the traffic pattern, the channel reliability, the delay constraints, and the energy consumption.
- For broadcast networks, where a single transmitter can reach all the receivers in the network, the MAC protocol should support reliable broadcast transmission, which means that all the intended receivers should receive the transmitted message correctly.
- Reliable broadcast transmission is challenging in broadcast networks due to the possibility of collisions, interference, channel errors, and hidden terminals.
- Collisions occur when two or more users try to access the channel at the same time, resulting in a corrupted message.
- Interference occurs when the signal from a user is affected by the signals from other users or sources, resulting in a degraded message quality.
- Channel errors occur when the signal from a user is distorted by the noise or fading of the channel, resulting in a erroneous message.
- Hidden terminals occur when a user cannot sense the presence of another user who is accessing the channel, resulting in a collision.
- To achieve reliable broadcast transmission in broadcast networks, the MAC protocol should provide mechanisms to avoid or resolve collisions, mitigate interference, cope with channel errors, and deal with hidden terminals.
- Some of the mechanisms that can be used are:

  - Collision avoidance: using techniques such as carrier sensing, random backoff, or channel reservation to reduce the probability of collisions.
  - Collision detection: using techniques such as listening to the channel feedback, sending acknowledgments, or using error detection codes to detect collisions and retransmit the message if needed.
  - Collision resolution: using techniques such as binary exponential backoff, contention resolution algorithms, or adaptive transmission rates to resolve collisions and improve the channel utilization.
  - Interference mitigation: using techniques such as power control, frequency hopping, or spread spectrum to reduce the impact of interference on the message quality.
  - Error control: using techniques such as forward error correction, automatic repeat request, or hybrid ARQ to correct or recover from channel errors and improve the message reliability.
  - Hidden terminal solution: using techniques such as request-to-send/clear-to-send (RTS/CTS) handshake, busy tone, or directional antennas to avoid or eliminate hidden terminals and prevent collisions.

- An example of a MAC protocol that supports reliable broadcast transmission in broadcast networks is the adaptive MAC protocol proposed by Zaruba et al. , which adapts the transmission rate and the retransmission strategy based on the channel conditions and the feedback from the receivers.

Some possible mnemonics and learning tricks for the topic are:

- To remember the types of MAC protocols, you can use the acronym PDR, which stands for Probabilistic, Deterministic, and Reservation-based.
- To remember the challenges of reliable broadcast transmission in broadcast networks, you can use the acronym CICH, which stands for Collisions, Interference, Channel errors, and Hidden terminals.
- To remember the mechanisms to achieve reliable broadcast transmission in broadcast networks, you can use the acronym CIECH, which stands for Collision avoidance, Collision detection, Collision resolution, Interference mitigation, Error control, and Hidden terminal solution.