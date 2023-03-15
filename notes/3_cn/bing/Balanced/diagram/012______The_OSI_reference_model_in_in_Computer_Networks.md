The OSI reference model is a seven-layered architecture that describes how information from a software application in one computer moves through a physical medium to the software application in another computer. Each layer performs a particular network function and communicates with the adjacent layers through interfaces  .

The following diagram shows the OSI reference model in Computer Networks:

```
+------------------------+
| Application Layer      |  <--- Layer 7: Provides services to user applications
+------------------------+
| Presentation Layer     |  <--- Layer 6: Translates data formats and encryption
+------------------------+
| Session Layer          |  <--- Layer 5: Manages communication sessions
+------------------------+
| Transport Layer        |  <--- Layer 4: Provides reliable data transfer
+------------------------+
| Network Layer          |  <--- Layer 3: Routes packets across networks
+------------------------+
| Data Link Layer        |  <--- Layer 2: Transmits frames over physical links
+------------------------+
| Physical Layer         |  <--- Layer 1: Transfers bits over physical medium
+------------------------+
```