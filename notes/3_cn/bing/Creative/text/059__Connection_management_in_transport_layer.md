### Connection management in transport layer

- Connection management is the process of establishing, maintaining, and terminating a logical connection between two or more end points in a network.
- Connection management is one of the responsibilities of the transport layer, which provides end-to-end communication services for applications.
- Connection management can be either connection-oriented or connectionless, depending on the transport protocol used.
- Connection-oriented protocols, such as TCP, require a handshake procedure to set up and tear down a connection between two end points. This ensures reliable and ordered delivery of data, as well as flow and congestion control.
- Connectionless protocols, such as UDP, do not require a handshake procedure to establish or terminate a connection. They simply send and receive datagrams without any guarantee of delivery, order, or error detection. They are suitable for applications that require low latency and high throughput, such as streaming or gaming.
- Connection management involves the following steps:
  - Connection establishment: The initiator of the connection sends a request to the responder, who either accepts or rejects the request. A connection identifier, such as a port number, is assigned to each end point to uniquely identify the connection.
  - Data transfer: The end points exchange data using the agreed transport protocol. The data may be segmented, reassembled, acknowledged, retransmitted, or discarded, depending on the protocol features.
  - Connection termination: The end points signal their intention to close the connection, either gracefully or abruptly. The connection resources, such as buffers and timers, are released.