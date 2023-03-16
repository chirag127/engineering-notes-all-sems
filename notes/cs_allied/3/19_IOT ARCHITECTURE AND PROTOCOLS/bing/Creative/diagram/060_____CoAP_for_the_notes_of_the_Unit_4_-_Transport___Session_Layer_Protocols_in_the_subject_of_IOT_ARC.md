### CoAP

- CoAP stands for **Constrained Application Protocol** and it is defined in **RFC 7252** .
- CoAP is an **application-layer protocol** that is intended for use in **resource-constrained Internet devices**, such as wireless sensor network nodes.
- CoAP is designed to easily translate to **HTTP** for simplified integration with the web, while also meeting specialized requirements such as **multicast support**, **very low overhead**, and **simplicity**.
- CoAP is a **client-server protocol** that enables clients to make requests for web transfers and servers to respond to them.
- CoAP is based on the **REST** (Representational State Transfer) model, which means that resources are identified by **URIs** (Uniform Resource Identifiers) and manipulated by **methods** such as GET, PUT, POST, and DELETE.
- CoAP uses **UDP** (User Datagram Protocol) as the underlying transport layer, which makes it suitable for unreliable and low-power networks.
- CoAP supports **asynchronous message exchanges** by using a **message ID** and a **token** to match requests and responses.
- CoAP also supports **reliability** by using a simple **stop-and-wait retransmission** mechanism with exponential back-off for messages marked as **confirmable**.
- CoAP provides **security** by using **DTLS** (Datagram Transport Layer Security), which is a variant of TLS (Transport Layer Security) for UDP.
- CoAP has interesting features specifically designed for constrained devices, such as **observe**, which allows clients to subscribe to resource updates, and **block**, which allows large transfers to be split into smaller blocks.