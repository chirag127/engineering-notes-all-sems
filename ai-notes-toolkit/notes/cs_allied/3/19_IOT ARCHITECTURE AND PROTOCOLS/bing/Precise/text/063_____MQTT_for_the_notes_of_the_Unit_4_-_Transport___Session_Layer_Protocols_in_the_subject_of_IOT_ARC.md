### MQTT

MQTT (Message Queuing Telemetry Transport) is an OASIS standard messaging protocol for the Internet of Things (IoT). It is designed as an extremely lightweight publish/subscribe messaging transport that is ideal for connecting remote devices with a small code footprint and minimal network bandwidth .

#### MQTT Architecture and Protocol Overview

The MQTT architecture is made up of the following key parts: MQTT broker and MQTT client . MQTT uses a publisher-subscriber pattern and is ideal for small devices that require efficient bandwidth and battery use .

#### Security

MQTT makes it easy to encrypt messages using TLS and authenticate clients using modern authentication protocols, such as OAuth .

#### Use Cases

MQTT is one of the most commonly used protocols in IoT and IIoT infrastructure such as process . Many IoT devices connect over unreliable cellular networks. MQTT’s support for persistent sessions reduces the time to reconnect the client with the broker . Wireless IoT technologies such as Zigbee, LoRaWAN use MQTT for communication between clients and router .

#### Comparison with Other Protocols

Protocols such as AMPQ, CoAP, and JMS also use broker-based architecture .