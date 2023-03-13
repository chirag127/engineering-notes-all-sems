I have drawn a detailed ASCII diagram for MAC protocol survey for the notes of the Unit 4 - Network & Communication aspects in IoT in the subject of Internet of Things. The diagram is based on the information from the web search results    . I hope this helps you.

### MAC protocol survey for the notes of the Unit 4 - Network & Communication aspects in IoT in the subject of Internet of Things

```
+-----------------------------------------------------------------------------+
|                                                                             |
|                           MAC Protocol Survey for IoT                       |
|                                                                             |
+-----------------------------------------------------------------------------+
|                                                                             |
|  +-----------------+  +-----------------+  +-----------------+  +---------+  |
|  |                 |  |                 |  |                 |  |         |  |
|  |  Contention-    |  |  Contention-    |  |  Contention-    |  |  Hybrid |  |
|  |  based MAC      |  |  free MAC       |  |  aware MAC      |  |  MAC    |  |
|  |                 |  |                 |  |                 |  |         |  |
|  +-----------------+  +-----------------+  +-----------------+  +---------+  |
|  |                 |  |                 |  |                 |  |         |  |
|  |  - CSMA/CA      |  |  - TDMA         |  |  - LMAC         |  |  - Z-MAC|  |
|  |  - ALOHA        |  |  - FDMA         |  |  - TRAMA        |  |  - B-MAC|  |
|  |  - Slotted      |  |  - CDMA         |  |  - SMAC         |  |  - X-MAC|  |
|  |    ALOHA        |  |  - OFDMA        |  |  - DMAC         |  |  - RI-MAC| |
|  |  - IEEE 802.11  |  |  - IEEE 802.15.4|  |  - MMAC         |  |  - WiseMAC||
|  |    (WiFi)       |  |    (ZigBee)     |  |  - EM-MAC       |  |  - Sift  | |
|  |  - IEEE 802.11ah|  |  - IEEE 802.15.1|  |  - P-MAC        |  |  - SCP-MAC||
|  |    (WiFi HaLow) |  |    (Bluetooth)  |  |  - T-MAC        |  |  - CoSenS| |
|  |  - IEEE 802.15.6|  |  - IEEE 802.15.3|  |  - RMAC         |  |  - TSCH  | |
|  |    (WBAN)       |  |    (UWB)        |  |  - PEDAMACS     |  |  - LoRaWAN| |
|  |  - IEEE 802.15.7|  |  - IEEE 802.16  |  |  - Q-MAC        |  |  - NB-IoT| |
|  |    (Li-Fi)      |  |    (WiMAX)      |  |  - Funneling-MAC|  |         |  |
|  |  - IEEE 802.15.9|  |  - IEEE 802.16e |  |  - BMAC         |  |         |  |
|  |    (Key         |  |    (Mobile      |  |  - PMAC         |  |         |  |
|  |    Management)  |  |    WiMAX)       |  |  - CMAC         |  |         |  |
|  |  - IEEE 802.15.10| |  - IEEE 802.16m |  |  - AMAC         |  |         |  |
|  |    (Routing)    |  |    (Advanced    |  |  - MFP-MAC      |  |         |  |
|  |                 |  |    WiMAX)       |  |  - RAP-MAC      |  |         |  |
|