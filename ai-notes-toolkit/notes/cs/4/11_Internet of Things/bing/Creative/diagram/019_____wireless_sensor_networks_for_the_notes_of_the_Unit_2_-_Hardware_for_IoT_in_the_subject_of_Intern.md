# Wireless Sensor Networks

- Wireless sensor networks (WSNs) refer to networks of spatially dispersed and dedicated sensors that monitor and record the physical conditions of the environment and forward the collected data to a central location.
- WSNs can measure environmental conditions such as temperature, sound, pollution levels, humidity and wind.
- A WSN consists of a set of connected tiny sensor nodes, which communicate with each other and exchange information and data.
- A WSN also consists of one or more sink nodes (also called base stations) that collect data from sensors and forward it to a higher-level network.
- A sensor node could behave both as data originator and data router.
- A WSN is characterized as infrastructure-less, fault-tolerant and self-organizing network which provides opportunities for low-cost, easy-to-apply, rapid and flexible installations in an environment for various applications.
- WSNs can be used for various purposes such as environmental monitoring, health care, smart homes, industrial automation, military surveillance, etc.

The following diagram shows the basic architecture of a WSN:

```
+-----------------+       +-----------------+
| Higher-level    |       | Higher-level    |
| network         |       | network         |
+-----------------+       +-----------------+
        ^                         ^
        |                         |
        |                         |
+-----------------+       +-----------------+
| Sink node       |       | Sink node       |
| (base station)  |       | (base station)  |
+-----------------+       +-----------------+
        ^                         ^
        |                         |
        |                         |
+-----------------+       +-----------------+
| Sensor node     |       | Sensor node     |
| (data originator|       | (data originator|
| and router)     |       | and router)     |
+-----------------+       +-----------------+
        ^                         ^
        |                         |
        |                         |
+-----------------+       +-----------------+
| Sensor node     |       | Sensor node     |
| (data originator|       | (data originator|
| and router)     |       | and router)     |
+-----------------+       +-----------------+
        ^                         ^
        |                         |
        |                         |
+-----------------+       +-----------------+
| Sensor node     |       | Sensor node     |
| (data originator|       | (data originator|
| and router)     |       | and router)     |
+-----------------+       +-----------------+
```