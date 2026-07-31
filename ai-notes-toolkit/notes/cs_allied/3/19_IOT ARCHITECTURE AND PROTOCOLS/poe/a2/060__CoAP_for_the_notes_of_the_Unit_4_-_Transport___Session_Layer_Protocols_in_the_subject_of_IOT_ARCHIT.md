 Here is the content in markdown format without any emojis or external links:

### CoAP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. CoAP stands for Constrained Application Protocol. It is a web transfer protocol designed for use with constrained nodes and constrained networks in the Internet of Things (IoT).

2. CoAP is designed to easily interface with HTTP for integration with the web, while meeting specialized requirements such as multicast support and very low overhead.

3. CoAP uses a request/response model between application endpoints. This model is similar in concept to HTTP, but with fewer features, lower overhead, and simpler implementation requirements suitable for constrained environments.

4. CoAP supports four types of messages:

- CONFIRMABLE (CON): Request messages that require acknowledgement
- NON-CONFIRMABLE (NON): Request messages that do not require acknowledgement
- ACKNOWLEDGEMENT (ACK): Used to confirm a CON message
- RESET (RST): Used to reject a message and return the client to its initial state

5. CoAP endpoints can be discovered using link-local multicast address (IPv6) or a well known port (UDP/IP). This makes it more suitable for constrained networks and saves bandwidth.

6. CoAP uses either UDP or DTLS as the underlying transport protocol. UDP provides a simple transport service without the overhead of TCP. DTLS provides security at the transport layer, using TLS over UDP.

7. The key features of CoAP are:

- Request/Response model: Similar to HTTP
- Low overhead: Suitable for constrained environments and networks
- Multicast support: Makes it suitable for IoT
- Supports UDP/DTLS as transport
- Mapped easily to HTTP for integration with web
- Supports asynchronous message exchanges
- Includes support for discovery of resources and endpoints

That's all for the notes on CoAP for the given topic. I have written the content in points in a formal tone without any feeling or friendliness and without using emojis or external links as instructed. Please let me know if you would like me to modify or expand the answer.