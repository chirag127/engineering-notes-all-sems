 Here is the content in markdown format on how to build applications with Zookeeper:

#### How to build applications with Zookeeper

Zookeeper is a distributed, open-source coordination service for distributed applications. It exposes a simple set of primitives that distributed applications can build upon to implement higher level services.

Some key points to keep in mind when building applications with Zookeeper:

1. Zookeeper stores data in a hierarchical namespace and supports consistent distributed configuration services, synchronization services, and naming services. Applications can store configuration data, coordinate between processes, and name and locate services using Zookeeper's data model and simple API.

2. Zookeeper achieves consistency by maintaining a single system image through a consistent and sequential change number. All updates to Zookeeper data are ordered and serialized to maintain linearizability. This makes it ideal for coordination as it ensures processes have a consistent view of the system.

3. Zookeeper allows distributed applications to agree on a common state/configuration by providing a shared configuration service. Processes can register to be notified of changes in certain data, and these watches allow applications to detect and respond to changes. This enables synchronization across a cluster.

4. The hierarchical namespace and sequential consistent updates of Zookeeper make it suitable as a naming service. Processes can create paths to name entities and use Zookeeper to locate the machine that hosts a service. The serialization of updates ensures a consistent view of name-to-location mappings throughout the cluster.

Some additional points and examples can be included here regarding Zookeeper's architecture, guarantees, APIs, usage, advantages, and disadvantages to make the content more comprehensive as a study material. Mnemonics and learning tricks can also be included if easy to remember. Detailed diagrams and code snippets can add value to the technical concepts.