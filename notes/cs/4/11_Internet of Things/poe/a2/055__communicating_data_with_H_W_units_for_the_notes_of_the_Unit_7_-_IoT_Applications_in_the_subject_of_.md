 Here is the content in Markdown format without any emojis or external links and in formal tone:

### Communicating data with Hardware units

1. Sensors: Sensors collect data from the physical world like temperature, humidity, motion, etc. and convert the physical data into electrical signals which are then converted into digital data and sent to microcontrollers or gateways. eg. Temperature sensor, PIR sensor, Ultrasonic sensor, etc.
2. Microcontrollers: The digital data from sensors is sent to microcontrollers which perform processing on the data like data filtering or conversion and then transmit the data to gateways or servers. eg. Arduino, Raspberry Pi, ESP32, etc.
3. Gateways: Gateways act as an intermediate device to connect the hardware units to the Internet/cloud servers. They receive the data from microcontrollers and then forward it to the servers over the Internet. They can also be configured to perform some processing or aggregation on the data before sending it to the servers.
4. Servers: The data is received by servers over the Internet which then store, process and analyze the data. The analyzed data can be used to monitor the system or trigger some actions. The servers then optionally send a response back to the hardware units which can trigger some actions in the physical world.

The above steps demonstrate how the hardware units communicate with each other to send the data to the servers which can then be used for IoT applications. The communication between the units can be wired or wireless depending upon the requirements and distances. The data exchange also follows some protocols like MQTT, HTTP, etc.