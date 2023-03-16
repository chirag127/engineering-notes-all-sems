### Architectural view for the notes of the Unit 1 - Internet of Things (IoT) in the subject of Internet of Things

- The architectural view of IoT is the way of describing the structure and behavior of an IoT system, which consists of many interconnected devices and applications that communicate and exchange data over the internet.
- There is no standard or universal architecture for IoT, as different IoT systems may have different requirements, functionalities, and implementations in various domains and sectors.
- However, some common architectural models have been proposed and used in the literature and practice, which can be classified into three main categories: three-layer, five-layer, and semantic models.

#### Three-layer architecture
- The three-layer architecture is the simplest and most basic model of IoT, which defines the main idea and components of an IoT system.
- The three layers are:

  - Perception layer: This is the lowest layer, which consists of physical devices, such as sensors, actuators, RFID tags, cameras, etc., that can sense, collect, and transmit data from the environment.
  - Network layer: This is the middle layer, which provides the connectivity and communication between the perception layer and the application layer. It uses various network technologies, such as Wi-Fi, Bluetooth, cellular, ZigBee, etc., to transfer the data over the internet.
  - Application layer: This is the highest layer, which provides the services and applications for the end-users, such as smart home, smart city, smart health, smart agriculture, etc. It processes, analyzes, and displays the data received from the network layer, and sends commands and feedback to the perception layer.

#### Five-layer architecture
- The five-layer architecture is an extension and refinement of the three-layer architecture, which adds two more layers to address some of the limitations and challenges of the three-layer architecture, such as data management, security, and scalability .
- The five layers are:

  - Perception layer: This is the same as the three-layer architecture, which consists of physical devices that can sense, collect, and transmit data from the environment.
  - Transport layer: This is the second layer, which is responsible for transferring the data from the perception layer to the processing layer, and vice versa. It uses various network protocols, such as TCP/IP, UDP, MQTT, CoAP, etc., to ensure reliable and efficient data transmission over the internet.
  - Processing layer: This is the third layer, which is also known as the middleware layer, which provides the data processing, storage, and management functions for the IoT system. It uses various technologies, such as cloud computing, fog computing, edge computing, etc., to perform data filtering, aggregation, compression, encryption, etc., and to store and manage the data in databases or data centers.
  - Application layer: This is the fourth layer, which is similar to the three-layer architecture, which provides the services and applications for the end-users, such as smart home, smart city, smart health, smart agriculture, etc. It uses various techniques, such as machine learning, artificial intelligence, big data analytics, etc., to process, analyze, and display the data received from the processing layer, and to send commands and feedback to the perception layer.
  - Business layer: This is the fifth and highest layer, which provides the business and management functions for the IoT system. It uses various methods, such as business models, policies, strategies, etc., to manage the resources, users, and profits of the IoT system, and to ensure the security, privacy, and quality of service of the IoT system.

#### Semantic architecture
- The semantic architecture is an advanced and intelligent model of IoT, which focuses on making all things (not just those electronic, smart, or connected) accessible, interoperable, and understandable by humans and machines.
- The semantic architecture uses the concepts and technologies of the semantic web, such as ontologies, RDF, SPARQL, etc., to provide a common and standardized way of describing, representing, and querying the data, devices, and services of the IoT system.
- The semantic architecture can be seen as a layer on top of the existing IoT architectures, such as the three-layer or the five-layer architectures, which adds the semantic layer to provide the semantic interoperability and reasoning capabilities for the IoT system.
- The semantic layer consists of three sub-layers:

  - Semantic annotation: This sub-layer is responsible for annotating the data, devices, and services of the IoT system with semantic metadata, such as labels, tags, attributes, etc., that can describe their meaning, context, and relationships