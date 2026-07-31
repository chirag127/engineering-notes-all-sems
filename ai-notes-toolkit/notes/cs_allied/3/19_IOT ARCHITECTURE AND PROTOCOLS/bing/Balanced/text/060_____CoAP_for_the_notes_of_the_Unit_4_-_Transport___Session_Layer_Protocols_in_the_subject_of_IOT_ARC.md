### CoAP

- CoAP stands for **Constrained Application Protocol** and it is defined in **RFC 7252** .
- CoAP is an **application-layer protocol** that is intended for use in **resource-constrained Internet devices**, such as wireless sensor network nodes.
- CoAP is designed to easily translate to **HTTP** for simplified integration with the web, while also meeting specialized requirements such as **multicast support**, **very low overhead**, and **simplicity**.
- CoAP is a **client-server protocol** that enables clients to make requests for web transfers and servers to respond to them.
- CoAP uses a **request/response** model similar to HTTP, but with some differences:
  - CoAP uses **UDP** as the underlying transport protocol, instead of TCP .
  - CoAP supports **asynchronous** message exchanges, where a request or a response can be sent without waiting for the previous one to be acknowledged .
  - CoAP messages can be of four types: **confirmable**, **non-confirmable**, **acknowledgment**, and **reset** .
  - CoAP messages have a **binary header** of 4 bytes, followed by optional **options** and a **payload** .
  - CoAP messages are identified by a **message ID** and a **token** .
  - CoAP supports **caching**, **proxying**, and **observing** of resources .
- CoAP is suitable for **IoT applications** that require low power consumption, low latency, and high reliability .
- CoAP can be used for various IoT scenarios, such as **smart home**, **smart city**, **industrial IoT**, **healthcare**, and **environmental monitoring**.