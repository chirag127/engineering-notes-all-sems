The following is a detailed ASCII diagram for architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

There are different types of architectural models for distributed systems, such as layered, object-oriented, event-based, shared data space, and service-oriented. Each model has its own advantages and disadvantages, depending on the requirements and characteristics of the system.

One of the most common architectural models is the layered model, which organizes the components of the system into layers. Each layer communicates with its adjacent layer by sending requests and receiving responses. The layers can be arranged in a hierarchical or a cross-layer fashion. A hierarchical layering follows a strict top-down or bottom-up approach, where each layer can only communicate with the layer above or below it. A cross-layering allows skipping some layers to improve performance or functionality.

An example of a layered model is the Open Systems Interconnection (OSI) model, which defines seven layers for network communication: physical, data link, network, transport, session, presentation, and application. The diagram below shows the OSI model and how each layer interacts with its adjacent layer.

    +-----------------+  +-----------------+
    | Application     |  | Application     |
    +-----------------+  +-----------------+
    | Presentation    |  | Presentation    |
    +-----------------+  +-----------------+
    | Session         |  | Session         |
    +-----------------+  +-----------------+
    | Transport       |  | Transport       |
    +-----------------+  +-----------------+
    | Network         |  | Network         |
    +-----------------+  +-----------------+
    | Data Link       |  | Data Link       |
    +-----------------+  +-----------------+
    | Physical        |  | Physical        |
    +-----------------+  +-----------------+
        |  |  |  |          |  |  |  |
        V  V  V  V          V  V  V  V
    +-----------------------------------+
    |             Medium                |
    +-----------------------------------+

Another example of a layered model is the client-server model, which divides the system into two layers: the client and the server. The client sends requests to the server and receives responses from the server. The server provides services to the client and processes the requests. The diagram below shows the client-server model and how the client and the server communicate.

    +-----------------+  +-----------------+
    | Client          |  | Server          |
    +-----------------+  +-----------------+
    | Application     |  | Application     |
    +-----------------+  +-----------------+
    | Transport       |  | Transport       |
    +-----------------+  +-----------------+
        |  |  |  |          |  |  |  |
        V  V  V  V          V  V  V  V
    +-----------------------------------+
    |             Network               |
    +-----------------------------------+

Another type of architectural model is the object-oriented model, which treats the components of the system as objects that communicate with each other by invoking methods. The objects are loosely coupled and can be distributed across the network. The objects can interact with each other through remote procedure calls (RPCs) or remote method invocations (RMIs). Web services and REST APIs are examples of object-oriented models. The diagram below shows the object-oriented model and how the objects communicate with each other.

    +-----------------+  +-----------------+
    | Object A        |  | Object B        |
    +-----------------+  +-----------------+
    | Attributes      |  | Attributes      |
    +-----------------+  +-----------------+
    | Methods         |  | Methods         |
    +-----------------+  +-----------------+
        |  |  |  |          |  |  |  |
        V  V  V  V          V  V  V  V
    +-----------------------------------+
    |             Network               |
    +-----------------------------------+
        |  |  |  |          |  |  |  |
        ^  ^  ^  ^          ^  ^  ^  ^
    +-----------------+  +-----------------+
    | RPC/RMI         |  | RPC/RMI         |
    +-----------------+  +-----------------+

Another type of architectural model is the event-based model, which organizes the components of the system as publishers and subscribers. The publishers generate events and send them to an event service, which distributes them to the subscribers who are