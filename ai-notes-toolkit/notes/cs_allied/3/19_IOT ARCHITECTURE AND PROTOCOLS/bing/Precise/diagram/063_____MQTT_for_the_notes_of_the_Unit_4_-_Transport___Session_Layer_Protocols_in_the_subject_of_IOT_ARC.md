### MQTT

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol designed for machine-to-machine (M2M) communication. It is commonly used in IoT (Internet of Things) and IIoT (Industrial Internet of Things) infrastructure .

#### MQTT Architecture

The MQTT architecture is made up of two key parts: the MQTT broker and the MQTT client. The broker is responsible for receiving messages from clients and distributing them to the appropriate subscribers. The client is responsible for publishing messages to the broker and subscribing to topics to receive messages .

#### MQTT Protocol

MQTT uses a publish/subscribe pattern, which is ideal for small devices that require efficient bandwidth and battery use. The protocol supports persistent sessions, which reduces the time to reconnect the client with the broker. MQTT also makes it easy to encrypt messages using TLS and authenticate clients using modern authentication protocols, such as OAuth .

#### MQTT Use Cases

MQTT is used in a variety of IoT applications, including wireless IoT technologies such as Zigbee and LoRaWAN. Other protocols, such as AMPQ, CoAP, and JMS, also use a broker-based architecture similar to MQTT .

#### Transport Layer

In any IoT protocol, the transport layer enables and safeguards the communication of data as it travels between layers. MQTT uses the Transmission Control Protocol (TCP) as its transport layer .