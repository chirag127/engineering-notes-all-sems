Data enrichment and consolidation is a process of integrating IoT data with non-IoT data and writing the data to the blockchain. This can improve data visibility, data security, and data analysis options. A contract can be used as a connection point between the IoT data and the non-IoT data based on a correlation parameter, such as the IoT device ID. The matched IoT data and non-IoT data are merged to create an enriched asset that is stored in the blockchain. An enriched IoT event is sent to a supply chain application as a notification of the success of the transaction and includes the transaction data.

The following diagram illustrates the basic architecture of a data enrichment and consolidation solution for IoT using Node-RED and a contract:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  IoT Platform   |     |  Node-RED Flow  |     |  Blockchain     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  IoT Data       |---->|  IoT Data       |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
                        |                 |     |                 |
                        |  Non-IoT Data   |---->|  Non-IoT Data   |
                        |                 |     |                 |
                        +-----------------+     +-----------------+
                        |                 |     |                 |
                        |  Contract       |---->|  Contract       |
                        |                 |     |                 |
                        +-----------------+     +-----------------+
                        |                 |     |                 |
                        |  Enriched Asset |---->|  Enriched Asset |
                        |                 |     |                 |
                        +-----------------+     +-----------------+
                        |                 |     |                 |
                        |  Enriched Event |---->|  Enriched Event |
                        |                 |     |                 |
                        +-----------------+     +-----------------+
```