The following diagram illustrates the basic architecture of a data enrichment and consolidation process for IoT data. The diagram is based on the information from the search results  and uses ASCII characters to draw the shapes and arrows.

### Data enrichment and consolidation for IoT data

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   IoT device   +----->+ Watson IoT     +----->+ Node-RED app   |
|                |      | Platform       |      |                |
+----------------+      +----------------+      +----------------+
                                                    |
                                                    |
                                                    v
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Database     +<-----+ IoT Blockchain +<-----+ Asset in       |
|                |      | Service        |      | accordance     |
+----------------+      +----------------+      +----------------+
                                                    |
                                                    |
                                                    v
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
| Supply chain   +<-----+ Enriched IoT   +<-----+ Enriched asset |
| application    |      | event          |      |                |
+----------------+      +----------------+      +----------------+
```

The diagram shows the following steps:

- An IoT device sends IoT data to Watson IoT Platform. The data includes a temperature reading, location information, and a device ID.
- A Node-RED application subscribes to Watson IoT Platform for IoT sensor data. The Node-RED application requests non-IoT data from a database. The application uses the device ID to request non-IoT data from the database. The device ID is a correlation parameter and is common to both sources of data.
- The Node-RED application creates an asset in IoT Blockchain Service. The application combines sensor data, which is IoT data, and shipment data, which is non-IoT data, into an asset in accordance with the contract definition.
- IoT Blockchain Service sends a transaction with the IoT and non-IoT data to IBM Blockchain Platform. The matched IoT data and non-IoT data are merged to create an enriched asset in accordance with a contract. The enriched asset is stored in the blockchain.
- IoT Blockchain Service sends an enriched IoT event to a supply chain application as a notification of the success of the transaction and includes the transaction data. The supply chain application can use the enriched IoT event to track the shipment status and take actions if needed.