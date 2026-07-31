#### Layering principles with reference to Network Architecture in Computer Networks

- Layering is a design principle that divides a complex system into smaller and simpler components, called layers, that can be managed independently.
- Each layer has a specific function and provides services to the layer above it, while using the services of the layer below it.
- Layering allows for modularity, interoperability, scalability, and flexibility of network systems, as well as hiding the implementation details of each layer from other layers.
- The most widely used layered network architecture is the Open Systems Interconnection (OSI) model, which consists of seven layers: physical, data link, network, transport, session, presentation, and application.
- The OSI model defines the functions, protocols, and interfaces of each layer, and serves as a reference for developing and standardizing network protocols and devices.
- The following table summarizes the main features and examples of each layer of the OSI model:

| Layer | Function | Protocols | Devices |
| --- | --- | --- | --- |
| Physical | Transmits raw bits over a physical medium | Ethernet, RS-232, Bluetooth | Hubs, repeaters, cables |
| Data link | Provides reliable and error-free transmission of frames between adjacent nodes | HDLC, PPP, MAC, LLC | Switches, bridges, NICs |
| Network | Provides logical addressing and routing of packets across networks | IP, ICMP, ARP, RIP, OSPF | Routers, firewalls, gateways |
| Transport | Provides end-to-end reliable and ordered delivery of data segments | TCP, UDP, SCTP | N/A |
| Session | Establishes, maintains, and terminates sessions between applications | RPC, NFS, SQL, NetBIOS | N/A |
| Presentation | Translates, encrypts, and compresses data for the application layer | SSL, TLS, JPEG, GIF | N/A |
| Application | Provides user interface and high-level services for network applications | HTTP, FTP, SMTP, DNS, Telnet | Web browsers, email clients, servers |

- A possible mnemonic to remember the order of the OSI layers from bottom to top is: **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way.