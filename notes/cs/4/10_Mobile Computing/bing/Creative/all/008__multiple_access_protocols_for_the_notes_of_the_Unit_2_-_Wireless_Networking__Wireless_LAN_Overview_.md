### Multiple access protocols for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless

- Multiple access protocols are used to coordinate the access of multiple stations to a shared medium, such as a wireless channel or a wired LAN.
- Multiple access protocols can be classified into three categories: random access, controlled access, and channelization.
- Random access protocols allow any station to transmit at any time without coordination with other stations. However, this may result in collisions, which degrade the performance and require retransmission mechanisms. Examples of random access protocols are ALOHA, CSMA, CSMA/CA, and CSMA/CD.
- Controlled access protocols require stations to obtain permission before transmitting. This can avoid collisions and improve the efficiency of the channel. However, this may introduce delay and overhead. Examples of controlled access protocols are reservation, polling, and token passing.
- Channelization protocols divide the channel into smaller units, such as time slots, frequency bands, or codes, and assign them to different stations. This can prevent interference and allow simultaneous transmissions. However, this may waste bandwidth and require synchronization. Examples of channelization protocols are TDMA, FDMA, and CDMA.

#### ALOHA
- ALOHA is a simple random access protocol that was developed for wireless networks, such as ALOHAnet.
- ALOHA does not require any carrier sensing or coordination among stations. Any station can transmit a frame whenever it has data to send.
- ALOHA has two variants: pure ALOHA and slotted ALOHA.
- Pure ALOHA does not impose any timing structure on the transmissions. A station can transmit at any arbitrary time. However, this increases the probability of collisions, as two or more frames may overlap partially or completely.
- Slotted ALOHA divides the time into equal-sized slots, and requires stations to transmit only at the beginning of a slot. This reduces the collision probability by half, as only frames that start in the same slot can collide.
- ALOHA has a low throughput and efficiency, as only a fraction of the channel capacity is utilized. The maximum throughput of pure ALOHA is about 18%, and the maximum throughput of slotted ALOHA is about 37%.
- ALOHA is suitable for networks with low traffic and sporadic transmissions, such as satellite networks.

#### CSMA
- CSMA stands for Carrier Sense Multiple Access. It is a random access protocol that improves on ALOHA by using carrier sensing to reduce collisions.
- CSMA requires stations to sense the channel before transmitting. If the channel is idle, the station can transmit. If the channel is busy, the station can defer its transmission until the channel becomes idle.
- CSMA has three variants: 1-persistent CSMA, nonpersistent CSMA, and p-persistent CSMA.
- 1-persistent CSMA is the simplest and most aggressive variant. A station that has a frame to send senses the channel. If the channel is idle, it transmits immediately. If the channel is busy, it waits until the channel becomes idle, and then transmits immediately. This may result in collisions, as two or more stations may sense the channel at the same time and transmit simultaneously.
- Nonpersistent CSMA is the least aggressive variant. A station that has a frame to send senses the channel. If the channel is idle, it transmits immediately. If the channel is busy, it waits for a random period of time, and then senses the channel again. This may reduce collisions, as stations do not transmit at the same time. However, this may increase the delay, as stations may wait for a long time before transmitting.
- p-persistent CSMA is a compromise between 1-persistent CSMA and nonpersistent CSMA. It is used for slotted channels, where time is divided into slots. A station that has a frame to send senses the channel at the beginning of a slot. If the channel is idle, it transmits with a probability p, and defers with a probability 1-p. If the channel is busy, it waits until the next slot, and repeats the process. This may balance the trade-off between collision and delay, as stations have a chance to transmit or defer in each slot.
- CSMA has a higher throughput and efficiency than ALOHA, as it avoids transmitting when the channel is busy. However, CSMA cannot eliminate collisions completely, as there is a propagation delay between the sender and the receiver, and the channel status may change during this time.

#### CSMA