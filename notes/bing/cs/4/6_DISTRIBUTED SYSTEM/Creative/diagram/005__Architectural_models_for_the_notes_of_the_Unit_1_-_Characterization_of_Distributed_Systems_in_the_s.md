The following is a detailed ASCII diagram for architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Architectural models for distributed systems

Architectural models describe the organization of components in a distributed system and their interrelationships. There are different types of architectural models, such as layered, object-oriented, data-centered, event-based, and peer-to-peer. Each model has its own advantages and disadvantages depending on the requirements and characteristics of the distributed system.

The following diagram illustrates the basic structure of each architectural model using ASCII symbols. The components are represented by boxes and the communication links are represented by lines. The arrows indicate the direction of communication. The labels indicate the name and role of each component.

Layered model:

+-----------------+     +-----------------+     +-----------------+
| Application     |     | Application     |     | Application     |
| layer           |     | layer           |     | layer           |
+-----------------+     +-----------------+     +-----------------+
| Middleware      |     | Middleware      |     | Middleware      |
| layer           |     | layer           |     | layer           |
+-----------------+     +-----------------+     +-----------------+
| Operating       |     | Operating       |     | Operating       |
| system layer    |     | system layer    |     | system layer    |
+-----------------+     +-----------------+     +-----------------+
| Hardware layer  |     | Hardware layer  |     | Hardware layer  |
+-----------------+     +-----------------+     +-----------------+
     | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
     | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
     V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V
+-----------------+     +-----------------+     +-----------------+
| Network         |     | Network         |     | Network         |
| layer           |     | layer           |     | layer           |
+-----------------+     +-----------------+     +-----------------+

In the layered model, each component is organized in a hierarchical layer that provides services to the layer above it and uses services from the layer below it. The layers are independent and can be changed or replaced without affecting the other layers. The layered model simplifies the design and implementation of distributed systems, but it may introduce overhead and performance issues due to the multiple levels of abstraction and communication.

Object-oriented model:

+-----------------+     +-----------------+     +-----------------+
| Object          |     | Object          |     | Object          |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
| Object          |     | Object          |     | Object          |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
| Object          |     | Object          |     | Object          |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
     | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
     | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
     V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V
+-----------------+     +-----------------+     +-----------------+
| Network         |     | Network         |     | Network         |
| layer           |     | layer           |     | layer           |
+-----------------+     +-----------------+     +-----------------+

In the object-oriented model, each component is an object that encapsulates data and behavior and communicates with other objects by invoking methods. The objects are distributed across the network and can be accessed by using a common interface and a naming service. The object-oriented model supports modularity, reusability, and abstraction, but it may introduce complexity and overhead due to the distributed object management and invocation.

Data-centered model:

+-----------------+     +-----------------+     +-----------------+
| Process         |