### Data Aggregation & Dissemination for the Notes of the Unit 4 - Network & Communication Aspects in IoT in the Subject of Internet of Things

In the world of the Internet of Things (IoT), data collection and dissemination are critical. IoT devices are capable of producing a large amount of data, making it challenging to manage and process the information. Data aggregation and dissemination are the methods used to address this issue.

#### Data Aggregation

Data aggregation is the process of collecting data from various sources and presenting it in a summarized format. In IoT, data aggregation can be done at the edge or the cloud. Edge computing is the process of processing data near the source, whereas cloud computing involves processing data in a centralized location.

Some of the ways data can be aggregated in IoT are:

- **Temporal Aggregation:** This method involves combining data points over a specific time interval. For example, temperature readings from a sensor can be combined over an hour to give the average temperature for that hour.
- **Spatial Aggregation:** This method involves combining data from various sensors located in the same area. For example, data from multiple temperature sensors placed in a room can be combined to determine the temperature of the room.
- **Feature Aggregation:** This method involves combining features of data points to create a summary. For example, combining the temperature and humidity readings from a sensor to determine the comfort level of the environment.

#### Data Dissemination

Data dissemination is the process of distributing data to different entities or systems. In IoT, data dissemination can be done in various ways, such as:

- **Push-based:** In this method, the data is sent to the receiver without any request from the receiver. For example, a sensor can send temperature readings to a server without the server requesting the data.
- **Pull-based:** In this method, the receiver requests the data from the sender. For example, a server can request temperature readings from a sensor.

Some of the data dissemination protocols used in IoT are:

- **Message Queuing Telemetry Transport (MQTT):** MQTT is a lightweight publish-subscribe protocol used for IoT devices. It is designed to be low-power and low-bandwidth, making it ideal for IoT devices.
- **Advanced Message Queuing Protocol (AMQP):** AMQP is an open-source protocol used for messaging between applications. It is ideal for IoT devices as it allows for reliable communication between devices.
- **Constrained Application Protocol (CoAP):** CoAP is a protocol designed for use in constrained environments such as IoT devices. It is designed to be low-power and low-bandwidth, making it ideal for IoT devices.

#### Mnemonics and Learning Tricks

One useful mnemonic for remembering the different data aggregation methods in IoT is "TFS." TFS stands for Temporal, Feature, and Spatial, which are the three methods of data aggregation in IoT. Another useful trick is to associate each data dissemination protocol with a letter: MQTT with "M," AMQP with "A," and CoAP with "C." This can help remember which protocol is which.