The following is a possible diagram for land records and other kinds of record keeping between government entities for the notes of the Unit 8 - Use case 3 in the subject of Block chain Architecture Design. The diagram is based on the information from the web search results and is drawn using ASCII characters.

### Land Records and Other Kinds of Record Keeping Between Government Entities

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Land Owner A   |       |  Land Owner B   |       |  Land Owner C   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       v                       v                       v
+-----------------------------------------------------------------------+
|                                                                       |
|                          Blockchain Network                           |
|                                                                       |
|  +-----------------+  +-----------------+  +-----------------+        |
|  |                 |  |                 |  |                 |        |
|  |  Government A   |  |  Government B   |  |  Government C   |        |
|  |                 |  |                 |  |                 |        |
|  +-----------------+  +-----------------+  +-----------------+        |
|                                                                       |
|  +-----------------+  +-----------------+  +-----------------+        |
|  |                 |  |                 |  |                 |        |
|  |  Land Registry  |  |  Land Registry  |  |  Land Registry  |        |
|  |                 |  |                 |  |                 |        |
|  +-----------------+  +-----------------+  +-----------------+        |
|                                                                       |
|  +-----------------+  +-----------------+  +-----------------+        |
|  |                 |  |                 |  |                 |        |
|  |  GIS Provider   |  |  GIS Provider   |  |  GIS Provider   |        |
|  |                 |  |                 |  |                 |        |
|  +-----------------+  +-----------------+  +-----------------+        |
|                                                                       |
|  +-----------------+  +-----------------+  +-----------------+        |
|  |                 |  |                 |  |                 |        |
|  |  Smart Contract |  |  Smart Contract |  |  Smart Contract |        |
|  |                 |  |                 |  |                 |        |
|  +-----------------+  +-----------------+  +-----------------+        |
|                                                                       |
|  +-----------------+  +-----------------+  +-----------------+        |
|  |                 |  |                 |  |                 |        |
|  |  Ledger Node    |  |  Ledger Node    |  |  Ledger Node    |        |
|  |                 |  |                 |  |                 |        |
|  +-----------------+  +-----------------+  +-----------------+        |
|                                                                       |
+-----------------------------------------------------------------------+
```

The diagram illustrates the basic architecture of a blockchain-based land registration system. The system consists of the following components:

- Land owners: These are the entities that own the land parcels and can initiate transactions to transfer the ownership or update the information of their land parcels.
- Blockchain network: This is the distributed network of nodes that store and validate the transactions of land ownership and information using a consensus algorithm. The network also provides security, transparency, and immutability of the land records.
- Government entities: These are the entities that are responsible for regulating and verifying the land transactions and maintaining the land records. They can also access the blockchain network to query or audit the land records.
- Land registry: This is the component that manages the land records and provides the interface for the land owners and the government entities to interact with the blockchain network. The land registry also stores the geospatial information of the land parcels using a geographical information system (GIS) provider.
- GIS provider: This is the component that provides the geocoded description of the land parcels and their location on the earth surface.