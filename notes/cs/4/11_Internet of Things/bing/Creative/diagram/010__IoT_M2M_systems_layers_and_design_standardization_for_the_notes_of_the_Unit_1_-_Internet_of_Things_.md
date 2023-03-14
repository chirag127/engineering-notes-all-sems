The following is a detailed ASCII diagram for IoT/M2M systems layers and design standardization for the notes of the Unit 1 - Internet of Things (IoT) in the subject of Internet of Things.

The diagram is based on the oneM2M IoT standardized architecture   , which divides IoT functions into three major domains: the application layer, the service layer, and the network layer.

The application layer contains the applications that use the IoT data and services, such as smart home, smart city, e-health, etc. The application layer communicates with the service layer through the oneM2M APIs, which are standardized interfaces that enable interoperability and portability of applications.

The service layer provides the common services and functions that are needed by the IoT applications, such as data management, device management, security, discovery, etc. The service layer consists of two types of entities: the Common Service Entity (CSE) and the Application Entity (AE). The CSE is the core component of the service layer that implements the oneM2M service logic and exposes the oneM2M APIs to the application layer and the network layer. The AE is an optional component that represents an application or a part of an application that resides in the service layer and interacts with the CSE.

The network layer provides the connectivity and transport mechanisms for the IoT data and messages, such as cellular, Wi-Fi, Bluetooth, LoRa, etc. The network layer communicates with the service layer through the oneM2M protocols, which are standardized protocols that enable interoperability and security of data and messages. The network layer consists of two types of entities: the Network Service Entity (NSE) and the Network Application Entity (NAE). The NSE is the core component of the network layer that implements the oneM2M protocols and exposes the oneM2M APIs to the service layer. The NAE is an optional component that represents an application or a part of an application that resides in the network layer and interacts with the NSE.

The diagram also shows the different types of nodes that can host the service layer and the network layer entities, such as the Application Dedicated Node (ADN), the Middle Node (MN), and the Infrastructure Node (IN). The ADN is a node that hosts only one AE and one NAE, and is typically a device or a sensor. The MN is a node that hosts one or more CSEs and NSEs, and is typically a gateway or a router. The IN is a node that hosts one or more CSEs and NSEs, and is typically a server or a cloud platform.

The diagram also shows the different types of communication patterns that can occur between the entities in the IoT/M2M system, such as request/response, notification, group communication, and broadcast communication. The request/response pattern is a synchronous communication where an entity sends a request to another entity and waits for a response. The notification pattern is an asynchronous communication where an entity sends a notification to another entity without expecting a response. The group communication pattern is a communication where an entity sends a message to a group of entities that share a common interest or topic. The broadcast communication pattern is a communication where an entity sends a message to all the entities in the system.

The diagram uses the following symbols and conventions:

- A box represents an entity or a node
- A dashed line represents the boundary of a layer or a domain
- A solid line represents a communication link
- An arrow represents the direction of a message
- A label represents the type or the name of an entity, a node, a layer, a domain, or a message
- A subscript represents the number or the identifier of an entity or a node

The diagram is as follows:

```
+-----------------+   +-----------------+   +-----------------+
| Application     |   | Application     |   | Application     |
| Layer           |   | Layer           |   | Layer           |
+-----------------+   +-----------------+   +-----------------+
| oneM2M APIs     |   | oneM2M APIs     |   | oneM2M APIs     |
+-----------------+   +-----------------+   +-----------------+
| AE1             |   | AE2             |   | AE3             |
+-----------------+   +-----------------+   +-----------------+
| Service Layer   |   | Service Layer   |   | Service Layer   |
+-----------------+   +-----------------+   +-----------------+
| CSE1            |   | CSE