The following is a detailed ASCII diagram for Wireless Medium access issues for the notes of the Unit 4 - Network & Communication aspects in IoT in the subject of Internet of Things.

### Wireless Medium access issues

The wireless medium access issues in IoT are mainly related to the following aspects:

- Medium Access Control (MAC) protocol: The MAC protocol is responsible for coordinating the data transmission among various IoT devices. However, to achieve high network throughput, low energy consumption, and low latency, various challenges at the MAC layer must be overcome, such as interference, hidden terminal problem, exposed terminal problem, and fairness.
- Wireless interference: Wireless interference is the unwanted signal that disrupts the communication between the intended transmitter and receiver. Wireless interference can be caused by various sources, such as other wireless devices, microwave ovens, cordless phones, Bluetooth devices, etc. Wireless interference can degrade the network performance, increase the packet loss, and reduce the energy efficiency of the IoT devices .
- Wireless security: Wireless security is the protection of the wireless network and the data transmitted over it from unauthorized access, modification, or disclosure. Wireless security is challenging in IoT due to the resource constraints of the IoT devices, the dynamic and heterogeneous nature of the IoT network, and the lack of a centralized authority. Wireless security issues in IoT include authentication, encryption, key management, privacy, and trust .

The following diagram illustrates the basic architecture of a wireless IoT network and some of the wireless medium access issues:

```
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|  IoT device 1   |   |  IoT device 2   |   |  IoT device 3   |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|  Access Point   |   |  Interference   |   |  Eavesdropper   |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
+-----------------+
|                 |
|  Internet       |
|                 |
+-----------------+
```

- The access point is the device that connects the IoT devices to the Internet. It can also provide wireless power to the IoT devices using wireless energy harvesting techniques.
- The interference is the unwanted signal that disrupts the communication between the IoT devices and the access point. It can be caused by various sources, such as other wireless devices, microwave ovens, cordless phones, Bluetooth devices, etc.
- The eavesdropper is the malicious device that tries to intercept the data transmitted over the wireless medium. It can also launch active attacks, such as jamming, spoofing, replaying, etc.
- The IoT devices are the devices that collect, process, and transmit data over the wireless medium. They can be sensors, actuators, smart phones, wearable devices, etc. They have limited resources, such as battery, memory, processing power, etc.
- The hidden terminal problem occurs when two IoT devices that are out of the range of each other try to communicate with the access point at the same time, causing a collision at the access point.
- The exposed terminal problem occurs when an IoT device that is in the range of another IoT device and the access point refrains from transmitting to the access point because it senses that the other IoT device is transmitting, even though there is no collision at the access point.
- The fairness problem occurs when some IoT devices get more access to the wireless medium than others, due to factors such as distance, interference, priority, etc.