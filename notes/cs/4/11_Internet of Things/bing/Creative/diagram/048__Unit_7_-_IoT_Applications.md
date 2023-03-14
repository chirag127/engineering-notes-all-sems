The following diagram illustrates the basic architecture of a typical IoT application, based on the information from the search results   . It shows the three main layers of IoT architecture: perception, network, and application. It also shows some of the possible components and services that can be used in each layer.

## Unit 7 - IoT Applications

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Application    |    |   Network       |    |  Perception     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| - User interface|    | - Cloud gateway |    | - Sensors       |
| - Data analysis |    | - Connectivity  |    | - Actuators     |
| - Data storage  |    | - Data transfer |    | - Smart devices |
| - Data security |    | - Data security |    | - Connected     |
| - Data action   |    | - Data routing  |    |   devices       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Azure IoT   | |    | | Azure IoT   | |    | | Azure RTOS  | |
| | Hub         | |    | | Hub         | |    | | Azure Sphere| |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Azure Data  | |    | | Azure IoT   | |    | | MX Chip     | |
| | Explorer    | |    | | Device      | |    | +-------------+ |
| +-------------+ |    | | Provisioning| |    | +-------------+ |
| +-------------+ |    | | Service     | |    | | Raspberry Pi| |
| | Azure       | |    | +-------------+ |    | +-------------+ |
| | Machine     | |    | +-------------+ |    | +-------------+ |
| | Learning    | |    | | Azure       | |    | | Sensors     | |
| +-------------+ |    | | Digital     | |    | +-------------+ |
| +-------------+ |    | | Twins       | |    | +-------------+ |
| | Azure       | |    | +-------------+ |    | | Actuators   | |
| | Databricks  | |    |                 |    | +-------------+ |
| +-------------+ |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```