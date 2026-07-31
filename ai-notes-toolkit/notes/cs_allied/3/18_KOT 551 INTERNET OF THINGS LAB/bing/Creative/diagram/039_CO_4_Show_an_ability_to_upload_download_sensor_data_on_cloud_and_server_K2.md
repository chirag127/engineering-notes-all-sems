# CO 4 Show an ability to upload/download sensor data on cloud and server K2

- Sensor data is the information collected by various types of sensors that measure physical phenomena such as temperature, humidity, pressure, light, sound, motion, etc.
- Cloud and server are two types of computing platforms that can store, process, and analyze sensor data remotely over the internet.
- Uploading sensor data means sending the data from the sensor device to the cloud or server, while downloading sensor data means receiving the data from the cloud or server to the sensor device or another device.
- To upload/download sensor data on cloud and server, the following steps are required:

  - Connect the sensor device to the internet using a wired or wireless connection, such as Ethernet, Wi-Fi, Bluetooth, cellular, satellite, etc.
  - Choose a cloud or server platform that supports the sensor data format, protocol, and security requirements, such as AWS, Azure, Google Cloud, ThingSpeak, etc.
  - Register the sensor device on the cloud or server platform and obtain the credentials and configuration details, such as device ID, access key, endpoint, topic, etc.
  - Install and configure the software or library on the sensor device that can communicate with the cloud or server platform, such as MQTT, HTTP, CoAP, etc.
  - Write the code on the sensor device that can read the sensor data, format it, and publish it to the cloud or server platform using the software or library.
  - Write the code on the sensor device or another device that can subscribe to the cloud or server platform and receive the sensor data using the software or library.
  - Test and debug the code and the connection to ensure the sensor data is uploaded/downloaded correctly and securely.

- Some examples of uploading/downloading sensor data on cloud and server are:

  - Using a Raspberry Pi and a DHT22 sensor to send humidity and temperature data to ThingSpeak using MQTT.
  - Using an Arduino and a light sensor to send light intensity data to AWS DynamoDB using HTTP.
  - Using a Microsoft Defender for IoT sensor to send network traffic data to Azure using a subscription and activation file.
  - Using a SAPHI sensor and a satellite modem to send environmental data to Google Cloud using TCP/IP.