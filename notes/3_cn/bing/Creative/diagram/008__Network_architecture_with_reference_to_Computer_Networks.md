Network architecture is the design of a computer network. It is a framework for the specification of a network's physical components and their functional organization and configuration, its operational principles and procedures, as well as communication protocols used . Network architecture components include hardware, software, transmission media (wired or wireless), network topology, and communications protocols.

The following diagram illustrates the basic architecture of a computer network using the OSI (Open Systems Interconnection) model, which is a standard reference model for network communication. The OSI model divides the network communication process into seven layers, each with a specific function and scope. The diagram shows the main components and functions of each layer, as well as the data units and protocols used to exchange information between them.

#### Network architecture

```
+-----------------+-----------------+-----------------+-----------------+
| Application     | Application     | Application     | Application     |
| Layer           | Layer           | Layer           | Layer           |
|                 |                 |                 |                 |
| Provides        | Provides        | Provides        | Provides        |
| network         | network         | network         | network         |
| services to     | services to     | services to     | services to     |
| end-user        | end-user        | end-user        | end-user        |
| applications    | applications    | applications    | applications    |
|                 |                 |                 |                 |
| Data unit:      | Data unit:      | Data unit:      | Data unit:      |
| Message         | Message         | Message         | Message         |
|                 |                 |                 |                 |
| Protocols:      | Protocols:      | Protocols:      | Protocols:      |
| HTTP, FTP,      | HTTP, FTP,      | HTTP, FTP,      | HTTP, FTP,      |
| SMTP, etc.      | SMTP, etc.      | SMTP, etc.      | SMTP, etc.      |
+-----------------+-----------------+-----------------+-----------------+
| Presentation    | Presentation    | Presentation    | Presentation    |
| Layer           | Layer           | Layer           | Layer           |
|                 |                 |                 |                 |
| Translates      | Translates      | Translates      | Translates      |
| data formats    | data formats    | data formats    | data formats    |
| and encodings   | and encodings   | and encodings   | and encodings   |
| for different   | for different   | for different   | for different   |
| applications    | applications    | applications    | applications    |
|                 |                 |                 |                 |
| Data unit:      | Data unit:      | Data unit:      | Data unit:      |
| Message         | Message         | Message         | Message         |
|                 |                 |                 |                 |
| Protocols:      | Protocols:      | Protocols:      | Protocols:      |
| ASCII, JPEG,    | ASCII, JPEG,    | ASCII, JPEG,    | ASCII, JPEG,    |
| MPEG, etc.      | MPEG, etc.      | MPEG, etc.      | MPEG, etc.      |
+-----------------+-----------------+-----------------+-----------------+
| Session         | Session         | Session         | Session         |
| Layer           | Layer           | Layer           | Layer           |
|                 |                 |                 |                 |
| Establishes,    | Establishes,    | Establishes,    | Establishes,    |
| manages, and    | manages, and    | manages, and    | manages, and    |
| terminates      | terminates      | terminates      | terminates      |
| sessions        | sessions        | sessions        | sessions        |
| between         | between         | between         | between         |
| applications    | applications    | applications    | applications    |
|                 |                 |                 |                 |
| Data unit:      | Data unit:      | Data unit:      | Data unit:      |
| Message         | Message         | Message         | Message         |
|                 |                 |                 |                 |
| Protocols:      | Protocols:      | Protocols:      | Protocols:      |
| RPC, NFS,       | RPC, NFS,       | RPC, NFS,       | RPC, NFS,       |
| SQL, etc.       | SQL, etc.       | SQL, etc.       | SQL, etc.       |
+-----------------+-----------------+-----------------+-----------------+
| Transport       |