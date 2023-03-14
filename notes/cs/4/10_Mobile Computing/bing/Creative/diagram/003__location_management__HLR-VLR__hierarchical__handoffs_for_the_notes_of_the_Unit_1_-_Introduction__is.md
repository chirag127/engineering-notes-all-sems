Location management is a technique to track the location of a mobile user in a wireless cellular network. It consists of two main components: location update and location search. Location update is the process of informing the network about the current location of the mobile user, while location search is the process of finding the mobile user when a call arrives.

One of the common schemes for location management is the HLR-VLR scheme, which uses a hierarchical database structure to store the location information of the mobile users. HLR stands for Home Location Register, which is a central database that contains the permanent records of all the mobile users in the network. VLR stands for Visitor Location Register, which is a local database that contains the temporary records of the mobile users who are currently visiting a certain area. Each area is divided into smaller regions called Location Areas (LAs), which are composed of several cells. Each LA has a VLR associated with it.

When a mobile user moves from one cell to another within the same LA, it performs a location update to the VLR of that LA. When a mobile user crosses the boundary of an LA, it performs a location update to both the VLR of the new LA and the HLR. The HLR then updates the old VLR to delete the record of the mobile user and informs the new VLR to create a new record. When a call arrives for a mobile user, the network first queries the HLR to find the current VLR of the mobile user. Then, the network queries the VLR to find the current LA of the mobile user. Finally, the network pages all the cells within the LA to locate the mobile user and establish the connection.

The following diagram illustrates the basic architecture of a HLR-VLR scheme:

```
+-----------------+        +-----------------+
|                 |        |                 |
|      PSTN       |        |       HLR       |
|                 |        |                 |
+-----------------+        +-----------------+
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
+-----------------+        +-----------------+
|                 |        |                 |
|      STP        |        |      VLR1       |
|                 |        |                 |
+-----------------+        +-----------------+
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
+-----------------+        +-----------------+
|                 |        |                 |
|      PCN        |        |      VLR2       |
|                 |        |                 |
+-----------------+        +-----------------+
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
+-----------------+        +-----------------+
|                 |        |                 |
|      LA1        |        |      LA2        |
|                 |        |                 |
+-----------------+        +-----------------+
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
+-----------------+        +-----------------+
|                 |        |                 |
|      Cell1      |        |      Cell2      |
|                 |        |                 |
+-----------------+        +-----------------+
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
          |                        |
+-----------------+        +-----------------+
|                 |        |                 |
|      MU1        |        |      MU2        |
|                 |        |                 |
+-----------------+        +-----------------+
```

PSTN: Public Switched Telephone Network
STP: Service Transfer Point
PCN: Personal Communication Network
HLR: Home Location Register
VLR: Visitor Location Register
LA: Location Area
Cell: Base Station
MU: Mobile User

Handoff management is another technique to ensure the continuity of service for a mobile user in a wireless cellular network. It is the process of transferring