The following is a detailed ASCII diagram for IoT/M2M systems layers and design standardization for the notes of the Unit 1 - Internet of Things (IoT) in the subject of Internet of Things. The diagram is based on the oneM2M IoT standardized architecture  which divides IoT functions into three major domains: the application layer, the service layer and the network layer. The diagram also shows the common protocols and technologies used in each layer.

### IoT/M2M systems layers and design standardization

```
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|    Application    |    Application    |    Application    |
|                   |                   |                   |
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|    HTTP, MQTT,    |    oneM2M API     |    HTTP, MQTT,    |
|    CoAP, XMPP     |                   |    CoAP, XMPP     |
|                   |                   |                   |
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|    Service Layer  |    Service Layer  |    Service Layer  |
|                   |                   |                   |
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|    HTTP, MQTT,    |    oneM2M API     |    HTTP, MQTT,    |
|    CoAP, XMPP     |                   |    CoAP, XMPP     |
|                   |                   |                   |
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|    Network Layer  |    Network Layer  |    Network Layer  |
|                   |                   |                   |
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|    3GPP, Wi-Fi,   |    3GPP, Wi-Fi,   |    3GPP, Wi-Fi,   |
|    ZigBee, Z-Wave |    ZigBee, Z-Wave |    ZigBee, Z-Wave |
|                   |                   |                   |
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|     Device 1      |     Device 2      |     Device 3      |
|                   |                   |                   |
+-------------------+-------------------+-------------------+
```