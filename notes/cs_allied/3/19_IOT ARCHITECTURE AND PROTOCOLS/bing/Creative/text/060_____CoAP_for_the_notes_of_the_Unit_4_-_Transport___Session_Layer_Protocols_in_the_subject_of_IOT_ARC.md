### CoAP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- CoAP stands for **Constrained Application Protocol**  .
- CoAP is an **application-layer protocol** that is intended for use in **resource-constrained Internet devices**, such as wireless sensor network nodes.
- CoAP is designed to enable simple, constrained devices to join the **Internet of Things (IoT)** even through constrained networks with low bandwidth and low availability.
- CoAP is defined in **RFC 7252**  and is based on the **REST** (Representational State Transfer) architectural style.
- CoAP is designed to easily translate to **HTTP** for simplified integration with the web, while also meeting specialized requirements such as multicast support, very low overhead, and simplicity.
- CoAP uses **UDP** (User Datagram Protocol) as the underlying transport layer protocol, and provides reliability, congestion control, and message deduplication mechanisms.
- CoAP supports four types of **request methods**: GET, PUT, POST, and DELETE, and four types of **response codes**: 2.xx (success), 4.xx (client error), 5.xx (server error), and 1.xx (informational).
- CoAP supports **URI** (Uniform Resource Identifier) for identifying resources, and **content negotiation** for selecting the appropriate representation format.
- CoAP supports **observe** option for enabling clients to subscribe to resources and receive notifications of state changes.
- CoAP supports **security** features such as encryption, authentication, and authorization through **DTLS** (Datagram Transport Layer Security).