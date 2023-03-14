### Mobile IP

Mobile IP is a protocol that allows a mobile node (MN) to keep the same IP address while roaming between different networks. Mobile IP uses the following components:

- Home network: The network where the MN belongs and has a permanent IP address (home address).
- Home agent (HA): A router in the home network that keeps track of the MN's current location and forwards packets to it.
- Foreign network: The network where the MN is currently visiting and has a temporary IP address (care-of address).
- Foreign agent (FA): A router in the foreign network that provides the MN with a care-of address and delivers packets to it.
- Correspondent node (CN): A device on the internet that communicates with the MN.

The following diagram illustrates the basic architecture of Mobile IP:

```
+----------------+                +----------------+                +----------------+
|                |                |                |                |                |
|  Home Network  |                |  Internet      |                | Foreign Network|
|                |                |                |                |                |
+----------------+                +----------------+                +----------------+
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
+----------------+                +----------------+                +----------------+
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|      HA        |                |      CN        |                |      FA        |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
+----------------+                +----------------+                +----------------+
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
+----------------+                +----------------+                +----------------+
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|      MN        |                |                |                |      MN        |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
|                |                |                |                |                |
+----------------+                +----------------+                +----------------+

```

The diagram shows the MN in two different locations: at home and away from home. When the MN is at home, it communicates directly with the CN using its home address. When the MN is away from home, it registers its care-of address with the HA, which creates a binding between the home address and the care-of address. The CN sends packets to the MN's home address, which are intercepted by the HA and tunneled to the FA using encapsulation. The FA decapsulates the packets and delivers them to the MN using its care-of address. The MN sends packets to the CN directly or through the FA, depending on the type of care-of address (foreign agent care-of address or co-located care-of address). The CN can also learn the MN's care-of address from the HA and send packets directly to the MN using a technique called route optimization.