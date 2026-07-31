### CoAP

- CoAP stands for **Constrained Application Protocol** and it is defined in **RFC 7252** .
- CoAP is an **application-layer protocol** that is intended for use in **resource-constrained Internet devices**, such as wireless sensor network nodes.
- CoAP is designed to easily translate to **HTTP** for simplified integration with the web, while also meeting specialized requirements such as **multicast support**, **very low overhead**, and **simplicity**.
- CoAP is a **client-server protocol** that enables clients to make requests for web transfers and servers to respond to them.
- CoAP is based on the **REST** (Representational State Transfer) architectural style, which means that resources are identified by **URIs** (Uniform Resource Identifiers) and manipulated by using **methods** such as GET, PUT, POST, and DELETE.
- CoAP uses **UDP** (User Datagram Protocol) as the underlying transport layer, which makes it suitable for unreliable and low-power networks.
- CoAP supports **asynchronous message exchanges** by using a **message ID** and a **token** to match requests and responses.
- CoAP also supports **reliability** and **congestion control** by using a **retransmission mechanism** and an **exponential back-off algorithm**.
- CoAP defines two types of messages: **confirmable** and **non-confirmable**. Confirmable messages require an acknowledgement from the receiver, while non-confirmable messages do not.
- CoAP also defines two optional types of messages: **acknowledgement** and **reset**. Acknowledgement messages are sent to confirm the receipt of a confirmable message, while reset messages are sent to reject a confirmable message.
- CoAP uses a **four-byte header** that contains the following fields: **version**, **type**, **token length**, and **code**.
- CoAP also uses a **variable-length token** that is used to correlate requests and responses, and a **variable-length options** that are used to specify parameters such as **content format**, **URI path**, **observe**, and **block**.
- CoAP supports **observe** option that allows clients to subscribe to a resource and receive notifications when it changes.
- CoAP supports **block** option that allows large transfers to be split into smaller blocks and exchanged incrementally.
- CoAP is an **IoT protocol** that has interesting features specifically designed for constrained devices. There are other IoT protocols useful to build IoT solutions, such as **MQTT**, **AMQP**, **DDS**, and so on .