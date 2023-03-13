The layering principles with reference to network architecture in computer networks are based on the idea of dividing the communication process into smaller and manageable parts, each with a specific function and interface. One of the most widely used models of network architecture is the Open Systems Interconnection (OSI) model, which consists of seven layers: physical, data link, network, transport, session, presentation, and application. The following diagram illustrates the basic architecture of the OSI model using ASCII characters:

```
+------------------------+
| Application            |  <---->  Application layer protocols (e.g. HTTP, FTP, SMTP, etc.)
+------------------------+
| Presentation           |  <---->  Data representation and encryption (e.g. ASCII, JPEG, SSL, etc.)
+------------------------+
| Session                |  <---->  Session management and synchronization (e.g. RPC, NFS, SQL, etc.)
+------------------------+
| Transport              |  <---->  Reliable and unreliable data delivery (e.g. TCP, UDP, etc.)
+------------------------+
| Network                |  <---->  Routing and addressing (e.g. IP, ICMP, ARP, etc.)
+------------------------+
| Data Link              |  <---->  Error detection and correction (e.g. Ethernet, PPP, HDLC, etc.)
+------------------------+
| Physical               |  <---->  Transmission medium and signal encoding (e.g. copper, fiber, radio, etc.)
+------------------------+
```