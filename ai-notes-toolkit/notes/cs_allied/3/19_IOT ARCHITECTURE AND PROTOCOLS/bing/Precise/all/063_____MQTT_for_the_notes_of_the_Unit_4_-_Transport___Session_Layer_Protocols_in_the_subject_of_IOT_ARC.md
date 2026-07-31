### MQTT

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol that is used for machine-to-machine (M2M) communication. It is designed for connections with remote locations where a small code footprint is required and/or network bandwidth is limited. MQTT is one of the most commonly used protocols in IoT and IIoT infrastructure.

#### MQTT Architecture

The MQTT architecture is made up of the following key parts: MQTT broker and MQTT client. MQTT uses a publisher-subscriber pattern and is ideal for small devices that require efficient bandwidth and battery use.

#### MQTT Protocol

MQTT’s support for persistent sessions reduces the time to reconnect the client with the broker. MQTT makes it easy to encrypt messages using TLS and authenticate clients using modern authentication protocols, such as OAuth.

#### MQTT Use Cases

Wireless IoT technologies such as Zigbee and LoRaWAN use MQTT for communication between clients and router. Protocols such as AMPQ, CoAP, and JMS also use a broker-based architecture.

#### Transport Layer

In any IoT protocol, the transport layer enables and safeguards the communication of the data as it travels between layers. Transmission Control Protocol (TCP) is used in MQTT.