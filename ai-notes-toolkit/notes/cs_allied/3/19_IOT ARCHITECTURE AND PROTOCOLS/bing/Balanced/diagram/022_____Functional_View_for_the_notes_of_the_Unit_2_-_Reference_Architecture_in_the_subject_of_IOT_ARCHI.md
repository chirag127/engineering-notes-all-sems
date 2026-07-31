### Functional View

The functional view of the IoT reference architecture describes the system's runtime functional components, their responsibilities, default functions, interfaces and primary interactions. The functional view follows the modular structure of functional blocks organized into layers, as it was proposed e.g. in SENSEI.

The functional view consists of the following layers:

- **Device Layer**: This layer contains the physical devices that are connected to the IoT system, such as sensors, actuators, gateways, etc. The device layer is responsible for providing data acquisition, data processing, data storage, data transmission and device management functions.
- **Network Layer**: This layer provides the communication infrastructure and protocols for the IoT system, such as wired or wireless networks, routing, addressing, security, etc. The network layer is responsible for enabling data exchange, data aggregation, data filtering, data compression and network management functions.
- **Service Layer**: This layer provides the application logic and services for the IoT system, such as data analysis, data visualization, data fusion, data mining, etc. The service layer is responsible for providing data processing, data presentation, data interpretation and service management functions.
- **Business Layer**: This layer provides the business value and goals for the IoT system, such as business processes, business rules, business models, etc. The business layer is responsible for providing business intelligence, business optimization, business innovation and business governance functions.

The functional view also defines the cross-layer functions that span across multiple layers, such as security, privacy, trust, identity, discovery, etc. These functions are responsible for ensuring the quality, reliability, interoperability and scalability of the IoT system.

The functional view can be represented by the following diagram:

```
+-----------------+
|  Business Layer |
+-----------------+
|  Service Layer  |
+-----------------+
|  Network Layer  |
+-----------------+
|  Device Layer   |
+-----------------+
```