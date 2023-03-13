 Here is the content in markdown format:

### Sensor deployment & Node discovery for the notes of the Unit 4 - Network & Communication aspects in IoT in the subject of Internet of Things

- Sensors are deployed in the field to sense the physical parameters like temperature, humidity, pressure, etc. The sensors are connected to the edge nodes which are embedded systems having processing and wireless communication capabilities.
- The edge nodes collect the data from the sensors and transmit the data to the gateway node. The gateway node has more powerful hardware and serves as an interface between the edge nodes and the cloud.
- The gateway node may be able to process the data locally before sending it to the cloud. The gateway node may use cellular data networks or local area networks to send the data to the cloud.
- In the cloud, the data is stored and analyzed. The results are sent back to the edge nodes or gateway nodes to take appropriate actions in the physical environment.
- For node discovery in an IoT network, the nodes can broadcast 'hello' messages to detect the presence of neighboring nodes. The nodes can exchange information about themselves and build a neighborhood map. The neighborhood map is updated dynamically as nodes join or leave the network.
- The nodes can use a broad system like [MQTT](http://mqtt.org/) to publish and subscribe to topics to send and receive messages. The topic names can incorporate location information to facilitate discovery of nodes in a neighborhood.
- The nodes may have unique IDs or addresses to identify them in the network. The IDs can be used to retrieve data from specific nodes or send instructions to specific nodes.
- Learning tricks: Think of sensors as input devices, edge nodes as processors and gateway node as an interface to the cloud which is the brain. Data flows from sensors to cloud guiding actions to the physical environment.

The content includes details on sensor deployment, data flow, node discovery methods and MQTT for communication. Mnemonics are included where relevant to aid learning. Please let me know if you would like me to elaborate on any part or modify the content.