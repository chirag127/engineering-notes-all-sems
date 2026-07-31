# AMQP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- AMQP stands for **Advanced Message Queuing Protocol**.
- It is an **open standard**, **binary** application layer protocol designed for **message-oriented middleware**.
- It enables **encrypted** and **interoperable** messaging between organizations and applications.
- It is used in **client/server messaging** and in **IoT device management**.
- It has **reliable**, **secure**, **interoperable**, **open**, and **standard** properties, along with its **low overhead** characteristics, making it a good solution for IoT applications.
- It supports **publish/subscribe**, **point-to-point**, and **request/response** messaging patterns.
- It standardizes messaging using **Producers**, **Brokers** and **Consumers**.
- Producers send messages to a **broker** (a server that routes messages to the appropriate destinations).
- Consumers receive messages from a broker, either by **subscribing** to a **topic** (a logical name for a group of messages) or by **polling** a **queue** (a buffer that stores messages until they are consumed or expire).
- AMQP defines a **wire-level protocol**, which means that the messages are **binary** and can be efficiently parsed by any platform.
- AMQP also defines a **semantic model**, which specifies the **meaning** and **behavior** of the messages and the entities involved in the communication.
- AMQP uses **TCP** as the underlying transport protocol, and optionally **TLS** for encryption.
- AMQP can also use **WebSockets** as a transport layer, which allows it to work over **HTTP**.
- To connect to an IoT hub by using AMQP, a client can use the **claims-based security (CBS)** or **Simple Authentication and Security Layer (SASL)** authentication.
- The client needs to provide the **IoT hub hostname**, the **key name**, and the **key value** for authentication.
- The client can then create a **sender link** or a **receiver link** to send or receive messages to or from the IoT hub.
- AMQP supports **device-to-cloud** and **cloud-to-device** communications, as well as **device twins**, **direct methods**, and **file upload** features of IoT Hub.