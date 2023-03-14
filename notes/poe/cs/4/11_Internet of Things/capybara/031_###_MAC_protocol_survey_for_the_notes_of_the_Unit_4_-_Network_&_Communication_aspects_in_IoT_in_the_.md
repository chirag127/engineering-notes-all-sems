### MAC Protocol Survey for the Notes of Unit 4 - Network & Communication Aspects in IoT

In the field of Internet of Things (IoT), MAC (Medium Access Control) protocols are an essential aspect of communication between different devices. This protocol is responsible for controlling access to the shared medium and ensuring that no two devices transmit data at the same time, leading to collisions, which results in data loss.

Here are some of the MAC protocol survey notes that you should keep in mind while studying Unit 4 of the Network & Communication Aspects in IoT.

#### 1. CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)

CSMA/CA is a widely used MAC protocol in IoT. In this protocol, a device listens for a clear channel before transmitting data. If the channel is busy, the device waits for a random amount of time before checking again. This process ensures that no two devices transmit data at the same time, leading to collisions.

Mnemonic: C-CA, where C stands for Carrier Sense and CA stands for Collision Avoidance.

#### 2. TDMA (Time Division Multiple Access)

TDMA is a MAC protocol that divides the available bandwidth into time slots. Each device is assigned a specific time slot in which it can transmit data. This protocol ensures that no two devices transmit data at the same time, leading to collisions.

Mnemonic: T-TDMA, where T stands for Time Division.

#### 3. FDMA (Frequency Division Multiple Access)

FDMA is a MAC protocol that divides the available bandwidth into different frequency bands. Each device is assigned a specific frequency band in which it can transmit data. This protocol ensures that no two devices transmit data on the same frequency band, leading to collisions.

Mnemonic: F-FDMA, where F stands for Frequency Division.

#### 4. Aloha

Aloha is a simple MAC protocol that allows devices to transmit data whenever they have data to send. If two devices transmit data at the same time, a collision occurs, and both devices wait for a random amount of time before trying again.

Mnemonic: None.

#### Advantages and Disadvantages of Different MAC Protocols

| MAC Protocol | Advantages | Disadvantages |
|--------------|------------|---------------|
| CSMA/CA      | Efficient use of bandwidth, Collision avoidance | Slow with high network traffic |
| TDMA         | Efficient use of bandwidth, Low latency | Requires precise synchronization |
| FDMA         | Efficient use of bandwidth, Low interference | Requires precise frequency allocation |
| Aloha        | Simple, Low implementation cost | High collision rate, Low efficiency |

#### Applications of Different MAC Protocols

| MAC Protocol | Applications |
|--------------|--------------|
| CSMA/CA      | Wi-Fi, Bluetooth, Zigbee |
| TDMA         | GSM, TETRA, P25 |
| FDMA         | AM and FM radio, TV broadcasting |
| Aloha        | RFID, Satellite communication |

These are some of the MAC protocol survey notes that you should keep in mind while studying Unit 4 of the Network & Communication Aspects in IoT. Understanding these protocols will help you design and implement efficient communication networks for IoT devices.