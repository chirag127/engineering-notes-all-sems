# IOT ARCHITECTURE AND PROTOCOLS

- IoT architecture refers to the many ways that IoT devices are structured to meet user needs. Based on complexity, IoT system elements are grouped into 3 to 7 layers, each with its own role.
- IoT protocols are the set of rules that enable communication between IoT devices, gateways, services, and data centers. Different IoT protocols have been designed and optimized for different scenarios and usage.
- A common IoT architecture consists of the following layers  :
  - Device layer: This layer contains the sensors and actuators that collect data and perform actions. Devices can be embedded, wearable, or standalone. Devices can communicate with each other, with gateways, or with the cloud using various IoT protocols.
  - Gateway layer: This layer acts as a bridge between the device layer and the cloud layer. Gateways can aggregate, filter, process, and secure data from multiple devices before sending it to the cloud. Gateways can also perform edge computing and analytics, and provide local control and feedback to devices.
  - Cloud layer: This layer provides the storage, processing, and management of data from the gateway layer. Cloud services can also perform advanced analytics, machine learning, and artificial intelligence on the data, and provide visualization and user interfaces for applications. Cloud services can also send commands and updates to the gateway and device layers.
  - Application layer: This layer serves as the interface between the user and the device within a given IoT protocol. Applications can provide various functionalities, such as monitoring, control, automation, optimization, and decision making, based on the data and insights from the cloud layer.

- A diagram of the IoT architecture is shown below:

```
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Application    |      |    Cloud        |      |    Gateway      |      |    Device       |
|  Layer          |      |    Layer        |      |    Layer        |      |    Layer        |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  User           |      |  Storage        |      |  Edge           |      |  Sensor         |
|  Interface      |      |  Processing     |      |  Computing      |      |  Actuator       |
|  Visualization  |      |  Management     |      |  Security       |      |  Embedded       |
|  Control        |      |  Analytics      |      |  Aggregation    |      |  Wearable       |
|  Automation     |      |  Machine        |      |  Filtering      |      |  Standalone     |
|  Optimization   |      |  Learning       |      |  Protocol       |      |  Protocol       |
|  Decision       |      |  Artificial     |      |  Conversion     |      |  Conversion     |
|  Making         |      |  Intelligence   |      |                 |      |                 |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Application    |      |  Application    |      |  Application    |      |  Application    |
|  Protocol       |      |  Protocol       |      |  Protocol       |      |  Protocol       |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Internet       |      |  Internet       |      |  Internet       |      |  Internet       |
|  Protocol       |      |  Protocol       |      |  Protocol       |      |  Protocol       |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
```

- Some of the common IoT protocols are :
  - Message queue telemetry transport (MQTT) protocol: A lightweight, publish-subscribe protocol that works well for low-power, low-band