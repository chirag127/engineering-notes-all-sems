### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- An architectural model describes the organization of components across the network and their interrelationships.
- It helps to understand the system's structure, functionality, and performance.
- There are different types of architectural models, such as layered, object-oriented, client-server, peer-to-peer, master-slave, etc.
- Each model has its own advantages and disadvantages, depending on the system's requirements and goals.

#### Layered architecture
- In this model, different components are organized in layers.
- Each layer communicates with its adjacent layer by sending requests and getting responses.
- The layered architecture separates components into units. It is an efficient way of communication.
- Any layer cannot directly communicate with another layer. A layer can only communicate with its neighboring layer and then the next layer transfers information to another layer and so on the process goes on.
- In some cases, layered architecture is in cross-layer coordination. In a cross-layer, any adjacent layer can be skipped until it fulfills the request and provides better performance results.
- Request flow from top to bottom (downwards) and response flow from bottom to top (upwards).
- The advantage of layered architecture is that each layer can be modified independently without affecting the whole system.
- This type of architecture is used in Open System Interconnection (OSI) model.
- To the layers on top, the layers at the bottom offer a service. While the response is transmitted from bottom to top, the request is sent from top to bottom.
- This method has the advantage that calls always follow a predetermined path and that each layer is simple to replace or modify without affecting the architecture as a whole.

```
+-----------------+
| Application     |
+-----------------+
| Presentation    |
+-----------------+
| Session         |
+-----------------+
| Transport       |
+-----------------+
| Network         |
+-----------------+
| Data Link       |
+-----------------+
| Physical        |
+-----------------+
```

#### Object-oriented architecture
- In this type of architecture, components are treated as objects which convey information to each other.
- Object-Oriented Architecture contains an arrangement of loosely coupled objects.
- Objects can interact with each other through method calls.
- Objects are connected to each other through the Remote Procedure Call (RPC) mechanism or Remote Method Invocation (RMI) mechanism.
- Web Services and REST API are examples of object-oriented architecture.
- Invocations of methods are how objects communicate with one another.
- The advantage of object-oriented architecture is that it supports modularity, reusability, and encapsulation of data and behavior.
- The disadvantage of object-oriented architecture is that it may introduce overhead and complexity in the communication and coordination of objects.

```
+-----------------+    +-----------------+    +-----------------+
| Object A        |    | Object B        |    | Object C        |
+-----------------+    +-----------------+    +-----------------+
| Data            |    | Data            |    | Data            |
| Behavior        |    | Behavior        |    | Behavior        |
+-----------------+    +-----------------+    +-----------------+
| Method 1        |    | Method 2        |    | Method 3        |
| Method 2        |    | Method 3        |    | Method 4        |
+-----------------+    +-----------------+    +-----------------+
    |                  / \                    / \
    |                 /   \                  /   \
    |                /     \                /     \
    |               /       \              /       \
    |              /         \            /         \
    |             /           \          /           \
    |            /             \        /             \
    |           /               \      /               \
    |          /                 \    /                 \
    |         /                   \  /                   \
    |        /                     \/                     \
    |       /                      /\                      \
    |      /                      /  \                      \
    |     /                      /    \                      \
    |    /                      /      \                      \
    |   /                      /        \                      \
    |  /                      /          \                      \
    | /                      /            \                      \
    |/                      /              \                      \
+-----------------+    +-----------------+    +-----------------+
| RPC/RMI         |    | RPC/RMI         |    | RPC/RMI         |
+-----------------+    +-----------------+    +