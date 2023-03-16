### MAC protocol survey for the notes of the Unit 4 - Network & Communication aspects in IoT in the subject of Internet of Things

- MAC (Medium Access Control) protocol is a sublayer of the data link layer that coordinates the access of multiple devices to a shared wireless medium.
- MAC protocol is essential for IoT (Internet of Things) applications that involve a large number of devices with diverse communication requirements and constraints.
- MAC protocol can be classified into two main categories: contention-based and contention-free.
- Contention-based MAC protocols allow devices to compete for the channel access without reservation or scheduling. They are suitable for low traffic and dynamic scenarios, but may suffer from collisions, overhead, and unfairness.
- Contention-free MAC protocols allocate the channel access to devices based on reservation or scheduling mechanisms. They can provide guaranteed quality of service (QoS) and efficiency, but may incur high complexity and latency.
- There are various MAC protocols designed for different IoT scenarios, such as IEEE 802.11ah, IEEE 802.15.4, LoRaWAN, NB-IoT, and Sigfox.
- IEEE 802.11ah, also known as WiFi HaLow, is a scalable solution for medium-range communication in IoT. It leverages various innovative medium access control techniques, such as restricted access window (RAW), target wake time (TWT), and group addressed transmission (GAT).
- IEEE 802.15.4 is a standard for low-rate wireless personal area networks (LR-WPANs) that supports various MAC protocols, such as beacon-enabled, non-beacon-enabled, and slotted CSMA/CA.
- LoRaWAN is a low-power wide-area network (LPWAN) protocol that uses a star-of-stars topology and a chirp spread spectrum (CSS) modulation. It employs a pure ALOHA MAC protocol with adaptive data rate (ADR) and duty cycle control.
- NB-IoT is a narrowband cellular IoT technology that operates in licensed spectrum. It uses a single-tone frequency division multiple access (FDMA) scheme and a hybrid automatic repeat request (HARQ) mechanism for uplink transmission, and a time division duplex (TDD) scheme for downlink transmission.
- Sigfox is an ultra-narrowband (UNB) IoT technology that operates in unlicensed spectrum. It uses a binary phase-shift keying (BPSK) modulation and a random access MAC protocol with frequency and time diversity.