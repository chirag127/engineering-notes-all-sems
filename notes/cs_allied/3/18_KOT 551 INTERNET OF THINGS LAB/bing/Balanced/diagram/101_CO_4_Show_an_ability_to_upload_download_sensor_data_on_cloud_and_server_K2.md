# CO 4 Show an ability to upload/download sensor data on cloud and server K2

- Sensor data is the information collected by various types of sensors that measure physical phenomena such as temperature, humidity, pressure, light, sound, motion, etc.
- Cloud and server K2 are two different platforms that can store and process sensor data remotely, without requiring the sensor devices to have high computational power or memory.
- To upload sensor data on cloud and server K2, the following steps are required:
  - Establish a network connection between the sensor device and the cloud or server K2, using protocols such as Wi-Fi, Bluetooth, cellular, or LoRaWAN.
  - Choose a data format and a communication protocol for sending the sensor data, such as JSON, XML, MQTT, HTTP, or CoAP.
  - Encode and compress the sensor data to reduce the bandwidth and storage requirements, using techniques such as binary encoding, delta encoding, or lossy compression.
  - Send the sensor data to the cloud or server K2, using methods such as publish/subscribe, request/response, or push/pull.
  - Handle any errors or failures that may occur during the transmission, such as packet loss, network congestion, or security breaches.
- To download sensor data from cloud and server K2, the following steps are required:
  - Establish a network connection between the sensor device and the cloud or server K2, using the same protocols as for uploading.
  - Choose a data format and a communication protocol for receiving the sensor data, such as JSON, XML, MQTT, HTTP, or CoAP.
  - Decode and decompress the sensor data to restore the original information, using the same techniques as for uploading.
  - Receive the sensor data from the cloud or server K2, using methods such as publish/subscribe, request/response, or push/pull.
  - Handle any errors or failures that may occur during the transmission, such as packet loss, network congestion, or security breaches.
- A diagram illustrating the upload and download of sensor data on cloud and server K2 is shown below:

```
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  Sensor data   |        |  Cloud or      |        |  Sensor data   |
|  (raw or       |        |  server K2     |        |  (processed or |
|  processed)    |        |  (storage or   |        |  raw)          |
|                |        |  processing)   |        |                |
+----------------+        +----------------+        +----------------+
      |  ^                       |  ^                       |  ^
      |  |                       |  |                       |  |
      |  | Upload                |  | Download              |  |
      |  |                       |  |                       |  |
      v  |                       v  |                       v  |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  Sensor device |<------>|  Network       |<------>|  Sensor device |
|  (source or    |        |  (Wi-Fi,       |        |  (sink or      |
|  destination)  |        |  Bluetooth,    |        |  destination)  |
|                |        |  cellular,     |        |                |
|                |        |  LoRaWAN, etc.)|        |                |
+----------------+        +----------------+        +----------------+
```