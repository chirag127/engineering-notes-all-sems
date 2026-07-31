 Here is the content in Markdown format with formal tone and without external links or emojis:

### Forwarding and Delivery in Network Layer

1. Forwarding: The process of transferring data packets from input link to appropriate output link in a router is called forwarding. The router uses forwarding table to determine the output interface based on destination address.
2. Forwarding Table: The forwarding table contains routing information to forward the packets. It maps the destination IP address to the output interface. The forwarding table is built using routing protocols.
3. Delivery: The final process of transferring packets from router to destination device is called delivery. Once the packets reach the destination router, it delivers the packets to the destination device. The destination device then reassembles the packets and passes the data to application.
4. Additional Function: In addition to forwarding and delivery, network layer is also responsible for functions like:
- Addressing: IP addresses are assigned to devices at network layer.
- Routing: The process of selecting best path to forward packets is done using routing protocols at network layer.
- Fragmentation: The large packets are fragmented into smaller packets for transmission at network layer. The fragmented packets are reassembled at the destination.
- Time To Live: TTL field in IP header specifies lifetime of packets. If TTL expires before packets reach destination, they are discarded.

The above points cover the key concepts of forwarding and delivery processes in network layer. Let me know if you would like me to elaborate on any of the points.