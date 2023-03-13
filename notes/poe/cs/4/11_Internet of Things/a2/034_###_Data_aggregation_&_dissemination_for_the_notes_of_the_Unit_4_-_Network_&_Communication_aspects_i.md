 Here is the content in Markdown format:

### Data aggregation & dissemination for the notes of the Unit 4 - Network & Communication aspects in IoT in the subject of Internet of Things

- Data aggregation: Collecting data from multiple IoT devices and consolidating into a unified data store. This is done to get a holistic view of the system or to perform analytics.
- Methods:
  - Direct: Devices send data directly to the aggregation point. Scalability issues.
  - Hierarchical: Devices send to local aggregation points which then send to higher level and so on. Reduces bandwidth usage but increases latency.
  - Distributed: Peer-to-peer aggregation. Devices send to nearby devices which then send to aggregation point. Scalable but complex.
- Data dissemination: Send aggregated data/ analytics results/ control commands to relevant IoT devices.
- Methods:
  - Unicast: Send individual messages to each device. Not scalable.
  - Multicast: Send one message to a group of devices. More efficient but complex to implement.
  - Broacast: Send one message to all devices. Simple but can lead to congestion and waste bandwidth.

**Mnemonics:**

- DAD: Data Aggregation then Dissemination
- MAD: Multicast for dissemination, Aggregation can be Direct/Hierarchical/Distributed

**Advantages:** Holistic view, analytics, reduced bandwidth usage (hierarchical), scalability (distributed).

**Disadvantages:** Latency (hierarchical), complexity (distributed), congestion/waste (broadcast).

**Applications:** Smart cities, smart homes, industry automation, etc.

[Detailed diagrams and examples can be added here]

Hope this helps! Let me know if you would like me to elaborate on any of the points or add more details.