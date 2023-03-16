### Cryptographic controls built into IoT messaging and communication protocols

- Cryptographic controls are methods of applying security to information and communications using codes, keys, algorithms, and protocols.
- Cryptographic controls are essential for IoT devices, which often communicate over wireless networks and exchange sensitive data with other devices, servers, or cloud platforms.
- Cryptographic controls can provide authentication, data integrity, confidentiality, and non-repudiation for IoT communications.
- Authentication is the process of verifying the identity of the sender and the receiver of a message, ensuring that they are who they claim to be.
- Data integrity is the property that the message has not been altered, corrupted, or tampered with during transmission or storage.
- Confidentiality is the property that the message is only accessible to the authorized parties, and not to any unauthorized or malicious third parties.
- Non-repudiation is the property that the sender and the receiver of a message cannot deny having sent or received it, respectively.
- Cryptographic controls can be implemented at different layers of the IoT communication stack, such as the physical, network, transport, or application layer.
- Cryptographic controls can also be integrated into specific IoT protocols, such as ZigBee, Z-Wave, Bluetooth Low Energy (BLE), MQTT, CoAP, or DTLS.
- ZigBee, Z-Wave, and BLE are wireless protocols that support the creation of mesh networks of IoT devices, which can communicate with each other and with a gateway or hub device.
- ZigBee, Z-Wave, and BLE all have options for applying cryptographic controls, such as using symmetric or asymmetric encryption, digital signatures, message authentication codes, or key management schemes.
- MQTT and CoAP are application layer protocols that enable IoT devices to publish and subscribe to messages from a broker or a server, using a publish/subscribe or a request/response model, respectively.
- MQTT and CoAP both support the use of Transport Layer Security (TLS) or Datagram Transport Layer Security (DTLS) to secure the communication channel between the IoT device and the broker or server, using encryption, authentication, and integrity protection.
- DTLS is a variant of TLS that is designed for unreliable and datagram-based transport protocols, such as UDP, which are often used by IoT devices.
- DTLS provides the same security features as TLS, but with some modifications to handle packet loss, reordering, and duplication.