# CoAP Protocol

- CoAP stands for **Constrained Application Protocol** and it is defined in **RFC 7252** .
- CoAP is an **application-layer protocol** that is intended for use in **resource-constrained Internet devices**, such as wireless sensor network nodes.
- CoAP is designed to easily translate to **HTTP** for simplified integration with the web, while also meeting specialized requirements such as **multicast support**, **very low overhead**, and **simplicity**.
- CoAP is a **client-server protocol** that enables clients to make requests for web transfers as per the need of the hour and servers to respond to arriving requests.
- CoAP is based on the **REST** (Representational State Transfer) architectural style, which means that it follows a **stateless** and **uniform** interface for accessing resources.
- CoAP uses **UDP** (User Datagram Protocol) as the underlying transport layer protocol, which makes it suitable for unreliable and low-power networks.
- CoAP supports four types of **methods**: **GET**, **POST**, **PUT**, and **DELETE**, which correspond to the HTTP methods for retrieving, creating, updating, and deleting resources, respectively.
- CoAP also supports four types of **messages**: **Confirmable**, **Non-confirmable**, **Acknowledgement**, and **Reset**, which are used to ensure reliable and asynchronous communication.
- CoAP uses a simple binary format for encoding messages, which consists of a fixed **header** (4 bytes), a variable-length **token** (0-8 bytes), optional **options**, and an optional **payload**.
- CoAP defines a number of **options** that can be used to specify various parameters of the request or response, such as **Content-Type**, **Content-Format**, **URI-Path**, **URI-Query**, **Observe**, **Block**, etc.
- CoAP supports two types of **responses**: **Piggybacked** and **Separate**, which differ in the way they are delivered to the client. Piggybacked responses are sent within the acknowledgement message, while separate responses are sent as a new confirmable message.
- CoAP supports two types of **resource discovery** mechanisms: **.well-known/core** and **.well-known/linkformat**, which allow clients to query the server for the available resources and their attributes.
- CoAP supports two types of **security** mechanisms: **DTLS** (Datagram Transport Layer Security) and **OSCORE** (Object Security for Constrained RESTful Environments), which provide encryption, authentication, and integrity protection for CoAP messages.
- CoAP is an **IoT protocol** that has interesting features specifically designed for constrained devices. There are other IoT protocols useful to build IoT solutions, such as **MQTT**, **AMQP**, **DDS**, etc.