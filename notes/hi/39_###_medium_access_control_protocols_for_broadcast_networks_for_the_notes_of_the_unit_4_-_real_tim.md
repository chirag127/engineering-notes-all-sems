### Medium Access Control Protocols for Broadcast Networks for the notes of the Unit 4 - Real Time Communication in the subject of Real Time System
Medium Access Control (MAC) protocols are used in broadcast networks to regulate the access of nodes to the shared communication medium. The following are the main types of MAC protocols for broadcast networks: 

1. Aloha: a simple and first MAC protocol that operates on a first-come, first-served basis. Nodes transmit whenever they have data to send. If two nodes transmit at the same time, a collision occurs, and both transmissions are lost. 

2. CSMA/CD: Carrier Sense Multiple Access with Collision Detection. Nodes listen to the medium before transmitting. If the medium is busy, the node waits until it is free. If two nodes transmit at the same time, a collision occurs, and both transmissions are lost. 

3. CSMA/CA: Carrier Sense Multiple Access with Collision Avoidance. Nodes listen to the medium before transmitting. If the medium is busy, the node waits until it is free. If two nodes want to transmit at the same time, they use a random backoff algorithm to avoid collisions. 

4. TDMA: Time Division Multiple Access. The medium is divided into time slots, and each node is assigned a specific time slot to transmit. 

5. FDMA: Frequency Division Multiple Access. The medium is divided into frequency bands, and each node is assigned a specific frequency band to transmit. 

6. Hybrid MAC: A combination of any of the above MAC protocols to provide a more efficient communication system.
