The following is a detailed ASCII diagram for location management: HLR-VLR, hierarchical, handoffs for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing.

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|      HLR        |    |      VLR 1      |    |      VLR 2      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|      MSC        |    |      MSC 1      |    |      MSC 2      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|      BSC        |    |      BSC 1      |    |      BSC 2      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|      BTS        |    |      BTS 1      |    |      BTS 2      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|      MS         |    |      MS 1       |    |      MS 2       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram illustrates the basic architecture of a cellular network, where:

- HLR: Home Location Register, a centralized database that stores the permanent and temporary information of all subscribers in the network.
- VLR: Visitor Location Register, a local database that stores the information of subscribers who are currently in the service area of the VLR.
- MSC: Mobile Switching Center, a node that performs call routing and switching functions for mobile stations.
- BSC: Base Station Controller, a node that controls and manages one or more base transceiver stations (BTS).
- BTS: Base Transceiver Station, a node that communicates with mobile stations via radio channels.
- MS: Mobile Station, a device that allows a user to access the cellular network.

The location management process involves the following steps:

- Registration: When a mobile station moves into a new service area, it registers with the VLR of that area and updates its location information in the HLR.
-