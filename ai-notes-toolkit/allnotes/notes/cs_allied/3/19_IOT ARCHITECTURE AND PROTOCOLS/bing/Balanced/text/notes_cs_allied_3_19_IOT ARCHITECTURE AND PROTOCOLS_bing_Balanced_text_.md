

# IOT ARCHITECTURE AND PROTOCOLS

- IoT architecture refers to the many ways that IoT devices are structured to meet user needs. Based on complexity, IoT system elements are grouped into 3 to 7 layers, each with its own role.
- IoT protocols are the set of rules that enable communication between IoT devices, gateways, services and data centers. Different IoT protocols have been designed and optimized for different scenarios and usage.
- A common IoT architecture consists of the following layers  :
  - Device layer: This layer contains the sensors and actuators that collect data and perform actions in the physical world. They can be embedded, wearable, mobile or stationary devices. They can communicate using wired or wireless connections, and use various protocols depending on their capabilities and requirements.
  - Gateway layer: This layer acts as a bridge between the device layer and the cloud layer. It can aggregate, filter, process and transmit data from multiple devices to the cloud, and vice versa. It can also provide security, authentication, encryption and device management functions. It can be a dedicated hardware device, a software application or a combination of both.
  - Cloud layer: This layer provides the storage, processing and analysis of the data collected from the devices. It can also host the applications and services that enable the IoT functionality and user interaction. It can use various cloud computing models, such as public, private or hybrid clouds, and various cloud services, such as SaaS, PaaS or IaaS.
  - Application layer: This layer serves as the interface between the user and the device within a given IoT protocol. It can provide various functions, such as data visualization, analytics, control, notification, automation and integration. It can be accessed through various platforms, such as web, mobile or desktop applications.
- Some of the common IoT protocols are :
  - Message queue telemetry transport (MQTT): This is a lightweight, publish-subscribe protocol that enables efficient data exchange between devices and servers. It is suitable for low-power, low-bandwidth and unreliable networks. It uses TCP/IP as the transport layer and supports QoS levels and security mechanisms.
  - Constrained application protocol (CoAP): This is a web-based protocol that enables RESTful communication between devices and servers. It is suitable for constrained devices and networks that have limited resources and capabilities. It uses UDP as the transport layer and supports caching, discovery, multicast and security mechanisms.
  - Advanced message queuing protocol (AMQP): This is a binary, peer-to-peer protocol that enables reliable and secure data exchange between applications and services. It is suitable for high-performance, distributed and scalable systems. It uses TCP/IP as the transport layer and supports routing, queuing, transactions and security mechanisms.



## Unit 1 - IoT-An Architectural Overview

- IoT stands for Internet of Things, which is a network of physical devices, sensors, actuators, and software that can collect, process, and exchange data over the internet.
- IoT enables various applications and services that can improve the quality of life, efficiency, productivity, and sustainability of different domains, such as smart cities, smart homes, smart health, smart agriculture, smart industry, etc.
- IoT architecture is a conceptual framework that defines the components, layers, interfaces, and protocols of an IoT system, and how they interact and communicate with each other.
- IoT architecture can be divided into four main layers: perception layer, network layer, service layer, and application layer.
- Perception layer: This layer consists of the physical devices, sensors, and actuators that can sense, measure, and control the physical world. This layer is responsible for data acquisition, preprocessing, and transmission.
- Network layer: This layer provides the connectivity and communication between the perception layer and the service layer. This layer can use various wired or wireless technologies, such as Wi-Fi, Bluetooth, ZigBee, cellular, LoRaWAN, etc. This layer is responsible for data routing, forwarding, and security.
- Service layer: This layer provides the data storage, processing, and analysis capabilities for the IoT system. This layer can use various cloud computing, edge computing, or fog computing platforms, such as AWS, Azure, Google Cloud, etc. This layer is responsible for data management, processing, and analytics.
- Application layer: This layer provides the end-user interfaces and applications that can utilize the data and services provided by the service layer. This layer can use various web, mobile, or desktop applications, such as dashboards, alerts, notifications, etc. This layer is responsible for data visualization, interaction, and decision making.



### Building an architecture for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- An architecture for the notes of the Unit 1 can be based on the following main topics:

  - Introduction to IoT: Define what is IoT, its characteristics, applications, benefits and challenges.

  - IoT Architecture: Explain the different layers of IoT architecture, such as perception, network, middleware, application and business layers, and their functions and components.

  - IoT Protocols: Describe the various protocols used in IoT communication, such as MQTT, CoAP, HTTP, AMQP, XMPP, DDS, etc., and their features and advantages.

  - IoT Standards: Discuss the different standards and organizations involved in IoT development, such as IEEE, IETF, ITU, OCF, oneM2M, etc., and their roles and contributions.

  - IoT Security: Identify the main security threats and challenges in IoT, such as privacy, authentication, authorization, encryption, etc., and the possible solutions and best practices to mitigate them.

- An example of the architecture for the notes of the Unit 1 is shown below:

Unit 1 Notes Architecture

- The architecture for the notes of the Unit 1 can be used as a guide to organize and summarize the key concepts and information of the unit, and to facilitate the learning and revision process.



### Main design principles and needed capabilities for the notes of the Unit 1 - IoT-An Architectural Overview

- IoT-An Architectural Overview is a unit that introduces the basic concepts, architectures, and applications of the Internet of Things (IoT), which is a network of physical objects, sensors, and devices that can communicate and exchange data with minimal human intervention  .
- The main design principles of IoT architecture are   :
  - Openness: IoT architecture should be open to support interoperability, scalability, and integration of different devices, platforms, and services.
  - Service-orientation: IoT architecture should be service-oriented to provide real-world services that are accessible, reusable, and composable.
  - Security: IoT architecture should be secure to protect the data, devices, and services from unauthorized access, modification, or misuse.
  - Trust: IoT architecture should offer trust to the users, providers, and consumers of the IoT services, by ensuring reliability, availability, and quality of service.
- The needed capabilities of IoT architecture are  :
  - Perception: This is the layer that consists of the sensors, gadgets, and other devices that collect and generate data from the physical world.
  - Network: This is the layer that consists of the network structure and protocols that enable the data transmission and communication between the devices and the cloud.
  - Cloud: This is the layer that consists of the cloud technology and platforms that store, process, and analyze the data from the devices, and provide the services and applications for the IoT.
  - Application: This is the layer that consists of the user applications and interfaces that allow the users to access, control, and interact with the IoT services and devices.
  - Actuation: This is the layer that consists of the actuators and commands that perform actions on the physical world based on the data and insights from the IoT.



### An IoT architecture outline for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- IoT architecture is the system of numerous elements that enable IoT devices to communicate with each other and perform various tasks.
- A basic IoT architecture consists of three layers: perception, network, and application.
- Perception layer: This layer comprises the sensors, actuators, and other smart devices that collect data from the physical environment and perform actions based on commands .
- Network layer: This layer comprises the network devices and communications types and protocols that transmit data between the perception layer and the application layer  . Examples of network devices are routers, gateways, and switches. Examples of communications types and protocols are 5G, Wi-Fi, Bluetooth, MQTT, and CoAP.
- Application layer: This layer comprises the cloud services, platforms, and applications that store, process, and analyze data from the network layer and provide feedback and control to the perception layer  . Examples of cloud services are AWS IoT, Azure IoT, and Google Cloud IoT. Examples of platforms and applications are IoT dashboards, analytics tools, and user interfaces.
- Some IoT architectures may have additional layers or components, such as edge computing, middleware, security, and management  .
- Edge computing: This is a component that enables data processing and analysis at the edge of the network, closer to the perception layer, to reduce latency and bandwidth consumption .
- Middleware: This is a layer that provides interoperability and integration between different IoT devices, platforms, and applications, as well as data abstraction and standardization .
- Security: This is a component that provides authentication, encryption, and authorization for IoT devices, data, and communications, as well as protection from cyberattacks and privacy breaches .
- Management: This is a component that provides monitoring, configuration, and maintenance of IoT devices, networks, and applications, as well as fault detection and recovery .



### Standards considerations for the notes of the Unit 1 - IoT-An Architectural Overview

- The notes should provide a clear and concise introduction to the concept, definition, and characteristics of the Internet of Things (IoT).
- The notes should explain the main components and layers of a basic IoT architecture, such as perception, network, cloud, and application .
- The notes should describe the different architectural views and design principles of IoT, such as functional, information, deployment, operational, and business .
- The notes should highlight the key challenges and requirements of IoT, such as scalability, interoperability, security, privacy, and trust  .
- The notes should include examples and use cases of IoT applications in various domains, such as smart home, smart city, smart health, smart agriculture, and smart industry .
- The notes should follow a consistent and logical structure, using headings, subheadings, bullet points, diagrams, and tables to organize and present the information.
- The notes should cite the sources of information using numerical references and provide a list of references at the end of the notes.



### M2M and IoT Technology Fundamentals

- M2M stands for Machine-to-Machine communication, which is the exchange of data between two or more devices without human intervention.
- M2M technology was first adopted in manufacturing and industrial settings, where other technologies, such as SCADA and remote monitoring, helped remotely manage and control data from equipment.
- M2M has since found applications in other sectors, such as healthcare, business and insurance, where it enables remote monitoring, diagnostics, maintenance, asset tracking, security, etc.
- M2M uses point-to-point communication, which means that each device has a direct connection to another device or a central server. M2M devices typically use wired or wireless networks, such as cellular, Wi-Fi, Bluetooth, Zigbee, etc.
- IoT stands for Internet of Things, which is the network of physical objects embedded with sensors, software, and other technologies that enable them to connect and exchange data with other devices and systems over the internet.
- IoT involves communication between machines without human input, making it by definition a form of M2M communication. However, IoT expands the power and potential of M2M technology in new ways.
- The biggest difference between M2M and IoT is that an M2M system uses point-to-point communication, while an IoT system typically situates its devices within a global cloud network that allows larger-scale integration and more sophisticated applications.
- Scalability is another key difference between M2M and IoT. M2M systems are limited by the number of devices that can be connected and the bandwidth that can be allocated to each device. IoT systems, on the other hand, can leverage the cloud infrastructure, software, and platform to support millions of devices and massive amounts of data.
- IoT also enables more interoperability and intelligence among devices, as they can communicate using common protocols and standards, and leverage artificial intelligence, machine learning, and analytics to derive insights and actions from the data.
- IoT has applications in various domains, such as smart cities, smart homes, smart agriculture, smart healthcare, smart manufacturing, smart energy, smart transportation, etc.



### Devices and gateways for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Devices are the physical or virtual objects that can sense, actuate, compute, and communicate data in an IoT system. They can be classified into three types: sensors, actuators, and smart devices.
- Sensors are devices that can measure physical phenomena, such as temperature, humidity, light, sound, motion, etc. and convert them into electrical signals.
- Actuators are devices that can perform physical actions, such as turning on/off a switch, opening/closing a valve, moving a robot arm, etc. based on electrical signals.
- Smart devices are devices that can perform both sensing and actuation functions, as well as processing, storage, and communication of data. They can also run applications and interact with users.
- Gateways are intelligent central hubs that connect IoT devices and sensors to cloud-based data processing and computing. They perform various functions, such as   :
  - Security: They provide authentication, encryption, and firewall services to protect the data and devices from unauthorized access and attacks.
  - Device layer: They consist of hardware components, such as microprocessor, connectivity module, sensors, and circuitry, that enable the gateway to interact with the devices and sensors.
  - Data management: They collect, filter, aggregate, and store data from multiple devices and sensors, and send it to the cloud or other gateways for further analysis and processing.
  - Operating system: They run software that controls the hardware and other programs on the gateway, such as Linux, Windows, or Android.
  - Hardware abstraction: They provide a common interface for different types of devices and sensors, regardless of their communication protocols, data formats, and functionalities.
  - Gateway data transfer: They transfer data between devices and sensors, as well as between the gateway and the cloud, using various communication protocols, such as Wi-Fi, Bluetooth, Zigbee, MQTT, CoAP, etc.
  - Communication protocols: They translate between different communication protocols used by the devices and sensors, such as analog, digital, serial, parallel, etc., to enable interoperability and compatibility.
  - Cloud connectivity manager: They manage the connection and authentication with the cloud services, such as AWS, Azure, or Google Cloud, and handle the data transmission and reception.
- The architecture of IoT gateways can be represented by the following diagram:

IoT gateway architecture

: https://www.intuz.com/blog/the-workings-of-an-iot-gateway
: https://www.checkpoint.com/cyber-hub/network-security/what-is-iot/what-is-an-iot-gateway/
: https://www.geeksforgeeks.org/internet-of-things-iot-gateways/
: https://www.thalesgroup.com/en/markets/digital-identity-and-security/iot/inspired/iot-gateway
: https://www.techtarget.com/iotagenda/tip/A-comprehensive-view-of-the-4-IoT-architecture-layers



### Local and Wide Area Networking for IoT

- Local area networks (LAN) and wide area networks (WAN) are two types of networks that can be used to connect IoT devices to each other and to the internet.
- A LAN is a network that covers a small geographic area, such as a home, office, or building. A LAN typically uses wired or wireless technologies, such as Ethernet, WiFi, or Bluetooth, to connect devices within a short range (less than 1000 meters)  .
- A WAN is a network that covers a large geographic area, such as a city, country, or continent. A WAN typically uses cellular, satellite, or fiber-optic technologies, such as 4G, 5G, or LoRaWAN, to connect devices across long distances (more than 1000 meters)  .
- LAN and WAN have different advantages and disadvantages for IoT applications, depending on the requirements of data rate, latency, power consumption, cost, and scalability.
- LAN technologies, such as WiFi and Bluetooth, offer high data rates (up to Mbps) and low latency (less than 10 ms), but they also consume more power and have limited coverage and capacity  .
- WAN technologies, such as cellular and LoRaWAN, offer low data rates (up to Kbps) and high latency (more than 100 ms), but they also consume less power and have wide coverage and capacity  .
- Some IoT applications may use a combination of LAN and WAN technologies, such as WiFi for local communication and cellular for remote communication, to achieve the best trade-off between performance and efficiency .



### Data management for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Data management is the process of collecting, storing, processing, and analyzing data from various sources, such as sensors, devices, applications, and users, in the context of the Internet of Things (IoT).
- Data management is essential for the IoT because it enables the extraction of meaningful insights and value from the large and heterogeneous data generated by the IoT devices and applications.
- Data management for the IoT involves several challenges, such as:
  - Data volume: The IoT generates a huge amount of data, which requires efficient storage and processing techniques to handle the data at scale.
  - Data velocity: The IoT data is often generated at high speed and frequency, which requires real-time or near-real-time processing and analysis techniques to cope with the data stream.
  - Data variety: The IoT data is diverse in terms of sources, formats, types, and quality, which requires interoperable and flexible data models and standards to integrate and harmonize the data.
  - Data veracity: The IoT data is often noisy, incomplete, inconsistent, or inaccurate, which requires data cleaning, validation, and quality assessment techniques to ensure the reliability and trustworthiness of the data.
  - Data value: The IoT data is often raw, unstructured, or unlabelled, which requires data mining, machine learning, and artificial intelligence techniques to extract useful patterns, knowledge, and intelligence from the data.
- Data management for the IoT can be divided into four main phases, namely:
  - Data acquisition: This phase involves the collection and transmission of data from the IoT devices and sensors to the data storage or processing platforms, such as cloud, fog, or edge computing systems. This phase requires efficient data compression, encryption, and communication protocols to ensure the security, privacy, and integrity of the data.
  - Data storage: This phase involves the organization and preservation of data in the data storage or processing platforms, such as databases, data warehouses, or data lakes. This phase requires scalable and distributed data storage systems and techniques to handle the large and heterogeneous data sets.
  - Data processing: This phase involves the transformation and analysis of data in the data storage or processing platforms, such as data preprocessing, data integration, data aggregation, data filtering, data mining, machine learning, or artificial intelligence. This phase requires parallel and distributed data processing systems and techniques to handle the high-speed and high-frequency data streams.
  - Data visualization: This phase involves the presentation and communication of data to the end-users or applications, such as dashboards, reports, charts, graphs, or maps. This phase requires interactive and intuitive data visualization tools and techniques to enable the exploration and interpretation of the data insights and value.



### Business processes in IoT

- A business process is a collection of related events, activities and decisions that involve a number of factors and resources, which collectively lead to an outcome that is of value for the organisation and the customer.
- IoT (Internet of Things) is the network of physical objects embedded with sensors, software and other technologies that enable them to connect and exchange data with other devices and systems over the internet.
- IoT can improve business processes by automating tasks, gathering valuable information, extending business functions, triggering rules, sourcing predictive analytics and big data, among other useful objectives.
- Some examples of business processes that can benefit from IoT are:
  - Inventory management: IoT devices can track the location, quantity and condition of goods in real time, reducing errors, waste and costs.
  - Quality control: IoT devices can monitor and measure the performance and quality of products and processes, detecting defects, anomalies and deviations, and providing feedback and alerts.
  - Asset management: IoT devices can collect and analyse data from machines and equipment, enabling predictive maintenance, remote control and optimisation of operations.
  - Customer service: IoT devices can enhance the customer experience by providing personalised recommendations, support and feedback, as well as enabling self-service and loyalty programs.
- Some recommendations on implementing IoT business processes are:
  - To define the business process to improve and identify the problem to solve.
  - To use an end-to-end approach that covers the entire value chain of the process, from data collection to action execution.
  - To make agile design and start with POC (proof of concept) prototyping, testing and validating the solution before scaling up.
  - To get on board the right people, with the best knowledge and skills, and keep the team size low but efficient.
  - To be persistent but acknowledgeable to failure, and learn from mistakes and feedback.
  - To be aware of the potential disruption that IoT can bring, but not go crazy about it, and focus on the value proposition and the customer needs.



### Everything as a Service (XaaS) for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Everything as a Service (XaaS) is a general term that describes the delivery of any IT function as a service over the internet, using cloud computing and remote access technologies  .
- XaaS originated from the Software as a Service (SaaS) model, which provides software applications on demand, without requiring installation or maintenance on the user's device .
- XaaS has expanded to include other types of services, such as Infrastructure as a Service (IaaS), which provides computing resources such as servers, storage, and networking; Platform as a Service (PaaS), which provides development and deployment tools and environments; and more functionally-specific models, such as Storage as a Service (StaaS), Desktop as a Service (DaaS), and Disaster Recovery as a Service (DRaaS)   .
- XaaS offers many benefits to both providers and consumers of IT services, such as:
  - Cost reduction: XaaS eliminates the need for upfront capital investment, maintenance, and upgrade costs, and allows users to pay only for what they use    .
  - Scalability: XaaS enables users to easily adjust the amount and type of services they need, depending on their changing demands and preferences    .
  - Flexibility: XaaS allows users to access services from any device and location, and to choose from a variety of service options and features    .
  - Innovation: XaaS enables providers to offer new and improved services faster and more frequently, and allows users to benefit from the latest technologies and capabilities     .
- XaaS is closely related to the Internet of Things (IoT), which is the network of physical objects that are embedded with sensors, software, and connectivity, and can communicate and exchange data with other devices and systems.
- XaaS can enable IoT applications by providing the necessary infrastructure, platforms, software, and services to collect, process, analyze, and act on the data generated by the IoT devices .
- XaaS can also benefit from IoT data by using it to improve the quality, performance, and security of the services, and to create new value-added services and features for the users  .
- XaaS and IoT are both part of the digital transformation that is reshaping the business landscape and creating new opportunities and challenges for enterprises and consumers .



### M2M and IoT Analytics

- M2M and IoT are both technologies that enable remote communication and data exchange among machines without human intervention.
- M2M stands for machine-to-machine, and IoT stands for Internet of Things.
- The main difference between M2M and IoT is that M2M is a point-to-point connection of two or more devices over cellular or wired networks, while IoT is a network of devices that connect to the Internet and use IP-based protocols for data transmission and processing .
- M2M is more of a vertical application that meets internal demands, such as remote monitoring, asset tracking, or smart metering, while IoT is more of a horizontal application that has overarching results or open-ended capabilities, such as smart cities, smart homes, or smart health.
- M2M and IoT analytics are the processes of collecting, storing, analyzing, and visualizing the data generated by M2M and IoT devices, respectively.
- M2M and IoT analytics can provide insights into the performance, behavior, status, and trends of the devices, as well as the environment, users, and business processes associated with them.
- M2M and IoT analytics can help improve operational efficiency, reduce costs, enhance customer experience, optimize decision making, and create new value propositions and business models.
- M2M and IoT analytics require different platforms, tools, and techniques to handle the volume, variety, velocity, and veracity of the data.
- M2M analytics typically use proprietary or legacy platforms that are designed for specific use cases and data formats, while IoT analytics use cloud-based or open-source platforms that are scalable, flexible, and interoperable.
- M2M analytics usually rely on traditional data analysis methods, such as descriptive, diagnostic, or predictive analytics, while IoT analytics leverage advanced data analysis methods, such as prescriptive, cognitive, or edge analytics.



### Knowledge Management for the notes of the Unit 1 - IoT-An Architectural Overview

- Knowledge management (KM) is the process of creating, sharing, using and managing the knowledge and information of an organization or a network of entities.
- KM can generate intelligence in IoT ecosystems to enable a digital business and society transformation by leveraging the interactive and dynamic relationship among data, information and knowledge that feedback continuously the process.
- IoT architecture is the structure enabling internet-connected devices to communicate with other devices and systems. It comprises of several IoT system building blocks connected to ensure that sensor-generated device data is collected, stored, and processed in the big data warehouse and that devices’ actuators perform commands sent via a user application.
- A standard IoT solution architecture consists of five basic elements:
  - Devices are industrial equipment, sensors, and microcontrollers that connect with the cloud to send and receive data.
  - Provisioning enables devices to take actions and communicate with the cloud.
  - Communication protocols enable devices to securely connect and exchange data with the cloud.
  - Data processing and analytics enable the cloud to store, process, and analyze the data received from the devices.
  - User applications enable users to interact with the devices and the data through web or mobile interfaces.
- An IoT architecture can be divided into three main layers: perception, transport, and application.
  - Perception layer consists of sensors and actuators that collect and transmit data from the physical world to the digital world.
  - Transport layer consists of communication networks and protocols that enable data transmission between the perception layer and the application layer.
  - Application layer consists of software and services that provide functionality and value to the users and the business based on the data from the perception layer.
- An IoT architecture can also include some additional layers, such as edge computing, cloud computing, and security .
  - Edge computing enables data processing and analytics at the edge of the network, closer to the devices, to reduce latency and bandwidth consumption.
  - Cloud computing enables data storage, processing, and analytics at the cloud, which provides scalability, reliability, and flexibility.
  - Security enables data protection and privacy across the IoT architecture, from the devices to the cloud, using encryption, authentication, and authorization mechanisms.



## Unit 2 - Reference Architecture

- A reference architecture is a general and reusable solution to a commonly occurring problem in a specific domain or context.
- It provides a set of principles, guidelines, patterns, standards, and best practices that can be used to design, implement, and evaluate a specific architecture.
- A reference architecture is not a complete and detailed architecture, but rather a template or blueprint that can be customized and adapted to meet the specific needs and requirements of a particular system or organization.
- A reference architecture can help to ensure consistency, interoperability, scalability, security, and quality of the architectures that are derived from it.
- A reference architecture can also facilitate communication, collaboration, and learning among the stakeholders involved in the architecture process, such as architects, developers, users, customers, and managers.
- A reference architecture can be represented in various forms, such as diagrams, models, documents, or code. It can also be expressed at different levels of abstraction, such as conceptual, logical, or physical.
- A reference architecture can be developed and maintained by different entities, such as standards organizations, industry consortia, academic institutions, or individual experts. It can also be published and shared through various channels, such as books, journals, websites, or repositories.



### IoT Architecture-State of the Art

- A reference model is a model that describes the main conceptual entities and how they are related to each other, while the reference architecture aims at describing the main functional components of a system as well as how the system works, how the system is deployed, what information the system processes, etc.
- The principles of Reactive Systems define the state-of-the-art programming models for IoT. Because IoT devices are sensing and actuating physical systems, many of which are critical infrastructure for energy, food, healthcare, and transportation, it is important that they stay responsive, and operate safely and securely.
- IoT platforms must tackle asset management as a foundational problem and all of these platforms have facilities for managing the provisioning of devices and services, public key infrastructure (PKI), software and firmware updates, and desired-state configuration of devices, at huge scale.
- The paper will address the topic of IoT, the state of the art of IoT, and how IoT is used for fog, in 6G, and cloud computing. It surveys IoT architecture and sensors used in development and security together with their potential applications, such as system tuning and diagnosis.
- Internet of things (IoT) constitutes one of the most important technological development in the last decade. It has the potential to deeply affect our life style. However, its success relies greatly on a well-defined architecture that will provide scalable, dynamic, and secure basement to its deployment.



### Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- In this unit, we will learn about the concept of reference architecture for the Internet of Things (IoT) and its benefits and challenges.
- A reference architecture is a generic blueprint that defines the structure, components, interfaces, and interactions of a system or a domain of interest.
- A reference architecture can be used as a guide or a template for designing and implementing specific architectures for concrete applications or scenarios.
- A reference architecture can also facilitate interoperability, standardization, and reuse of existing solutions and best practices.
- A reference architecture for IoT can help address the complexity, heterogeneity, and scalability of IoT systems and enable the integration of various IoT devices, platforms, and services.
- A reference architecture for IoT can also support the development of common IoT functionalities, such as device management, data processing, security, privacy, and governance.
- There are different approaches and models for developing a reference architecture for IoT, such as the ISO/IEC 30141, the IoT-A, the IIRA, and the RAMI 4.0.
- In this unit, we will compare and contrast these different reference architectures for IoT and analyze their strengths and weaknesses.
- We will also discuss the key design principles and challenges for developing and applying a reference architecture for IoT.



### State of the art for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- A reference model is a model that describes the main conceptual entities and how they are related to each other, while the reference architecture aims at describing the main functional components of a system as well as how the system works, how the system is deployed, what information the system processes, etc.
- A reference architecture provides a common vocabulary, reusable designs, and best practices for IoT systems. It also facilitates interoperability, scalability, and security of IoT solutions.
- There are different approaches to design IoT reference architectures, depending on the level of abstraction, the scope, and the purpose of the architecture. Some examples are:
  - The three-layer architecture, which consists of three layers: perception, network, and application. The perception layer is responsible for sensing and collecting data from the physical world. The network layer is responsible for transmitting and processing the data. The application layer is responsible for providing services and applications to the end-users.
  - The five-layer architecture, which extends the three-layer architecture by adding two layers: processing and business. The processing layer is responsible for data analysis, storage, and management. The business layer is responsible for business logic, decision making, and management.
  - The IoT-A reference architecture, which is a comprehensive and domain-independent architecture developed by the European IoT-A project. It defines a set of architectural reference models, such as the functional model, the information model, the communication model, the trust, security and privacy model, and the IoT reference architecture model. It also defines a set of architectural design guidelines and best practices for IoT systems.
- The state of the art for IoT also includes the emerging computing paradigms and technologies that enable IoT systems, such as fog computing, edge computing, cloud computing, 6G, and artificial intelligence. These paradigms and technologies aim to address the challenges and requirements of IoT, such as low latency, high bandwidth, massive connectivity, distributed processing, security, and intelligence.



### Reference Model and Architecture for IoT

- A reference model is a conceptual framework that defines the common terminology, concepts, and principles for designing and implementing IoT systems.
- A reference architecture is a concrete instantiation of a reference model that provides specific guidance and best practices for developing IoT solutions.
- One of the most widely used reference models for IoT is the IoT World Forum Reference Model, which was proposed by the IoT World Forum, a consortium of industry leaders, academia, and government organizations.
- The IoT World Forum Reference Model consists of seven layers, as shown in the following diagram:

IoT World Forum Reference Model

- The seven layers are:

  - **Physical Devices and Controllers Layer**: This layer includes the physical devices and sensors that generate and collect data, as well as the controllers and actuators that manipulate the physical world.
  - **Connectivity Layer**: This layer provides the communication protocols and network infrastructure that enable data transmission and device management across different networks and domains.
  - **Edge Computing Layer**: This layer performs data processing and analytics at the edge of the network, close to the data sources, to reduce latency, bandwidth, and storage requirements.
  - **Data Accumulation Layer**: This layer stores and aggregates the data from multiple sources and formats, and provides data access and query capabilities.
  - **Data Abstraction Layer**: This layer transforms and normalizes the data into a common format and structure, and provides data services and APIs for consumption by other layers and applications.
  - **Application Layer**: This layer implements the business logic and functionality of the IoT system, and provides user interfaces and user experience.
  - **Collaboration and Processes Layer**: This layer enables collaboration and integration among different IoT systems, applications, and users, and supports business processes and workflows.

- The IoT World Forum Reference Model is not a prescriptive or definitive model, but rather a flexible and adaptable framework that can be customized and extended to suit different IoT scenarios and requirements.
- The IoT World Forum Reference Model also provides a common vocabulary and understanding for IoT stakeholders, and facilitates interoperability and standardization among IoT solutions.



### IoT Reference Model

- The IoT Reference Model is a framework that defines the main concepts, components, and relationships of IoT systems and architectures.
- It consists of the following sub-models:
  - IoT Domain Model: This model introduces the basic concepts of IoT, such as devices, IoT services, virtual entities, and their relations.
  - IoT Functional View: This model describes the main functions and capabilities of IoT systems, such as identification, communication, discovery, composition, and management.
  - IoT Information View: This model defines the information and data models of IoT systems, such as data formats, semantics, and ontologies.
  - IoT Communication View: This model specifies the communication protocols and standards of IoT systems, such as network layers, security, and interoperability.
  - IoT Deployment and Operation View: This model covers the deployment and operation aspects of IoT systems, such as configuration, monitoring, and maintenance.
- The IoT Reference Model aims to establish a common grounding and a common language for IoT architectures and IoT systems .
- The IoT Reference Model provides the concepts and definitions on which IoT architectures can be built.



### IoT Reference Architecture

- IoT reference architecture is a conceptual framework that defines the components, interactions, and principles of an IoT solution.
- IoT reference architecture can help to guide the design, development, and deployment of IoT solutions that are scalable, secure, interoperable, and adaptable to different domains and use cases.
- IoT reference architecture can also facilitate the communication and collaboration among different stakeholders, such as developers, vendors, customers, and regulators, by providing a common vocabulary and understanding of IoT concepts and systems.
- There are different IoT reference architectures proposed by various organizations, such as IBM, Microsoft, and the IoT-A project, but they share some common elements and layers, such as:

  - **Things layer**: This layer consists of the physical or virtual devices that generate, collect, process, and transmit data in an IoT system. These devices can have different capabilities, such as sensing, actuating, computing, and communicating, and can use different protocols and standards to connect to the network.
  - **Network layer**: This layer provides the connectivity and communication infrastructure for the IoT system. It can include different types of networks, such as wired, wireless, cellular, satellite, and mesh, and different protocols, such as TCP/IP, MQTT, CoAP, and AMQP, to enable data transmission and exchange among devices and other components.
  - **Service layer**: This layer provides the functionality and logic for the IoT system. It can include different types of services, such as device management, data management, analytics, security, and application, that can be hosted on the cloud or on the edge. These services can process, store, analyze, and visualize the data from the devices, and provide APIs and interfaces for the users and applications to access and control the IoT system.
  - **Application layer**: This layer consists of the end-user applications and interfaces that consume the data and services from the IoT system. These applications can provide different functionalities and value propositions for the users, such as monitoring, control, automation, optimization, and decision support, and can be tailored to different domains and use cases, such as smart home, smart city, smart agriculture, smart health, and smart industry.



### Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- In this unit, we will learn about the concept of reference architecture for the Internet of Things (IoT) and its benefits and challenges.
- A reference architecture is a generic blueprint that defines the structure, components, interfaces, and interactions of a system or a domain of interest.
- A reference architecture can be used as a guide or a template for designing and implementing specific architectures for concrete applications or scenarios.
- A reference architecture can also facilitate interoperability, standardization, and reuse of existing solutions and best practices.
- A reference architecture for IoT can help address the complexity, heterogeneity, and scalability of IoT systems and enable the integration of various IoT devices, platforms, and services.
- A reference architecture for IoT can also support the development of common IoT functionalities, such as device management, data processing, security, privacy, and governance.
- There are different approaches and models for developing a reference architecture for IoT, such as the ISO/IEC 30141, the IoT-A, the IIRA, and the RAMI 4.0.
- In this unit, we will compare and contrast these different reference architectures for IoT and analyze their strengths and weaknesses.
- We will also discuss the key design principles and challenges for developing and applying a reference architecture for IoT.



### Functional View for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The functional view describes the system's runtime functional components, their responsibilities, default functions, interfaces and primary interactions .
- The functional view of the IoT-A reference architecture, depicted in Figure 1, follows the modular structure of functional blocks organized into layers, as it was proposed e.g. in SENSEI .
- The functional view consists of four layers: Device Layer, Network Layer, Service Layer and Application Layer  .
- The Device Layer contains the physical devices that are connected to the IoT system, such as sensors, actuators, RFID tags, etc. The Device Layer provides the basic functions for device management, data acquisition, data processing and actuation  .
- The Network Layer provides the communication infrastructure and protocols for data transmission and routing between devices and services. The Network Layer supports various network technologies, such as wired, wireless, cellular, etc. The Network Layer also provides functions for network management, security and quality of service  .
- The Service Layer provides the core functionalities and abstractions for the IoT system, such as discovery, identity, virtualization, composition, etc. The Service Layer enables interoperability and integration of heterogeneous devices and services. The Service Layer also provides functions for service management, security and governance   .
- The Application Layer contains the end-user applications that consume and provide IoT services. The Application Layer supports various application domains, such as smart home, smart city, smart health, etc. The Application Layer also provides functions for application management, security and user interface   .

Figure 1: IoT-A reference architecture, functional view

Figure 1



### Information View for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The information view describes the data and information that the system handles, such as the types, formats, sources, destinations, flows, and quality of the data .
- The information view can help to identify the data requirements, dependencies, and interactions among the system components, as well as the security and privacy aspects of the data .
- The information view can be represented by different models and diagrams, such as:
  - Data model: A graphical representation of the data entities, attributes, relationships, and constraints in the system.
  - Data flow diagram: A graphical representation of the data sources, processes, outputs, and flows in the system.
  - Data dictionary: A textual description of the data elements, their definitions, formats, and values in the system.
  - Data quality model: A graphical or textual representation of the data quality dimensions, metrics, and indicators in the system.
- The information view can be aligned with the functional view and the deployment and operational view to ensure the consistency and coherence of the system design .
- The information view can be influenced by the reference model and architecture of the IoT domain, such as the IoT-A reference model and architecture .



### Deployment and Operational View

- The deployment and operational view describes the main real world components of the system such as devices, network routers, servers, etc. and how they are deployed and operated .
- The deployment view focuses on the physical layout and configuration of the system, such as the hardware, software, and network components, and how they are connected and distributed .
- The operational view focuses on the runtime behavior and management of the system, such as the data flows, communication protocols, security mechanisms, and monitoring and maintenance activities .
- The deployment and operational view can vary depending on the specific IoT domain, application, and scenario, and therefore there is no one-size-fits-all solution.
- However, some common aspects of the deployment and operational view that are relevant for most IoT systems are:
  - The identification and classification of the IoT devices and their capabilities, such as sensors, actuators, gateways, etc.
  - The selection and configuration of the IoT communication technologies and protocols, such as Wi-Fi, Bluetooth, ZigBee, MQTT, CoAP, etc.
  - The design and implementation of the IoT data processing and storage components, such as cloud services, databases, stream analytics, etc.
  - The integration and interoperability of the IoT components with other systems and platforms, such as web services, mobile apps, enterprise systems, etc.
  - The security and privacy of the IoT data and devices, such as encryption, authentication, authorization, etc.
  - The monitoring and management of the IoT system performance, availability, reliability, and scalability, such as logging, alerting, troubleshooting, etc.



### Other Relevant Architectural Views for IoT

- Apart from the functional view, which describes the components and interactions of an IoT system, there are other relevant architectural views that can help to understand and design IoT systems at different levels of abstraction and perspectives.
- Some of the other architectural views are:

  - **Contextual view**: This view shows the context and scope of the IoT system, including the stakeholders, goals, requirements, and boundaries. It helps to identify the purpose and value proposition of the IoT system, as well as the assumptions and constraints that affect its design and implementation. 
  - **Conceptual view**: This view shows the high-level concepts and principles that guide the design of the IoT system, such as the data model, the communication paradigm, the security and privacy policies, and the governance model. It helps to establish a common vocabulary and understanding among the stakeholders, and to align the IoT system with the business and technical objectives. 
  - **Logical view**: This view shows the logical structure and behavior of the IoT system, such as the entities, relationships, processes, and rules that define the system's functionality and logic. It helps to specify the requirements and constraints of the IoT system, and to design the system's architecture and components. 
  - **Physical view**: This view shows the physical deployment and configuration of the IoT system, such as the devices, networks, platforms, and services that constitute the system's infrastructure and resources. It helps to implement, deploy, and operate the IoT system, and to optimize its performance, scalability, and reliability. 
  - **Operational view**: This view shows the operational aspects and characteristics of the IoT system, such as the monitoring, management, maintenance, and evolution of the system's components and processes. It helps to ensure the quality and availability of the IoT system, and to address the challenges and risks that arise during its lifecycle. 

- These views are not mutually exclusive, but rather complementary and interrelated. They can be used to describe different aspects and perspectives of the same IoT system, or to compare and contrast different IoT systems. They can also be refined and extended according to the specific needs and preferences of the stakeholders and the domain of the IoT system.



### Real-World Design Constraints for IoT Reference Architecture

- Real-world design constraints are the factors that limit or influence the design choices and implementation of IoT systems in practical scenarios.
- Some of the common real-world design constraints are:
  - Technical design constraints: These are the challenges related to the hardware, software, network, security, and interoperability of IoT devices and systems. For example, IoT devices may have limited power, memory, processing, and communication capabilities, which affect their performance and functionality. IoT systems may also face security threats, such as unauthorized access, data breaches, or denial-of-service attacks, which require robust encryption, authentication, and authorization mechanisms. IoT systems may also need to interoperate with different protocols, standards, and platforms, which require common interfaces and data models.
  - Social design constraints: These are the challenges related to the human aspects of IoT systems, such as user acceptance, privacy, ethics, and social impact. For example, IoT systems may collect and process personal or sensitive data from users, which may raise privacy and ethical concerns. Users may also have different preferences, expectations, and behaviors, which affect their adoption and satisfaction with IoT systems. IoT systems may also have positive or negative effects on the society and the environment, such as improving health, safety, and efficiency, or creating pollution, waste, or inequality.
  - Business design constraints: These are the challenges related to the economic and legal aspects of IoT systems, such as cost, value, revenue, and regulation. For example, IoT systems may require significant investments in infrastructure, maintenance, and operation, which affect their profitability and scalability. IoT systems may also need to create and deliver value to the customers, stakeholders, and partners, which require innovative business models and strategies. IoT systems may also have to comply with various laws and regulations, such as data protection, consumer rights, and intellectual property, which affect their legality and liability.



### Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- In this unit, we will learn about the concept of reference architecture for the Internet of Things (IoT) and its benefits and challenges.
- A reference architecture is a set of principles, guidelines, standards, and best practices that provide a common framework and vocabulary for designing and implementing IoT systems.
- A reference architecture can help to address the complexity, heterogeneity, scalability, interoperability, security, and privacy issues of IoT systems by providing a clear and consistent structure and logic for their components and interactions.
- A reference architecture can also facilitate the reuse and integration of existing and emerging technologies, protocols, and services for IoT applications and domains.
- There are different types of reference architectures for IoT, such as domain-specific, generic, or hybrid, depending on the level of abstraction, scope, and applicability of the architecture.
- Some examples of reference architectures for IoT are the IoT-Architecture (IoT-A) project, the IEEE P2413 standard, the Industrial Internet Reference Architecture (IIRA), and the Reference Architecture Model for Industrie 4.0 (RAMI 4.0).
- In this unit, we will compare and contrast these reference architectures and analyze their strengths and weaknesses for different IoT scenarios and requirements.



### Technical Design Constraints of Hardware in IoT

- Hardware design for IoT involves creating embedded systems that can communicate with other devices and networks securely and efficiently.
- Hardware design constraints are the limitations or challenges that affect the performance, functionality, cost, and reliability of IoT hardware systems.
- Some of the common hardware design constraints for IoT are:

  - **Power consumption**: IoT devices often need to operate on batteries or harvested energy sources, which limits the amount of power available for sensing, processing, and communication. Power consumption also affects the lifetime and maintenance of IoT devices. Designers need to optimize the power management and energy efficiency of IoT hardware systems to reduce power consumption and extend battery life.
  - **Security**: IoT devices are exposed to various security threats, such as physical tampering, unauthorized access, data theft, malware attacks, and denial-of-service attacks. Security is essential to protect the confidentiality, integrity, and availability of IoT data and services. Designers need to implement security mechanisms at different levels of IoT hardware systems, such as encryption, authentication, access control, and secure boot.
  - **Scalability**: IoT devices are expected to operate in large-scale and dynamic networks, with potentially millions of devices and heterogeneous technologies. Scalability is the ability of IoT hardware systems to handle the increasing number and diversity of devices and data without compromising the performance and quality of service. Designers need to consider the scalability of IoT hardware systems in terms of communication protocols, data processing, storage, and management.
  - **Reliability**: IoT devices are often deployed in harsh and unpredictable environments, such as industrial plants, smart cities, and healthcare settings. Reliability is the ability of IoT hardware systems to function correctly and consistently under various conditions and scenarios. Designers need to ensure the reliability of IoT hardware systems by addressing the issues of fault tolerance, error detection and correction, self-healing, and redundancy.
  - **Cost and time-to-market**: IoT devices are usually mass-produced and have to compete with other products in the market. Cost and time-to-market are the factors that affect the profitability and success of IoT hardware systems. Designers need to balance the trade-offs between the quality and complexity of IoT hardware systems and the cost and time required for development and production. Designers also need to comply with the standards and regulations of IoT markets and domains.



### Data representation and visualization for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Data representation and visualization are important aspects of IoT systems, as they enable users to understand and interact with the data collected and processed by various smart devices and sensors.
- Data representation refers to the way data is encoded, stored, and transmitted in IoT systems. Data representation can affect the performance, scalability, security, and interoperability of IoT systems. Some of the factors that influence data representation are:
  - Data format: The structure and syntax of the data, such as JSON, XML, CSV, etc.
  - Data model: The logical and semantic organization of the data, such as relational, hierarchical, graph, etc.
  - Data schema: The definition and description of the data elements, attributes, and relationships, such as XML Schema, JSON Schema, etc.
  - Data compression: The technique of reducing the size of the data, such as gzip, zip, etc.
  - Data encryption: The technique of protecting the data from unauthorized access, such as AES, RSA, etc.
- Data visualization refers to the way data is presented and displayed to the users, such as charts, graphs, maps, dashboards, etc. Data visualization can help users to gain insights, discover patterns, and make decisions based on the data. Some of the factors that influence data visualization are:
  - Data type: The nature and characteristics of the data, such as numerical, categorical, temporal, spatial, etc.
  - Data dimension: The number of variables or attributes in the data, such as one-dimensional, two-dimensional, multidimensional, etc.
  - Data scale: The range and distribution of the data values, such as linear, logarithmic, ordinal, etc.
  - Data quality: The accuracy, completeness, consistency, and validity of the data, such as missing values, outliers, errors, etc.
  - Data analysis: The process of applying statistical and mathematical methods to the data, such as aggregation, filtering, clustering, correlation, etc.
  - Data design: The principles and guidelines of creating effective and appealing data visualizations, such as color, shape, size, layout, etc.
- Data representation and visualization in IoT systems can be challenging due to the following reasons:
  - Data volume: The amount of data generated by IoT devices can be huge and overwhelming, requiring efficient storage and transmission methods.
  - Data velocity: The speed and frequency of data generation and processing by IoT devices can be high and variable, requiring real-time or near-real-time visualization methods.
  - Data variety: The diversity and heterogeneity of data sources and formats in IoT systems can be complex and diverse, requiring standardized and interoperable representation and visualization methods.
  - Data veracity: The uncertainty and ambiguity of data quality and reliability in IoT systems can be low and unpredictable, requiring robust and trustworthy representation and visualization methods.
  - Data value: The potential and usefulness of data insights and outcomes in IoT systems can be high and impactful, requiring meaningful and actionable representation and visualization methods.



### Interaction and Remote Control for the Notes of the Unit 2 - Reference Architecture in the Subject of IoT Architecture and Protocols

- Interaction and remote control are two important aspects of IoT systems that enable communication and coordination among devices, applications, and users.
- Interaction refers to the exchange of information and commands between different entities in an IoT system, such as sensors, actuators, gateways, cloud services, and user interfaces.
- Remote control refers to the ability to monitor and manipulate the state and behavior of devices and applications in an IoT system from a distance, such as turning on/off a light, adjusting the temperature, or sending an alert.
- A reference architecture is a generic blueprint that defines the structure, components, interfaces, and interactions of an IoT system, and provides guidance and best practices for designing and implementing specific IoT solutions.
- A reference architecture can help to address the challenges and requirements of IoT systems, such as scalability, interoperability, security, reliability, and performance.
- A reference architecture can also facilitate the reuse and integration of existing IoT technologies, standards, and platforms, and enable the innovation and evolution of new IoT solutions.
- There are different reference architectures proposed by various organizations and initiatives for IoT systems, such as the IoT-A project, the IEEE P2413 standard, the ISO/IEC 30141 standard, the IBM Cloud architecture, and the Azure IoT architecture.
- These reference architectures share some common elements and layers, such as the device layer, the communication layer, the semantic layer, the service layer, and the application layer, but they may differ in the details and specifications of each layer and component.
- The device layer consists of the physical and virtual devices that generate, process, and consume data in an IoT system, such as sensors, actuators, cameras, smartphones, and wearables.
- The communication layer provides the protocols and mechanisms for data transmission and exchange among devices and other entities in an IoT system, such as MQTT, CoAP, HTTP, Bluetooth, Wi-Fi, and cellular networks.
- The semantic layer defines the data models and formats for representing and interpreting the information and commands in an IoT system, such as JSON, XML, RDF, and ontologies.
- The service layer offers the functionalities and capabilities for processing, analyzing, and storing the data and commands in an IoT system, such as cloud computing, edge computing, data analytics, and machine learning.
- The application layer implements the business logic and user interfaces for delivering the value and benefits of an IoT system to the end users, such as web applications, mobile applications, dashboards, and notifications.



## Unit 3 - IOT Data Link Layer & Network Layer Protocols

- The data link layer provides service to the network layer by enabling reliable and efficient communication between devices on the same network segment.
- The network layer provides service to the transport layer by enabling routing and addressing of data packets across different networks or subnets.
- Some of the common data link layer protocols for IoT are:
  - Bluetooth: A short-range wireless communication network over a radio frequency. It supports low-power and low-cost devices and enables peer-to-peer and mesh networking. It is suitable for personal area networks (PANs) and smart home applications. 
  - Wi-Fi: A medium-range wireless communication network over a radio frequency. It supports high-speed and high-bandwidth data transmission and enables access point and station modes. It is suitable for local area networks (LANs) and internet access. 
  - Zigbee: A low-power and low-data-rate wireless communication network over a radio frequency. It supports mesh, star, and tree topologies and enables self-organizing and self-healing networks. It is suitable for industrial, commercial, and residential applications. 
  - NFC: A very short-range wireless communication network over a radio frequency. It supports passive and active modes and enables secure and contactless data exchange. It is suitable for payment, identification, and authentication applications. 
  - Ethernet: A wired communication network over a twisted pair or optical fiber cable. It supports high-speed and high-reliability data transmission and enables point-to-point and broadcast modes. It is suitable for LANs and backbone networks. 
- Some of the common network layer protocols for IoT are:
  - IPv4: A widely used network layer protocol that assigns 32-bit addresses to devices and supports unicast, multicast, and broadcast communication. It has a limited address space and does not support end-to-end security or mobility. 
  - IPv6: A newer network layer protocol that assigns 128-bit addresses to devices and supports unicast, multicast, and anycast communication. It has a large address space and supports end-to-end security and mobility. It is compatible with IPv4 through various transition mechanisms. 
  - 6LoWPAN: A network layer protocol that enables IPv6 communication over low-power and low-bandwidth wireless networks such as Zigbee. It compresses and fragments IPv6 packets to fit the constraints of the underlying network. It supports mesh-under and route-over modes. 
  - RPL: A routing protocol for low-power and lossy networks (LLNs) such as 6LoWPAN. It builds a directed acyclic graph (DAG) based on various metrics and constraints and enables multipath and loop-free routing. It supports storing and non-storing modes.



### PHY/MAC Layer(3GPP MTC

- 3GPP MTC stands for 3rd Generation Partnership Project Machine Type Communication, which is a term used to describe various applications that involve communication between machines or devices without human intervention.
- 3GPP MTC can be categorized into two major challenges: massive MTC and critical MTC, depending on the requirements of latency, reliability, scalability, and complexity.
- 3GPP MTC can be supported by different radio access technologies, such as GSM, UMTS, LTE, and NR (New Radio), which have different physical and MAC layer specifications and procedures  .
- The physical layer (PHY) is responsible for modulation, coding, multiplexing, and transmission of data over the radio channel, as well as channel estimation, demodulation, decoding, and demultiplexing of the received data.
- The medium access control (MAC) layer is responsible for scheduling, resource allocation, error control, and flow control of data over the physical layer, as well as multiplexing and demultiplexing of data from different logical channels.
- The PHY and MAC layers of 3GPP MTC have been designed and optimized to meet the specific needs and challenges of MTC applications, such as low power consumption, low complexity, low cost, high scalability, high reliability, and low latency  .
- Some of the key features and solutions of the PHY and MAC layers of 3GPP MTC are:

  - Small data transmission (SDT): a mechanism to enable efficient and reliable transmission of infrequent and small size data packets, such as sensor readings, smart meter readings, or wearable device data.
  - Narrowband IoT (NB-IoT): a radio access technology that operates in a narrow bandwidth of 180 kHz, and provides enhanced coverage, low power consumption, and low complexity for MTC devices.
  - Grant-free access: a scheme that allows MTC devices to transmit data without waiting for a grant or an allocation from the network, which reduces the signaling overhead and the latency.
  - Non-orthogonal multiple access (NOMA): a technique that allows multiple MTC devices to share the same time-frequency resources, which increases the spectral efficiency and the scalability.
  - Multi-connectivity: a feature that enables MTC devices to connect to multiple base stations or access points simultaneously, which improves the reliability and the diversity of the communication.



### IEEE 802.11

- IEEE 802.11 is a set of standards for wireless local area networks (WLANs) developed by the IEEE 802.11 Working Group  .
- IEEE 802.11 is used in most home and office networks to allow laptops, printers, smartphones, and other devices to communicate with each other and access the Internet without connecting wires.
- IEEE 802.11 is also a basis for vehicle-based communication networks with IEEE 802.11p.
- IEEE 802.11 defines the physical layer (PHY) and the medium access control (MAC) layer specifications for WLANs.
- The PHY layer specifies the modulation, coding, and frequency bands used for wireless transmission.
- The MAC layer specifies the rules for accessing the shared wireless medium, such as carrier sense multiple access with collision avoidance (CSMA/CA), and the frame formats and control messages used for data exchange.
- IEEE 802.11 has several amendments that extend or modify the original standard, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax .
- These amendments differ in the data rates, frequency bands, modulation schemes, and channel widths they support .
- For example, IEEE 802.11a supports up to 54 Mbps data rate in the 5 GHz band and uses orthogonal frequency-division multiplexing (OFDM) modulation.
- IEEE 802.11b supports up to 11 Mbps data rate in the 2.4 GHz band and uses direct-sequence spread spectrum (DSSS) modulation.
- IEEE 802.11g supports up to 54 Mbps data rate in the 2.4 GHz band and uses OFDM modulation.
- IEEE 802.11n supports up to 600 Mbps data rate in the 2.4 GHz or 5 GHz band and uses multiple-input multiple-output (MIMO) technology and channel bonding.
- IEEE 802.11ac supports up to 6.9 Gbps data rate in the 5 GHz band and uses MIMO technology, channel bonding, and higher-order modulation.
- IEEE 802.11ax supports up to 9.6 Gbps data rate in the 2.4 GHz or 5 GHz band and uses MIMO technology, channel bonding, higher-order modulation, and orthogonal frequency-division multiple access (OFDMA) technique.
- IEEE 802.11ad is an amendment that defines a new physical layer for 802.11 networks to operate in the 60 GHz millimeter wave spectrum. This frequency band has significantly different propagation characteristics than the 2.4 GHz and 5 GHz bands where Wi-Fi networks operate.
- IEEE 802.11ad supports up to 7 Gbps data rate and uses directional antennas and beamforming technology.
- IEEE 802.11p is an amendment that defines a new physical layer and MAC layer for 802.11 networks to support wireless access in vehicular environments (WAVE). This amendment enables vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communication using the 5.9 GHz band.
- IEEE 802.11p supports up to 27 Mbps data rate and uses OFDM modulation and enhanced distributed channel access (EDCA) mechanism.
- IEEE 802.11-2020 is the latest revision of the IEEE 802.11 standard that incorporates all the previous amendments and some new features, such as enhanced security, improved power saving, and support for mesh networks.



### IEEE 802.15

- IEEE 802.15 is a working group of the Institute of Electrical and Electronics Engineers (IEEE) IEEE 802 standards committee which specifies Wireless Specialty Networks (WSN) standards .
- The working group was formerly known as Working Group for Wireless Personal Area Networks (WPANs) .
- The working group develops standards for low-data-rate, low-power, and low-cost wireless communications among devices .
- The working group has several task groups (TGs) that focus on different aspects of WSNs, such as physical layer (PHY), medium access control (MAC), security, mesh networking, coexistence, and applications .
- Some of the standards developed by the working group are:
  - IEEE 802.15.1: Bluetooth, a short-range wireless technology for personal area networks (PANs) .
  - IEEE 802.15.4: Low-Rate Wireless Networks (LR-WPANs), a standard for low-data-rate, low-power, and low-cost wireless connectivity with fixed, portable, and moving devices  .
  - IEEE 802.15.4a: an amendment to IEEE 802.15.4 specifying additional physical layers (PHYs) to the original standard, such as ultra-wideband (UWB) and chirp spread spectrum (CSS) .
  - IEEE 802.15.4e: an amendment to IEEE 802.15.4 specifying enhancements to the MAC sublayer, such as time-slotted channel hopping (TSCH), low-latency deterministic network (LLDN), and deterministic and synchronous multi-channel extension (DSME) .
  - IEEE 802.15.4f: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for active radio frequency identification (RFID) systems .
  - IEEE 802.15.4g: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for smart utility networks (SUNs) .
  - IEEE 802.15.4k: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for low-energy critical infrastructure monitoring (LECIM) networks .
  - IEEE 802.15.4n: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for medical body area networks (MBANs) .
  - IEEE 802.15.4p: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for rail communication and control (RCC) networks .
  - IEEE 802.15.4q: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for wireless access in vehicular environments (WAVE) networks .
  - IEEE 802.15.4r: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for high-density impulse radio (HD-IR) networks .
  - IEEE 802.15.4s: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for low-data-rate wireless smart metering utility networks (LDR-WiSUNs) .
  - IEEE 802.15.4t: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for point-to-point wireless bridging for personal area networks (PANs) .
  - IEEE 802.15.4u: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for long-range low-data-rate wireless smart metering utility networks (LR-WiSUNs) .
  - IEEE 802.15.4v: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for low-energy deterministic networks (LEDNs) .
  - IEEE



### WirelessHART

- WirelessHART is a wireless communications protocol for process automation applications.
- It is based on the HART industrial instrument communication standard as of version 7 .
- It communicates process data over 2.4 GHz radio waves using mesh networking technology .
- It maintains compatibility with existing HART devices, commands, and tools.
- It is designed for robustness and security, using 10 ms time slots, channel hopping, encryption, and authentication.
- It uses a common gateway device as an interface between the wireless network and a wired network or a host control system .
- It supports up to 250 devices per network and has a typical range of 200 meters.
- It is a multi-vendor, interoperable wireless standard, developed by the FieldComm Group .



### ZWave

- ZWave is a **wireless mesh network communication protocol** that operates in the **800 to 900 MHz frequency band**  .
- ZWave was developed by **Zensys**, a Danish company, in **1999** as a proprietary system on a chip (SoC) home automation protocol.
- ZWave is widely used in **IoT (Internet of Things)** due to its **low power** and **low data rate** features.
- ZWave supports **encryption** and **security layer** to protect the communication between smart devices .
- ZWave can support up to **232 devices** in a single network, and each device can act as a **repeater** to extend the range of the network .
- ZWave devices are **interoperable** and **backward compatible** with each other, regardless of the manufacturer or model .
- ZWave devices can be controlled by a **central controller** or a **smartphone app** via the **ZWave gateway** .
- ZWave devices can be categorized into **controllers**, **sensors**, **actuators**, and **bridges**.
- ZWave devices use a **source routing algorithm** to find the optimal path to the destination device.
- ZWave devices can form **logical groups** or **scenes** to enable simultaneous control of multiple devices.



### Bluetooth Low Energy

- Bluetooth Low Energy (BLE) is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group (Bluetooth SIG) aimed at novel applications in the healthcare, fitness, beacons, security, and home entertainment industries.
- BLE is distinct from the previous (often called "classic") Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR) protocol, but the two protocols can both be supported by one device: the Bluetooth 4.0 specification permits devices to implement either or both of the LE and BR/EDR systems.
- BLE has the following advantages over classic Bluetooth:
  - Lower power consumption: BLE devices can operate for months or years on a coin cell battery, while classic Bluetooth devices require frequent recharging.
  - Faster connection time: BLE devices can connect in a few milliseconds, while classic Bluetooth devices may take seconds.
  - Simpler pairing process: BLE devices can use a variety of methods to pair, such as scanning a QR code, tapping a NFC tag, or proximity detection, while classic Bluetooth devices require a PIN code or a confirmation button.
  - Higher scalability: BLE devices can support up to 20 concurrent connections, while classic Bluetooth devices are limited to 7.
- BLE uses two protocols for discovery and communication between devices: the Generic Access Profile (GAP) and the Generic Attribute Profile (GATT).
  - GAP defines how devices advertise themselves and discover other devices. GAP also defines the roles of devices, such as peripheral (device that advertises and provides data) and central (device that scans and consumes data).
  - GATT defines how devices exchange data using services, characteristics, and descriptors. GATT also defines the roles of devices, such as server (device that provides data) and client (device that requests data).
- BLE devices can operate in different modes, such as broadcast, connection, or mesh.
  - Broadcast mode: A device sends data to all nearby devices without establishing a connection. This mode is useful for applications such as beacons, which provide location or contextual information to nearby devices.
  - Connection mode: A device establishes a connection with another device and exchanges data using GATT. This mode is useful for applications such as fitness trackers, which provide biometric data to a smartphone or a smartwatch.
  - Mesh mode: A device connects with multiple devices and relays data between them. This mode is useful for applications such as smart home, which allow devices to communicate with each other and with a gateway device.



### Zigbee Smart Energy

- Zigbee Smart Energy (Zigbee SE) is a protocol designed for monitoring and actively managing energy consumption at the end-user level.
- Zigbee SE can help reduce waste, energy consumption and enables utilities to monitor and manage customers’ energy use.
- Zigbee SE is based on the Zigbee protocol, which is a low-cost and low-power wireless communication standard for IoT devices.
- Zigbee SE supports both 2.4 GHz and sub-GHz frequency bands, which provide global and regional coverage respectively.
- Zigbee SE defines an Internet Protocol-based communication protocol to monitor, control, inform, and automate the delivery and use of energy and water.
- Zigbee SE is aimed at coordinating energy usage, optimizing its generation and consumption, and creating “Green Homes”.
- Zigbee SE enables interoperability among different devices and applications, such as smart meters, thermostats, appliances, lighting, solar panels, etc.
- Zigbee SE is a certified and standardized technology that ensures security, reliability, and scalability of the smart energy network.



### DASH7

- DASH7 is an open-source wireless sensor and actuator network protocol, which operates in the 433 MHz, 868 MHz and 915 MHz unlicensed ISM band /SRD band.
- DASH7 is based on the ISO 18000-7 standard for active radio frequency identification (RFID) and supports bi-directional, low-power, low-latency communication with long range and high penetration .
- DASH7 is designed for applications that require mobility, security, low cost, and low power consumption, such as asset tracking, building automation, smart metering, and environmental monitoring.
- DASH7 uses a four-layer architecture, consisting of the physical layer, the data link layer, the network layer, and the application layer.
- The physical layer defines the modulation, coding, and framing schemes for the radio communication. DASH7 supports four modulation schemes: FSK, GFSK, ASK, and OOK, with data rates ranging from 1.2 kbps to 200 kbps.
- The data link layer defines the medium access control (MAC) protocol, which is based on a slotted ALOHA scheme with optional acknowledgments and retransmissions. The MAC protocol also supports multi-hop communication, channel hopping, and encryption.
- The network layer defines the addressing scheme, the routing protocol, and the network management functions. DASH7 uses a 16-bit network address and a 64-bit unique identifier for each device. The routing protocol is based on a flooding mechanism with optional filters and masks. The network management functions include network discovery, network joining, and network maintenance.
- The application layer defines the application interface and the application commands. DASH7 provides a common application interface (CAI) that allows interoperability among different devices and applications. The CAI defines a set of commands for device identification, device configuration, data transmission, and data reception.
- DASH7 has several advantages over other wireless sensor network protocols, such as Zigbee, Bluetooth, and Wi-Fi. Some of these advantages are :

  - Longer range: DASH7 can achieve a range of up to 2 km in line-of-sight and up to 500 m in non-line-of-sight conditions, depending on the antenna and the environment.
  - Higher penetration: DASH7 can penetrate through walls, metal, and water, which makes it suitable for indoor and outdoor applications.
  - Lower power consumption: DASH7 devices can operate on batteries for several years, thanks to the low duty cycle and the low data rate of the protocol.
  - Higher security: DASH7 supports AES-128 encryption and authentication, as well as frequency hopping and spread spectrum techniques, to prevent eavesdropping and jamming attacks.
  - Higher scalability: DASH7 can support up to 16 million devices per network, thanks to the large address space and the efficient routing protocol.
  - Higher mobility: DASH7 can handle fast-moving devices and dynamic network topologies, thanks to the low-latency and the adaptive channel hopping of the protocol.

- DASH7 has several applications in various domains, such as  :

  - Asset tracking: DASH7 can be used to track and locate assets, such as vehicles, containers, luggage, and equipment, in real time and with high accuracy.
  - Building automation: DASH7 can be used to monitor and control building systems, such as lighting, heating, ventilation, and security, as well as to detect occupancy, fire, and intrusion.
  - Smart metering: DASH7 can be used to read and transmit meter data, such as electricity, gas, water, and heat, from smart meters to utility companies, as well as to enable demand response and load management.
  - Environmental monitoring: DASH7 can be used to measure and report environmental parameters, such as temperature, humidity, pressure, and air quality, from sensors deployed in various locations, such as farms, forests, and cities.
  - Tire pressure monitoring system (TPMS): DASH7 can be used to provide more accurate tire pressure readings, resulting in greater fuel economy, reduced tire wear, and greater safety. DASH7 products are also being designed and used for other automotive applications like supply chain visibility.



### Network Layer

- The network layer is part of the infrastructure layer in the IoT reference architecture  .
- The network layer is responsible for addressing and routing of data packets .
- The network layer includes protocols and technologies that enable devices to connect and communicate with each other and with the wider internet .
- The network layer can be divided into two sub-layers: the routing layer and the encapsulation layer.
- The routing layer sends packets from origin to destination using different routing protocols, such as RPL, AODV, OLSR, etc.
- The encapsulation layer is responsible for creating packets by adding headers and trailers to the datagrams from the transport layer .
- The encapsulation layer uses different addressing schemes, such as IPv4, IPv6, 6LoWPAN, etc .
- The network layer also performs functions such as fragmentation, reassembly, compression, and decompression of packets .
- The network layer faces challenges such as limited resources, heterogeneity, scalability, mobility, security, and privacy in the IoT context  .



### IPv4

- IPv4 stands for Internet Protocol version 4, which is the fourth version in the development of the Internet Protocol (IP) and the first version of the protocol to be widely deployed.
- IPv4 is a connectionless protocol that operates on the network layer of the OSI model and the internet layer of the TCP/IP model.
- IPv4 uses 32-bit binary numbers to create a single unique address on the network, which can be represented by four decimal numbers separated by dots, also called dotted decimal notation.
- For example, an IPv4 address can be written as 192.168.0.1, where each number is between 0 and 255.
- IPv4 addresses are divided into two parts: network ID and host ID, which identify the network and the device within the network respectively.
- IPv4 addresses are also classified into five classes: A, B, C, D, and E, based on the first four bits of the address and the size of the network and host ID.
- Class A addresses have the first bit as 0, and can support up to 126 networks and 16,777,214 hosts per network.
- Class B addresses have the first two bits as 10, and can support up to 16,384 networks and 65,534 hosts per network.
- Class C addresses have the first three bits as 110, and can support up to 2,097,152 networks and 254 hosts per network.
- Class D addresses have the first four bits as 1110, and are reserved for multicast purposes.
- Class E addresses have the first four bits as 1111, and are reserved for experimental purposes.
- IPv4 supports various types of addresses, such as unicast, broadcast, multicast, anycast, and geocast, which are used for different purposes and scenarios.
- Unicast addresses are used to identify a single device on the network and deliver packets to that device only.
- Broadcast addresses are used to identify all devices on the network and deliver packets to all of them simultaneously.
- Multicast addresses are used to identify a group of devices on the network and deliver packets to only those devices that belong to the group.
- Anycast addresses are used to identify multiple devices on the network that provide the same service and deliver packets to the nearest or best device among them.
- Geocast addresses are used to identify a geographical area on the network and deliver packets to all devices within that area.
- IPv4 has a header of 20 bytes, which contains 12 fields that provide various information about the packet, such as source and destination addresses, version, length, type of service, identification, flags, fragment offset, time to live, protocol, header checksum, and options.
- IPv4 has some limitations, such as the exhaustion of address space, lack of security, and fragmentation issues, which led to the development of IPv6, the next generation of IP.



### IPv6

IPv6 is the next generation Internet Protocol (IP) standard intended to eventually replace IPv4, the protocol many Internet services still use today. IPv6 is designed to solve many of the problems of IPv4, such as address depletion, security, auto-configuration, extensibility, and so on. IPv6 expands the capabilities of the Internet to enable new kinds of applications, including peer-to-peer and mobile applications.

Some of the important features and uses of IPv6 are:

- IPv6 addresses: An IPv6 address uses 128 bits, four times more than the IPv4 address, which uses only 32 bits. This allows for a much larger address space, which can accommodate more devices and networks on the Internet. IPv6 addresses are written using hexadecimal, as opposed to dotted decimal in IPv4. For example, an IPv6 address may look like this: 2001:db8:0:1234:0:567:8:1.
- Network and node addresses: In IPv4, address classes were used to split an address into two components: a network component and a node component. In IPv6, the address is divided into two parts: a 64-bit network prefix and a 64-bit interface identifier. The network prefix identifies the network or subnet to which the device belongs, and the interface identifier identifies the device or interface on that network. The interface identifier can be derived from the MAC address of the device, or randomly generated for privacy reasons.
- IPv6 address types and scope: IPv6 defines different types of addresses for different purposes and scopes. Some of the common address types are:

  - Link-local: These are addresses that are valid only on the local link or subnet. They are used for communication between devices on the same link, such as neighbor discovery, router advertisement, and address resolution. They start with the prefix fe80::/10.
  - Global unicast: These are addresses that are globally unique and routable on the Internet. They are used for communication between devices on different networks. They start with any prefix other than fe80::/10, fc00::/7, or ff00::/8.
  - Unique local: These are addresses that are locally unique and routable within a site or a group of sites. They are used for communication between devices that do not need global connectivity, such as private networks. They start with the prefix fc00::/7.
  - Multicast: These are addresses that are used to send packets to multiple destinations at once. They are used for group communication, such as video streaming, conferencing, and service discovery. They start with the prefix ff00::/8.
  - Anycast: These are addresses that are assigned to multiple devices that provide the same service. They are used to send packets to the nearest or best device among the group, such as load balancing, redundancy, and mobility. They can use any of the above address types, except multicast.

- Using IPv6 addresses in uniform resource locators (URLs): IPv6 addresses can be used in URLs to access web resources, such as websites, files, and services. However, since IPv6 addresses contain colons, which are also used to separate the protocol and port number in URLs, they need to be enclosed in square brackets to avoid confusion. For example, a URL with an IPv6 address may look like this: http://[2001:db8:0:1234:0:567:8:1]:80/index.html.
- IPv6 loopback: The loopback address is a special address that is used to test the connectivity and functionality of the local device. It is used to send packets to itself, without involving any external network. In IPv4, the loopback address is 127.0.0.1. In IPv6, the loopback address is ::1. For example, a ping command to the loopback address may look like this: ping ::1.



### 6LoWPAN

- 6LoWPAN stands for IPv6 over Low-power Wireless Personal Area Networks.
- It is an open standard defined by the Internet Engineering Task Force (IETF) that enables low-power devices with limited processing capabilities to participate in the Internet of Things (IoT) by using IPv6 over IEEE 802.15.4 based networks .
- 6LoWPAN defines mechanisms for:
  - Encapsulation: how to fragment and reassemble IPv6 datagrams over the IEEE 802.15.4 frame size limit of 127 bytes.
  - Header compression: how to reduce the size of IPv6 and UDP headers to fit in the IEEE 802.15.4 frame payload.
  - Neighbor discovery: how to discover and register IPv6 addresses and prefixes of other nodes in the network.
  - Routing: how to forward IPv6 datagrams over multiple hops using different routing protocols, such as RPL (Routing Protocol for Low-Power and Lossy Networks).
- 6LoWPAN networks can be connected to other IPv6 networks, such as the Internet, through edge routers that support IPv6 transition mechanisms, such as NAT64, which allows IPv6 nodes to communicate with IPv4 nodes.
- 6LoWPAN networks can support various applications that require wireless internet connectivity at lower data rates, such as residential and office automation, smart grid, industrial monitoring, etc.



### 6TiSCH

- 6TiSCH stands for IPv6 over the Time Slotted Channel Hopping (TSCH) mode of IEEE 802.15.4e.
- It is a protocol stack that combines the industrial performance of TSCH with the seamless integration of IPv6 for the Industrial Internet of Things (IIoT).
- TSCH is a link layer protocol that provides reliable and energy-efficient communication by using time synchronization and frequency diversity.
- 6TiSCH defines how to use IPv6 addressing, header compression, encapsulation, and routing over TSCH networks.
- 6TiSCH also defines the 6TiSCH Operation Sublayer (6top), which is an interface between the network layer and the link layer that allows dynamic scheduling of TSCH timeslots.
- 6top uses the 6top Protocol (6P), which is a distributed protocol that enables nodes to negotiate and manage their TSCH schedules.
- 6TiSCH enables the convergence of Operational Technology (OT) and Information Technology (IT) by allowing interoperability and scalability of IIoT applications.



### ND for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The data link layer provides service to the network layer by enabling reliable and efficient communication between devices on the same network segment.
- The network layer provides service to the transport layer by enabling routing and addressing of data packets across different networks.
- Some of the common data link layer protocols in IoT are:
  - Bluetooth: A short-range wireless communication network over a radio frequency. It supports low-power and low-cost devices and enables peer-to-peer and mesh networking.
  - Wi-Fi: A wireless LAN technology that uses radio waves to provide high-speed internet access. It supports various standards such as 802.11a/b/g/n/ac/ax and enables infrastructure and ad-hoc modes.
  - Zigbee: A low-rate wireless personal area network (WPAN) that uses the IEEE 802.15.4 standard. It supports low-power and low-cost devices and enables star, tree and mesh topologies.
  - NFC: A short-range wireless communication technology that enables data exchange between devices by bringing them close together. It supports passive and active modes and enables peer-to-peer and card emulation applications.
- Some of the common network layer protocols in IoT are:
  - IPv4: The fourth version of the internet protocol that uses 32-bit addresses to identify devices on the internet. It supports various features such as fragmentation, checksum, and options.
  - IPv6: The sixth version of the internet protocol that uses 128-bit addresses to identify devices on the internet. It supports various features such as auto-configuration, security, and mobility.
  - 6LoWPAN: A protocol that enables IPv6 packets to be transmitted over low-power and lossy networks (LLNs) such as IEEE 802.15.4. It supports various features such as header compression, fragmentation, and adaptation.
  - CoAP: A protocol that enables constrained devices to communicate with web services using a RESTful architecture. It supports various features such as caching, observe, and multicast.



### DHCP

- DHCP stands for Dynamic Host Configuration Protocol   .
- It is a network management protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway .
- It uses a client-server architecture, where a DHCP server allocates IP addresses and other parameters to DHCP clients that request them   .
- It is based on the Bootstrap Protocol (BOOTP), which was designed for diskless workstations .
- It is defined by RFCs 2131 and 2132, and supports both IPv4 and IPv6 .
- It operates on four basic steps: discover, offer, request, and acknowledge   .
  - Discover: The DHCP client broadcasts a DHCPDISCOVER message to find a DHCP server on the network   .
  - Offer: The DHCP server responds with a DHCPOFFER message, containing an IP address and other configuration options for the client   .
  - Request: The DHCP client selects one of the offers and sends a DHCPREQUEST message to the chosen server, requesting the IP address and other parameters   .
  - Acknowledge: The DHCP server confirms the allocation with a DHCPACK message, or rejects it with a DHCPNAK message   .
- It allows for dynamic and efficient management of IP addresses and network configuration, reducing manual intervention and errors   .
- It also supports features such as lease time, renewal, release, and rebinding of IP addresses, as well as static and dynamic allocation of IP addresses   .
- It is widely used in various types of networks, such as LANs, WANs, WLANs, and IoT networks   .



### ICMP

- ICMP stands for Internet Control Message Protocol  .
- It is a network layer protocol used by network devices to diagnose network communication issues  .
- It is not associated with any transport layer protocol, such as TCP or UDP .
- It is a connectionless protocol, meaning a device does not need to open a connection with the target device before sending a message.
- It is used to generate error messages to the source IP address when network problems prevent delivery of IP packets .
- It is also used to determine whether or not data is reaching its intended destination in a timely manner .
- It is also used for inter-device communication, carrying everything from redirect instructions to timestamps for synchronization between devices.
- Some common types of ICMP messages are:
  - Echo request and echo reply: used to test the reachability and latency of a destination device   .
  - Destination unreachable: used to inform the source device that the destination device or network is unreachable   .
  - Time exceeded: used to inform the source device that the time to live (TTL) of a packet has expired   .
  - Parameter problem: used to inform the source device that there is a problem with the header of a packet   .
  - Source quench: used to inform the source device that the destination device is congested and cannot process more packets   .
  - Redirect: used to inform the source device that there is a better route to the destination device or network   .
- ICMP is important for IOT because it helps to monitor and troubleshoot the connectivity and performance of IOT devices and networks   .
- ICMP can also be used for malicious purposes, such as denial-of-service (DoS) attacks, ping flooding, ping of death, and ICMP tunneling   .
- ICMP can be blocked or filtered by firewalls or routers to prevent unwanted or harmful traffic   .



### RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The network layer is responsible for routing packets from source to destination in an IoT network.
- The network layer is divided into two sublayers: routing layer and encapsulation layer.
- The routing layer handles the transfer of packets from source to destination, while the encapsulation layer forms the packets.
- RPL stands for Routing Protocol for Low-Power and Lossy Networks. It is a routing protocol designed for IoT networks that are resource-constrained, dynamic, and unreliable.
- RPL constructs a tree-like topology for the data transmission, where each node has a rank that indicates its position in the tree.
- RPL uses two types of messages: control messages and data messages.
- Control messages are used to build and maintain the topology, while data messages are used to carry the application data.
- Control messages include DIO (DODAG Information Object), DAO (Destination Advertisement Object), DIS (DODAG Information Solicitation), and DAO-ACK (DAO Acknowledgment).
- DIO messages are used to advertise the rank and other information of a node to its neighbors.
- DAO messages are used to inform the parent node about the destination nodes that are reachable through the sender node.
- DIS messages are used to request DIO messages from the neighbors.
- DAO-ACK messages are used to acknowledge the receipt of DAO messages.
- Data messages include ICMPv6 (Internet Control Message Protocol version 6) and UDP (User Datagram Protocol) packets.
- ICMPv6 packets are used to perform diagnostic functions, such as ping and traceroute.
- UDP packets are used to carry the application data, such as sensor readings or actuator commands.
- RPL supports two modes of operation: storing mode and non-storing mode.
- In storing mode, each node maintains a routing table that contains the next hop information for all the destinations in the network.
- In non-storing mode, each node only maintains the next hop information for its parent node, and the source node includes the entire path information in the data packet.



### CORPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- CORPL stands for **C**ontrol **O**bjective **R**outing **P**rotocol for **L**ow power and lossy networks.
- It is a network layer protocol designed for IoT applications that require reliable and efficient data delivery in constrained environments.
- It is based on the concept of **control objectives**, which are high-level goals that the network should achieve, such as minimizing delay, maximizing throughput, or balancing energy consumption.
- CORPL uses a distributed algorithm to compute optimal routes based on the control objectives and the network state, such as link quality, traffic load, and node resources.
- CORPL is compatible with the IPv6 Routing Protocol for Low-Power and Lossy Networks (RPL), which is the standard routing protocol for IoT networks.
- CORPL can coexist with other RPL instances that use different control objectives or metrics, and can dynamically switch between them based on the application requirements.
- CORPL has been shown to outperform RPL in terms of packet delivery ratio, end-to-end delay, and energy efficiency in various scenarios, such as smart grid, smart city, and industrial IoT .

Some key points about the IoT data link layer and network layer protocols are:

- The data link layer is responsible for providing reliable and efficient data transmission between adjacent nodes in the network, such as sensors, actuators, gateways, and routers.
- The data link layer consists of protocols like Bluetooth, ZigBee, Wi-Fi, Ethernet, and mobile communication such as 5G, 4G, and 3G .
- The data link layer uses the physical and medium access control (MAC) sublayers to handle the physical characteristics and the access methods of the communication medium, such as radio frequency, infrared, or optical.
- The network layer is responsible for providing end-to-end data delivery across multiple hops in the network, such as from a sensor to a cloud server or from an actuator to a controller.
- The network layer consists of protocols like RPL, CORPL, CARP, and 6LoWPAN .
- The network layer uses the routing and encapsulation sublayers to handle the path selection and the packet formation of the data, such as using IPv6 addresses, headers, and compression techniques.



### CARP

- CARP stands for Channel-Aware Routing Protocol.
- It is a distributed routing protocol designed for underwater communication .
- It has lightweight packets so that it can be used for Internet of Things (IoT) .
- It performs two different functionalities: network initialization and data forwarding.
- CARP protocol does not support previously collected data.
- The protocol keeps track of data communication history to select nodes for data transfer.
- The protocol is adaptive to the dynamic channel conditions and node mobility.
- The protocol aims to minimize the end-to-end delay and maximize the packet delivery ratio.



## Unit 4 - Transport & Session Layer Protocols

- The transport layer is the fourth layer of the OSI model. It is responsible for providing reliable and efficient data transfer between applications on different hosts in a network.
- The transport layer protocols can be classified into two types: connection-oriented and connectionless. Connection-oriented protocols establish a virtual circuit between the sender and the receiver before exchanging data, while connectionless protocols send data without any prior arrangement.
- The most common transport layer protocols are TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). TCP is a connection-oriented protocol that provides reliable, ordered, and error-free data delivery. UDP is a connectionless protocol that provides fast and simple data delivery, but does not guarantee reliability, order, or error detection.
- Some other transport layer protocols that have been defined and implemented include DCCP (Datagram Congestion Control Protocol) and SCTP (Stream Control Transmission Protocol). DCCP is a connectionless protocol that provides congestion control for unreliable datagrams. SCTP is a connection-oriented protocol that supports multiple streams of data within a single connection.
- The session layer is the fifth layer of the OSI model. It is responsible for managing and coordinating the communication sessions between applications on different hosts in a network.
- The session layer protocols can provide various functions, such as authentication, authorization, encryption, synchronization, checkpointing, and dialog control. These functions enable applications to establish, maintain, and terminate sessions, and to recover from failures or interruptions.
- The session layer protocols are usually implemented by the application layer protocols, or otherwise considered the realm of the transport layer protocols. Some examples of session layer protocols are RPC (Remote Procedure Call), NFS (Network File System), SQL (Structured Query Language), and SIP (Session Initiation Protocol).



### Transport Layer

The transport layer is the fourth layer of the OSI model and the TCP/IP model. It is responsible for end-to-end communication between devices in an IoT system. It provides features such as reliability, congestion avoidance, ordering, and error detection and correction. It also enables multiplexing and demultiplexing of data streams from different applications.

Some of the main functions of the transport layer are:

- **Segmentation and reassembly**: The transport layer divides the data from the application layer into smaller units called segments, which are easier to transmit over the network. Each segment has a header that contains information such as source and destination port numbers, sequence numbers, and checksums. The transport layer at the receiver end reassembles the segments into the original data.
- **Connection-oriented and connectionless communication**: The transport layer can use either connection-oriented or connectionless protocols to communicate with the devices. Connection-oriented protocols, such as TCP, establish a logical connection between the sender and the receiver before exchanging data. They ensure reliable and ordered delivery of data, but they also incur more overhead and latency. Connectionless protocols, such as UDP, do not require a connection setup and teardown. They are faster and more efficient, but they do not guarantee reliability or ordering of data.
- **Flow control and congestion control**: The transport layer regulates the rate of data transmission between the sender and the receiver to avoid overflowing the network or the receiver's buffer. Flow control is achieved by using mechanisms such as sliding window or stop-and-wait. Congestion control is achieved by using algorithms such as additive increase multiplicative decrease (AIMD) or congestion avoidance and control (CAC).
- **Error detection and correction**: The transport layer detects and corrects errors in the data transmission by using techniques such as checksums, acknowledgments, and retransmissions. Checksums are used to verify the integrity of the data segments. Acknowledgments are used to confirm the receipt of the data segments. Retransmissions are used to resend the lost or corrupted data segments.

Some of the common transport layer protocols used in IoT are:

- **TCP (Transmission Control Protocol)**: TCP is a connection-oriented, reliable, and ordered protocol that provides features such as error detection and correction, flow control, and congestion control. TCP is widely used for applications that require high reliability and consistency, such as web browsing, email, and file transfer. However, TCP is not suitable for applications that require low latency, high efficiency, or real-time communication, such as streaming, gaming, or voice over IP (VoIP).
- **UDP (User Datagram Protocol)**: UDP is a connectionless, unreliable, and unordered protocol that provides features such as multiplexing and demultiplexing of data streams. UDP is often adopted for IoT transport for performance reasons. UDP is suitable for applications that can tolerate some loss or delay of data, such as streaming, gaming, or VoIP. However, UDP does not provide any error detection and correction, flow control, or congestion control, which may result in data loss, duplication, or disorder.
- **DCCP (Datagram Congestion Control Protocol)**: DCCP is a connection-oriented, unreliable, and ordered protocol that provides features such as congestion control, multiplexing and demultiplexing of data streams, and error detection. DCCP is designed for applications that require congestion control but not reliability, such as streaming, gaming, or VoIP. DCCP allows the application to choose from different congestion control profiles, such as TCP-like, TCP-friendly, or low-latency.
- **SCTP (Stream Control Transmission Protocol)**: SCTP is a connection-oriented, reliable, and ordered protocol that provides features such as error detection and correction, flow control, congestion control, and multihoming. SCTP is designed for applications that require multiple streams of data within a single connection, such as web browsing, email, or file transfer. SCTP allows the application to assign different priorities and reliability levels to different streams, and to switch between different network paths in case of failure.
- **RSVP (Resource Reservation Protocol)**: RSVP is a connection-oriented, reliable, and ordered protocol that provides features such as quality of service (QoS), resource reservation, and admission control. RSVP is designed for applications that require guaranteed bandwidth, delay, or jitter, such as streaming, gaming, or VoIP. RSVP allows the application to specify the QoS requirements and reserve the network resources along the path from the sender to the receiver.
- **DTLS (Datagram Transport Layer Security)**: DTLS is a connectionless, reliable, and ordered protocol that provides features such



### TCP

- TCP stands for **Transmission Control Protocol**  and is one of the main protocols of the **Internet protocol suite**.
- TCP is a **transport layer protocol**  that enables applications and devices to exchange messages over a network.
- TCP is a **connection-oriented protocol**, which means it establishes and maintains a connection between the endpoints until the data transfer is complete.
- TCP performs the following functions :
  - It divides the application data into **packets** that can be sent over the network.
  - It assigns a **sequence number** to each packet to identify its position in the data stream.
  - It uses a **checksum** to verify the integrity of each packet and detect any errors or corruption.
  - It uses a **three-way handshake** to initiate and terminate a connection between the endpoints.
  - It uses **acknowledgments** to confirm the receipt of packets and request retransmission of lost or damaged packets.
  - It uses **flow control** to regulate the rate of data transmission and avoid congestion or overload of the network.
  - It uses **congestion control** to adjust the window size and retransmission timeout based on the network conditions and feedback from the receiver.
  - It provides **reliability**, **ordered delivery**, and **error recovery** for the data transfer.



### MPTCP

- MPTCP stands for Multipath TCP, which is an extension to the original TCP protocol that allows a transport connection to operate across multiple paths simultaneously .
- MPTCP brings network connection redundancy to user endpoint devices, and improves connection stability, throughput, and resilience compared to single-path TCP  .
- MPTCP works by establishing multiple TCP subflows between the endpoints, each subflow using a different pair of source and destination addresses .
- MPTCP uses a new option in the TCP header to exchange additional information between the endpoints, such as the available addresses, the subflow identifiers, and the data sequence mapping .
- MPTCP is backward compatible with existing TCP applications and network infrastructure, as it falls back to regular TCP when MPTCP is not supported by either endpoint or any intermediate device .
- MPTCP is suitable for scenarios where multiple network interfaces are available, such as mobile devices with Wi-Fi and cellular connections, or data centers with multiple links between servers  .
- MPTCP is supported by Red Hat Enterprise Linux 8.3 and later versions, and can be enabled and configured using the `mptcp` kernel module and the `sysctl` command  .



### UDP

- UDP stands for User Datagram Protocol. It is one of the core communication protocols of the Internet protocol suite used to send messages (transported as datagrams in packets) to other hosts on an Internet Protocol (IP) network.
- UDP is a simple message-oriented transport layer protocol that is documented in RFC 768. It provides integrity verification (via checksum) of the header and payload, but it does not provide any guarantees to the upper layer protocol for message delivery and the UDP layer retains no state of UDP messages once sent .
- UDP is primarily used to establish low-latency and loss-tolerating connections between applications on the internet. UDP speeds up transmissions by enabling the transfer of data before an agreement is provided by the receiving party.
- UDP is a part of the Internet Protocol suite, referred to as UDP/IP suite. Unlike TCP, it is an unreliable and connectionless protocol. So, there is no need to establish a connection prior to data transfer.
- UDP provides a mechanism to detect corrupt data in packets, but it does not attempt to solve other problems that arise with packets, such as lost or out of order packets. UDP is suitable for applications that require speed and efficiency, such as streaming media, online gaming, voice over IP, etc .
- UDP has a header of 8 bytes, consisting of four fields: source port, destination port, length, and checksum. The source and destination ports identify the endpoints of the communication. The length field specifies the total length of the UDP datagram, including the header and the data. The checksum field is used to verify the integrity of the header and the data .
- UDP does not provide any flow control, congestion control, or error recovery mechanisms. These functions are left to the application layer or the upper layer protocols that use UDP as the underlying transport protocol. Some examples of such protocols are RTP, RTCP, DNS, DHCP, SNMP, etc .



### DCCP

- DCCP stands for **Datagram Congestion Control Protocol**.
- It is a **message-oriented** transport layer protocol that provides **unreliable** data delivery .
- It is designed to solve issues present in UDP and TCP, particularly for **real-time** and **multimedia** (streaming) traffic .
- It implements **reliable** connection setup, teardown, **Explicit Congestion Notification (ECN)**, congestion control, and feature negotiation .
- It supports **pluggable** congestion control modules called **CCIDs** (Congestion Control IDentifiers) that can be selected by the application or negotiated by the endpoints .
- It uses a **packet header** that contains a **sequence number**, a **type** field, and a **checksum** field.
- It defines several **packet types** for different purposes, such as **Request**, **Response**, **Data**, **Ack**, **Close**, etc.
- It uses a **three-way handshake** to establish a connection and a **four-way handshake** to close a connection.
- It uses a **feature negotiation** mechanism to allow the endpoints to agree on various options, such as **CCID**, **ECN**, **checksum coverage**, etc.
- It provides a **socket API** for applications to use DCCP as a transport protocol.



### SCTP

- SCTP stands for **Stream Control Transmission Protocol**.
- It is a **transport layer** protocol in the Internet protocol suite.
- It is a **connection-oriented** protocol that supports **multiple streams** of data between two endpoints.
- It ensures **reliable** and **in-sequence** data transmission, so that data units arrive completely and in the right order to the application or user.
- It can **fragment** a message into multiple data chunks, but each data chunk contains data from only one user message.
- It **bundles** the chunks into SCTP packets, each identified by a chunk header.
- It is designed to transport **PSTN** (Public Switched Telephone Network) signaling messages over IP networks, but is capable of broader applications.
- It provides features such as **multihoming**, **congestion control**, **flow control**, **error detection**, **security** and **graceful shutdown**.



### Session Layer for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The session layer is the fifth layer of the OSI model that manages the connection between two endpoints of a network by controlling data between sender and receiver .
- The session layer protocols are responsible for the actual transmission of data in the IoT ecosystem. They are also known as the messaging protocols or the data transmission protocols .
- The session layer protocols review standards and protocols for message passing. Different standardization organizations introduce the IoT session layer protocols. There are different types of session layer protocols available with different functionality and range.
- Some of the common IoT session layer protocols are   :
  - AMQP (Advanced Message Queuing Protocol): A binary, application layer protocol that provides reliable and secure message exchange between applications and devices. It supports publish/subscribe, point-to-point, and request/reply messaging patterns. It is widely used in cloud computing, financial services, and IoT applications.
  - MQTT (Message Queuing Telemetry Transport): A lightweight, publish/subscribe protocol that is designed for constrained devices and low-bandwidth networks. It enables efficient and reliable data transmission between devices and servers. It is widely used in IoT applications such as smart home, smart grid, and industrial automation.
  - HTTP (Hypertext Transfer Protocol): A widely used, application layer protocol that enables communication between clients and servers over the internet. It supports request/response, stateless, and RESTful interactions. It is used for web-based IoT applications that require interoperability and scalability.
  - CoAP (Constrained Application Protocol): A lightweight, RESTful protocol that is designed for constrained devices and networks. It enables resource-oriented communication between devices and servers over UDP. It supports asynchronous message exchange, multicast, and observe mechanisms. It is used for IoT applications that require low power consumption and low latency.
  - DDS (Data Distribution Service): A middleware protocol that provides data-centric, real-time, and reliable communication between applications and devices. It supports publish/subscribe, peer-to-peer, and quality of service mechanisms. It is used for IoT applications that require high performance, scalability, and resilience.
  - LwM2M (Lightweight Machine to Machine): A device management protocol that provides a standard way to manage and monitor IoT devices over CoAP. It supports object-oriented, secure, and bootstrap interactions. It is used for IoT applications that require device management, firmware update, and remote control.



### HTTP

HTTP stands for Hypertext Transfer Protocol. It is an application-layer protocol for transmitting hypermedia documents, such as HTML. It was designed for communication between web browsers and web servers, but it can also be used for other purposes.

Some basic concepts of HTTP are:

- **Resources and URIs**: A resource is any piece of information that can be identified by a Uniform Resource Identifier (URI). A URI is a string that uniquely identifies a resource on the web. For example, `https://example.com/index.html` is a URI that identifies an HTML document on a web server.
- **Messages**: HTTP communication consists of messages that are exchanged between a client and a server. A message has a simple structure: a start-line, zero or more headers, an empty line, and an optional body. The start-line indicates the type of the message: a request or a response. The headers provide additional information about the message, such as the content type, the length, the encoding, etc. The body contains the actual data of the message, such as the HTML document, the image, the JSON data, etc.
- **Methods**: HTTP defines a set of methods that indicate the action to be performed on a resource. The most common methods are: GET, POST, PUT, DELETE, HEAD, OPTIONS, etc. For example, a GET request asks the server to send back the resource identified by the URI, while a POST request sends data to the server to create or update a resource.
- **Status codes**: HTTP defines a set of status codes that indicate the outcome of a request. The status codes are divided into five categories: 1xx (informational), 2xx (success), 3xx (redirection), 4xx (client error), and 5xx (server error). For example, a 200 status code means that the request was successful, while a 404 status code means that the resource was not found.
- **Client-server communication flow**: HTTP is a client-server protocol, which means that requests are sent by one entity, the user-agent (or a proxy on behalf of it), and responses are sent by another entity, the origin server (or a proxy on behalf of it). Most of the time, the user-agent is a web browser, but it can be anything, such as a robot that crawls the web to populate and maintain a search engine index. The communication flow is as follows:

  1. The user-agent initiates a connection to the server using the URI of the resource.
  2. The user-agent sends a request message to the server, specifying the method, the URI, the protocol version, the headers, and the body (if any).
  3. The server receives the request and processes it according to its logic and configuration.
  4. The server sends a response message to the user-agent, specifying the protocol version, the status code, the headers, and the body (if any).
  5. The user-agent receives the response and interprets it according to the status code, the headers, and the body. It may display the resource to the user, follow a redirection, handle an error, etc.
  6. The connection is closed, unless the user-agent or the server indicates that it wants to keep it alive for further requests.

- **Extensions**: HTTP is an extensible protocol that allows adding new functionality and semantics with new methods, headers, status codes, etc. For example, HTTP/1.1 introduced features such as persistent connections, chunked encoding, caching, etc. HTTP/2 introduced features such as multiplexing, compression, server push, etc. HTTP/3 introduced features such as using QUIC as the underlying transport layer, etc.



### CoAP

- CoAP stands for **Constrained Application Protocol** and it is defined in **RFC 7252** .
- CoAP is an **application-layer protocol** that is intended for use in **resource-constrained Internet devices**, such as wireless sensor network nodes.
- CoAP is designed to easily translate to **HTTP** for simplified integration with the web, while also meeting specialized requirements such as **multicast support**, **very low overhead**, and **simplicity**.
- CoAP is a **client-server protocol** that enables clients to make requests for web transfers and servers to respond to them.
- CoAP uses a **request/response** model similar to HTTP, but with some differences:
  - CoAP uses **UDP** as the underlying transport protocol, instead of TCP .
  - CoAP supports **asynchronous** message exchanges, where a request or a response can be sent without waiting for the previous one to be acknowledged .
  - CoAP messages can be of four types: **confirmable**, **non-confirmable**, **acknowledgment**, and **reset** .
  - CoAP messages have a **binary header** of 4 bytes, followed by optional **options** and a **payload** .
  - CoAP messages are identified by a **message ID** and a **token** .
  - CoAP supports **caching**, **proxying**, and **observing** of resources .
- CoAP is suitable for **IoT applications** that require low power consumption, low latency, and high reliability .
- CoAP can be used for various IoT scenarios, such as **smart home**, **smart city**, **industrial IoT**, **healthcare**, and **environmental monitoring**.



### XMPP

- XMPP stands for **Extensible Messaging and Presence Protocol** .
- It is an **open communication protocol** designed for **instant messaging (IM)**, **presence information**, and **contact list maintenance** .
- It is based on **XML (Extensible Markup Language)**, which enables the **near-real-time exchange of structured data** between two or more network entities .
- It is a **decentralized protocol**, meaning that anyone can run their own XMPP server and communicate with other servers.
- It is a **living standard**, meaning that engineers actively extend and improve it.
- It supports a variety of features and applications, such as:
  - **IoT (Internet of Things)**: XMPP can be used to connect and control devices and sensors over the internet.
  - **WebRTC (Web Real-Time Communication)**: XMPP can be used to establish peer-to-peer audio and video calls in the browser.
  - **Online Gaming**: XMPP can be used to create multiplayer games and chat rooms.
  - **Realtime Social**: XMPP can be used to create social networks and microblogging platforms.
- It uses a **client-server architecture**, meaning that users connect to an XMPP server using an XMPP client.
- It uses a **stream-oriented** approach, meaning that data is sent and received as a continuous stream of XML elements.
- It uses a **stanza-based** model, meaning that data is structured into three types of XML elements: **message**, **presence**, and **iq** (information/query).
  - **Message**: used to send and receive text, media, or other data.
  - **Presence**: used to indicate the availability and status of a user or a resource.
  - **Iq**: used to request and provide information or perform actions.
- It uses a **JID (Jabber Identifier)** to identify users and resources.
  - A JID consists of three parts: **localpart@domainpart/resourcepart**.
  - The **localpart** is the username of the user.
  - The **domainpart** is the domain name of the server.
  - The **resourcepart** is an optional identifier for a specific device or session.
  - Example: alice@example.com/laptop.
- It uses a **SASL (Simple Authentication and Security Layer)** to authenticate users and secure the communication.
- It uses a **TLS (Transport Layer Security)** to encrypt the data and prevent eavesdropping.
- It uses a **DNS (Domain Name System)** to discover and connect to XMPP servers.
- It uses a **SRV (Service) record** to specify the hostname and port number of the XMPP server.
- It uses a **BOSH (Bidirectional-streams Over Synchronous HTTP)** to enable XMPP communication over HTTP.
- It uses a **WebSocket** to enable XMPP communication over a full-duplex TCP connection.
- It uses a **XEP (XMPP Extension Protocol)** to define additional features and functionalities .
  - A XEP is a document that describes a protocol extension, a best practice, or an informational note.
  - There are over 300 XEPs that cover various aspects of XMPP, such as:
    - **Roster**: used to manage the contact list of a user.
    - **MUC (Multi-User Chat)**: used to create and join chat rooms.
    - **PubSub (Publish-Subscribe)**: used to distribute and receive data from multiple sources.
    - **Jingle**: used to initiate and manage peer-to-peer sessions, such as voice and video calls.
    - **Carbons**: used to synchronize messages across multiple devices.
    - **OMEMO**: used to provide end-to-end encryption for messages.
    - **PEP (Personal Eventing Protocol)**: used to publish and subscribe to personal events, such as mood, location, or avatar.
    - **HTTP File Upload**: used to



### AMQP

- AMQP stands for **Advanced Message Queuing Protocol**.
- It is an **open standard**, **binary** application layer protocol designed for **message-oriented middleware**.
- It enables **encrypted** and **interoperable** messaging between organizations and applications.
- It is used in **client/server messaging** and in **IoT device management**.
- It has **reliable**, **secure**, **interoperable**, **open**, and **standard** properties, along with **low overhead** characteristics.
- It has become a good solution for **IoT applications**.
- It supports **claims-based security (CBS)** or **Simple Authentication and Security Layer (SASL)** authentication.
- It supports **MQTT**, **MQTT over WebSockets**, **AMQP over WebSockets**, and **HTTPS** protocols for device-side communications.
- It standardizes messaging using **Producers**, **Brokers** and **Consumers**.
- It defines a **wire-level protocol** that allows applications to communicate with each other using **messages**.
- It supports **publish/subscribe**, **point-to-point**, and **request/reply** messaging patterns.
- It supports **quality of service (QoS)** levels of **at-most-once**, **at-least-once**, and **exactly-once** delivery.
- It supports **message properties**, **headers**, and **annotations** to provide additional information about the messages.
- It supports **message routing**, **filtering**, and **transformation** using **exchanges**, **queues**, and **bindings**.
- It supports **transactions**, **acknowledgements**, and **flow control** to ensure reliable and efficient message delivery.



### MQTT

MQTT stands for **MQ Telemetry Transport**. It is a lightweight, publish-subscribe, machine to machine network protocol for message queue / message queuing service. It is designed for connections with remote locations that have devices with resource constraints or limited network bandwidth, such as in the Internet of Things (IoT).

Some of the main features and concepts of MQTT are:

- **Broker**: A message broker is a server that receives and distributes messages from clients. The broker is responsible for managing the topics and subscriptions, and ensuring the quality of service (QoS) levels.
- **Client**: A client is any device or application that connects to the broker and can publish or subscribe to messages. A client can be a publisher, a subscriber, or both.
- **Topic**: A topic is a hierarchical string that identifies the subject or category of a message. For example, `home/temperature` or `car/speed`. Topics are case-sensitive and can use wildcards (`+` and `#`) to match multiple topics.
- **Message**: A message is a packet of data that contains a topic and a payload. The payload can be any binary or text data, such as JSON, XML, or plain text. The payload size is limited to 256 MB.
- **Publish**: To publish is to send a message to the broker with a specific topic. The broker then delivers the message to all the clients that are subscribed to that topic or a matching topic.
- **Subscribe**: To subscribe is to register an interest in a topic or a set of topics with the broker. The broker then sends any messages that match the subscribed topics to the client.
- **QoS**: QoS stands for quality of service. It is a parameter that defines the reliability and delivery guarantee of a message. There are three levels of QoS:

  - QoS 0: At most once. The message is delivered at most once, but may be lost or duplicated.
  - QoS 1: At least once. The message is delivered at least once, but may be duplicated.
  - QoS 2: Exactly once. The message is delivered exactly once, with no loss or duplication.

- **Retain**: Retain is a flag that indicates whether the broker should store the last message published on a topic. If a client subscribes to a topic with the retain flag set to true, it will receive the last retained message on that topic, if any.
- **Will**: Will is a message that a client can specify when it connects to the broker. The will message is published by the broker if the client disconnects unexpectedly. This can be used to notify other clients about the status of the disconnected client.

MQTT is widely used in IoT applications because of its simplicity, efficiency, scalability, and interoperability. It can support millions of concurrent connections and handle high volumes of data with low latency and bandwidth consumption. It can also work with various platforms and languages, such as Python, Java, C, Node.js, etc. MQTT is an OASIS standard and has many implementations and libraries available .



## Unit 5 - Service Layer Protocols & Security

- The service layer is a layer in the telecommunication network architecture that provides capability servers owned by a network service provider, accessed through open and secure Application Programming Interfaces (APIs) by application layer servers owned by third-party content providers.
- The service layer also provides an interface to core networks at a lower resource layer.
- Service layer protocols are protocols that operate at the service layer and enable communication and data exchange between different applications and services.
- Some examples of service layer protocols are HTTP, SMTP, FTP, SOAP, REST, etc.
- Service layer security is the security of the data and services that are provided or consumed at the service layer.
- Service layer security involves the use of security protocols, mechanisms, and policies to protect the confidentiality, integrity, availability, and authenticity of the data and services.
- Some examples of security protocols that can be used at the service layer are SSL, TLS, IPSec, VPNs, Kerberos, OSPF authentication, SNMPv3, etc.
- Security protocols provide different security services, such as encryption, decryption, authentication, authorization, access control, non-repudiation, etc.
- Security protocols can operate at different layers of the network architecture, such as the application layer, the transport layer, or the network layer.
- Security protocols can also be classified as symmetric or asymmetric, depending on the type of keys they use for encryption and decryption.
- Security protocols can also be classified as stateful or stateless, depending on whether they maintain a session state or not.



### Service Layer for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The service layer is the layer that differentiates the IoT networks or cloud networks from the typical internet networks. It is responsible for providing services and resources to the IoT devices and applications over the internet.
- The service layer includes the following functions :
  - Service discovery or service management: This function enables the IoT devices to find other devices, services and resources over the internet. It also involves the registration and management of the resources on the cloud networks.
  - Data processing and analytics: This function involves the processing and analysis of the data collected from the IoT devices and sensors. It can provide insights, predictions and recommendations based on the data.
  - Application enablement: This function enables the development and deployment of IoT applications that can use the services and resources provided by the service layer. It can also provide APIs and SDKs for the developers to access the data and services.
  - Security: This function ensures the security and privacy of the data and services in the service layer. It can involve encryption, authentication, authorization and access control mechanisms.
- The service layer protocols are the protocols that enable the communication and interaction between the service layer and the other layers of the IoT architecture. Some of the common service layer protocols are  :
  - AMQP: Advanced Message Queuing Protocol is an open standard protocol for message-oriented middleware. It provides reliable and secure delivery of messages between the service layer and the application layer.
  - CoAP: Constrained Application Protocol is a web protocol designed for constrained devices and networks. It provides a RESTful interface for the service layer and the network layer. It supports multicast, caching and asynchronous communication.
  - MQTT: Message Queuing Telemetry Transport is a publish-subscribe protocol for lightweight and low-power communication. It provides a broker-based architecture for the service layer and the network layer. It supports QoS levels and topic-based filtering.
  - XMPP: Extensible Messaging and Presence Protocol is an open standard protocol for instant messaging and presence. It provides a decentralized and federated architecture for the service layer and the application layer. It supports extensions and interoperability.



### oneM2M

- oneM2M is a global partnership project founded in 2012 and constituted by 8 of the world's leading ICT standards development organizations.
- oneM2M aims to develop a common service layer that can be used by various industry IoT verticals, such as smart cities, healthcare, transportation, etc .
- oneM2M service layer consists of a suite of common service functions (CSFs) that provide basic functionalities for IoT applications, such as data management, device management, security, discovery, etc.
- oneM2M service layer is based on a resource-oriented architecture (ROA) that uses RESTful APIs and a hierarchical data model to represent IoT entities and their relationships .
- oneM2M service layer defines three types of common service entities (CSEs) that implement the CSFs and interact with each other and with applications: infrastructure node (IN-CSE), middle node (MN-CSE), and application node (AE-CSE) .
- oneM2M service layer supports various communication protocols and data formats, such as HTTP, CoAP, MQTT, JSON, XML, etc, by using protocol binding and data serialization mechanisms .
- oneM2M service layer provides security features, such as authentication, authorization, encryption, integrity, confidentiality, and privacy, by using standard mechanisms, such as OAuth, TLS, DTLS, etc .
- oneM2M service layer is an open and interoperable standard that is continuously evolving and expanding to meet the needs and challenges of the IoT domain.



### ETSI M2M

- ETSI M2M stands for European Telecommunications Standards Institute Machine-to-Machine.
- It is a standardization body that develops standards for M2M and IoT technologies.
- It is one of the founding partners of oneM2M, the global standards initiative for M2M and IoT interoperability.
- ETSI M2M defines a high-level architecture for M2M systems, as shown in the figure below.

ETSI M2M high-level architecture

- The architecture consists of three main layers: the M2M Device and Gateway layer, the M2M Network layer, and the M2M Service layer.
- The M2M Device and Gateway layer includes the devices, sensors, and actuators that communicate with each other or with the M2M Network layer through M2M Area Networks (MANs).
- The M2M Network layer provides connectivity and routing services for the M2M Device and Gateway layer and the M2M Service layer. It can use various network technologies, such as cellular, Wi-Fi, or Ethernet.
- The M2M Service layer provides the core functionality and intelligence of the M2M system. It consists of the M2M Service Capability Layer (SCL) and the M2M Applications.
- The M2M SCL is a middleware that enables the management, discovery, and access of M2M resources and services. It exposes a common Application Programming Interface (API) for the M2M Applications and the M2M Network layer.
- The M2M Applications are the software components that implement the specific logic and functionality of the M2M system. They can run on the M2M Devices, the M2M Gateways, or the M2M SCL.
- ETSI M2M also defines a resource structure for the M2M SCL, which is based on a hierarchical tree model. Each resource has a unique identifier, a set of attributes, and a set of sub-resources. The resources can be accessed and manipulated through the M2M API using CRUD (Create, Retrieve, Update, Delete) operations.
- ETSI M2M also specifies the interactions and protocols for the communication between the different layers and components of the M2M system. It supports various protocols, such as HTTP, CoAP, MQTT, or WebSocket.
- ETSI M2M also addresses the security aspects of the M2M system, such as authentication, authorization, encryption, and integrity. It defines a security framework that covers the M2M Device and Gateway layer, the M2M Network layer, and the M2M Service layer.
- ETSI M2M also supports the semantic interoperability of the M2M system, which is the ability to exchange and understand data and information across different domains and applications. It proposes a reference ontology and a semantic annotation mechanism for the M2M resources and services.



### OMA for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- OMA stands for Open Mobile Alliance, an organization that develops standards and specifications for the mobile and IoT industry.
- OMA LwM2M is one of the service layer protocols developed by OMA for IoT device management and service enablement .
- LwM2M stands for Lightweight Machine to Machine, and it is based on the Constrained Application Protocol (CoAP), a RESTful protocol for constrained devices and networks.
- LwM2M defines the application layer communication protocol between an LwM2M Server and an LwM2M Client, which is located in an IoT device.
- LwM2M provides four main features: device management, information reporting, firmware update, and remote control.
- LwM2M uses an object model to represent the resources and functionalities of an IoT device. An object is a collection of related resources, and a resource is a piece of information or an action that can be accessed or executed by the LwM2M Server.
- LwM2M defines a set of standard objects for common IoT use cases, such as device, connectivity monitoring, location, security, software management, etc. It also allows the creation of custom objects for specific applications.
- LwM2M supports different transport bindings, such as UDP, TCP, SMS, and non-IP data delivery (NIDD). It also supports different data formats, such as plain text, TLV, JSON, and CBOR.
- LwM2M provides end-to-end security for the IoT service topologies, using DTLS for the transport layer security and OSCORE for the application layer security. DTLS protects the data in transit between the LwM2M Server and the LwM2M Client, while OSCORE protects the data end-to-end, even if it passes through intermediate nodes or proxies.
- LwM2M is designed to be efficient, scalable, interoperable, and extensible for the IoT environment. It can support millions of devices with low bandwidth and power consumption, and it can interoperate with other IoT protocols, such as MQTT, HTTP, and WebSockets . It can also be extended with new objects, transport bindings, data formats, and security mechanisms .



### BBF for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Service layer protocols are the protocols that enable the communication and interaction among applications and services running on different IoT devices and on cloud/edge infrastructures.
- Security of service layer protocols is crucial for ensuring the confidentiality, integrity, availability, and privacy of the data and services in IoT.
- Some of the common service layer protocols in IoT are:
  - Constrained Application Protocol (CoAP): A lightweight protocol that is HTTP-friendly and uses two basic message types: request and response. It supports confirmable and non-confirmable messages, as well as multicast and observe options. It also provides security features such as encryption, authentication, and authorization using Datagram Transport Layer Security (DTLS).
  - Message Queuing Telemetry Transport (MQTT): A publish-subscribe protocol that uses a broker to facilitate the communication between publishers and subscribers. It is designed for low-bandwidth, high-latency, and unreliable networks. It offers three levels of quality of service (QoS): at most once, at least once, and exactly once. It also supports Transport Layer Security (TLS) for secure communication.
  - Advanced Message Queuing Protocol (AMQP): An open standard protocol that provides reliable and interoperable messaging between applications and services. It uses a broker to route messages based on exchanges, queues, and bindings. It supports different message delivery modes, such as persistent, transient, and mandatory. It also supports TLS and SASL for security.
- Some of the security challenges and solutions for service layer protocols in IoT are:
  - Data privacy: The protection of sensitive and personal data from unauthorized access and disclosure. Some of the solutions include data encryption, anonymization, pseudonymization, and access control mechanisms .
  - Authentication: The verification of the identity of the communicating parties. Some of the solutions include certificates, passwords, tokens, biometrics, and challenge-response schemes .
  - Authorization: The granting of permissions and privileges to the authenticated parties. Some of the solutions include role-based access control, attribute-based access control, and policy-based access control .
  - Trust management: The establishment and maintenance of trust relationships among the communicating parties. Some of the solutions include reputation systems, trust models, and trust negotiation protocols .
- BBF (Broadband Forum) is an industry organization that develops standards and best practices for broadband networks and services. One of its projects is the User Services Platform (USP), which is a protocol for managing and controlling IoT devices and services. USP is based on the CPE WAN Management Protocol (CWMP), which is commonly known as TR-069.
- USP provides the following features and benefits for IoT service layer protocols and security:
  - Simple migration from CWMP through the use of the same data model and data modeling tools.
  - Support for multiple transport protocols, such as HTTP, WebSocket, CoAP, and MQTT.
  - Support for secure communication using TLS and DTLS, as well as authentication and authorization using certificates and tokens.
  - Support for device grouping, device discovery, device configuration, device monitoring, device control, and device firmware upgrade.
  - Support for event-driven and scheduled communication, as well as push and pull modes.



### Security in IoT Protocols

- Security is a major challenge for IoT systems, as they involve a large number of heterogeneous devices, networks, and applications that communicate and exchange data over the internet.
- Security in IoT protocols refers to the methods and mechanisms that ensure the confidentiality, integrity, availability, and authenticity of data and devices in IoT systems.
- Some of the security requirements for IoT protocols are:
  - Data privacy: protecting the sensitive and personal data of users and devices from unauthorized access and disclosure.
  - Data integrity: ensuring that the data is not tampered with or corrupted during transmission or storage.
  - Data availability: ensuring that the data and devices are accessible and functional when needed.
  - Authentication: verifying the identity and legitimacy of the devices and users that participate in IoT systems.
  - Authorization: granting or denying access and privileges to the devices and users based on predefined policies and rules.
  - Trust management: establishing and maintaining trust relationships among the devices and users in IoT systems.
- Some of the security threats and attacks that IoT protocols have to deal with are:
  - Eavesdropping: intercepting and listening to the data transmitted over the network.
  - Replay: capturing and retransmitting the data to impersonate or deceive the legitimate devices or users.
  - Modification: altering or modifying the data to cause damage or disruption to the IoT system.
  - Denial-of-service: flooding the network or devices with excessive or malicious traffic to prevent them from functioning properly.
  - Spoofing: forging or falsifying the identity or location of the devices or users to gain unauthorized access or privileges.
  - Man-in-the-middle: inserting a malicious node between the sender and receiver to intercept, modify, or redirect the data.
- Some of the security protocols that are used or proposed for IoT systems are:
  - MQTT: a lightweight and publish-subscribe messaging protocol that supports encryption, authentication, and authorization using TLS/SSL, username/password, and access control lists .
  - CoAP: a web-based and RESTful protocol that supports encryption, authentication, and authorization using DTLS, pre-shared keys, certificates, and tokens.
  - LwM2M: a device management and service layer protocol that supports encryption, authentication, and authorization using DTLS, pre-shared keys, certificates, and bootstrap server.
  - XMPP: an extensible and XML-based messaging protocol that supports encryption, authentication, and authorization using TLS/SSL, SASL, and XEP-0198.
  - AMQP: an advanced and reliable messaging protocol that supports encryption, authentication, and authorization using TLS/SSL, SASL, and ACL.



### MAC 802.15.4

- MAC 802.15.4 is a standard for low-rate wireless personal area networks (LR-WPANs) that defines the physical layer (PHY) and medium access control (MAC) sublayer specifications  .
- MAC 802.15.4 is designed for low-data-rate wireless connectivity with fixed, portable, and moving devices with no battery or very limited battery consumption requirements .
- MAC 802.15.4 supports multiple PHYs for different frequency bands and modulation schemes, such as 2.4 GHz O-QPSK, 868/915 MHz BPSK, and 950 MHz GFSK  .
- MAC 802.15.4 provides two types of MAC services: data service and management service .
  - Data service enables the transmission and reception of MAC protocol data units (MPDUs) between peer MAC entities .
  - Management service enables the configuration and maintenance of the MAC sublayer and the coordination of the PHY sublayer .
- MAC 802.15.4 supports two types of network topologies: star and peer-to-peer .
  - Star topology consists of a single coordinator (PAN coordinator) and multiple devices that communicate only with the coordinator .
  - Peer-to-peer topology consists of multiple devices that can communicate with each other directly or through one or more coordinators .
- MAC 802.15.4 supports two types of device roles: coordinator and device .
  - Coordinator is a device that has the ability to start a network, synchronize other devices, and allocate addresses .
  - Device is a device that can join a network, communicate with other devices, and perform MAC management functions .
- MAC 802.15.4 supports two types of addressing modes: short and extended .
  - Short addressing mode uses 16-bit addresses that are allocated by the coordinator within a personal area network (PAN) .
  - Extended addressing mode uses 64-bit addresses that are globally unique and assigned by the manufacturer .
- MAC 802.15.4 supports two types of channel access methods: slotted and unslotted CSMA/CA .
  - Slotted CSMA/CA is a contention-based channel access method that uses a superframe structure with active and inactive periods, where the active period is divided into 16 equally sized time slots .
  - Unslotted CSMA/CA is a contention-based channel access method that does not use a superframe structure and allows devices to transmit at any time after sensing the channel to be idle .
- MAC 802.15.4 supports two types of frame formats: beacon and non-beacon .
  - Beacon frame is a frame that is transmitted by the coordinator periodically to synchronize devices, announce the PAN identifier, and indicate the availability of pending data .
  - Non-beacon frame is a frame that is transmitted by any device to transfer data or perform MAC management functions .
- MAC 802.15.4 supports four types of frame types: data, acknowledgment, MAC command, and multipurpose .
  - Data frame is a frame that carries upper layer data or MAC sublayer data .
  - Acknowledgment frame is a frame that is sent to confirm the successful reception of a data or MAC command frame .
  - MAC command frame is a frame that is used to perform MAC management functions, such as association, disassociation, or data request .
  - Multipurpose frame is a frame that can carry any type of payload and can be used for different purposes, such as ranging, security, or fragmentation .
- MAC 802.15.4 supports two types



### 6LoWPAN

- 6LoWPAN stands for IPv6 over Low-power Wireless Personal Area Networks.
- It is an open standard defined by the Internet Engineering Task Force (IETF) that enables low-power devices with limited processing capabilities to participate in the Internet of Things (IoT) using IPv6.
- It specifies mechanisms for encapsulation, header compression, neighbor discovery, routing, security, and interoperability of IPv6 over IEEE 802.15.4 based networks, which are low-rate wireless personal area networks (LR-WPANs) that operate in the 2.4 GHz ISM band .
- 6LoWPAN allows IPv6 datagrams to be transmitted over LR-WPANs with minimal overhead, by compressing the IPv6 header and using fragmentation and reassembly when needed.
- 6LoWPAN also supports mesh networking, where devices can relay packets for each other to extend the network coverage and reachability.
- 6LoWPAN networks can be connected to the Internet or other IPv6 networks through edge routers, which perform the necessary translation and adaptation between different link layers .
- 6LoWPAN networks can benefit from the features of IPv6, such as end-to-end addressing, auto-configuration, mobility, security, and scalability .
- 6LoWPAN is suitable for applications that require wireless internet connectivity at lower data rates, such as residential and office automation, smart grid, industrial monitoring, healthcare, and environmental sensing.



### RPL for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for Routing Protocol for Low-Power and Lossy Networks, which are networks that have limited resources, high packet loss, and dynamic topology  .
- RPL is designed for IoT applications that require multipoint-to-point (MP2P) and point-to-multipoint (P2MP) traffic, such as data collection and dissemination  .
- RPL operates on top of the IPv6 protocol and uses the 6LoWPAN adaptation layer to compress the IPv6 headers and fit them into the small frames of the IEEE 802.15.4 standard  .
- RPL organizes the network into a Destination Oriented Directed Acyclic Graph (DODAG), which is a tree-like structure rooted at a node called the DODAG root. The DODAG root acts as the sink or the source of the data traffic  .
- RPL uses two types of control messages to build and maintain the DODAG: DODAG Information Object (DIO) and Destination Advertisement Object (DAO). DIO messages are used to advertise the DODAG parameters and the rank of the sender, which is a metric that indicates the position of the node in the DODAG. DAO messages are used to propagate the routing information from the leaf nodes to the DODAG root  .
- RPL supports multiple routing metrics and constraints, such as hop count, latency, energy, and reliability, to optimize the DODAG formation according to the application requirements. RPL also supports multiple DODAG instances within the same network, each with a different objective function that defines how the routing metrics and constraints are combined  .
- RPL provides security mechanisms to protect the integrity and authenticity of the control messages and the routing information. RPL uses the Datagram Transport Layer Security (DTLS) protocol to establish a secure channel between the nodes and the DODAG root, and uses the RPL Option for Carrying RPL Information in Data-Plane (RPI) to verify the source and the path of the data packets  .
- RPL also faces some security challenges and vulnerabilities, such as rank attacks, version number attacks, DAO inconsistency attacks, DIO suppression attacks, and local repair attacks, which can disrupt the network performance and cause routing loops, black holes, or sinkholes  .
- RPL security can be enhanced by using cryptographic techniques, such as digital signatures, message authentication codes, and encryption, as well as non-cryptographic techniques, such as anomaly detection, trust management, and reputation systems  .



### Application Layer for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The application layer is the interface between the IoT device and the network with which it will communicate.
- It handles data formatting and presentation and serves as the bridge between what the IoT device is doing and the network handoff of the data it produces.
- It also provides services such as data storage, processing, analysis, visualization, and management.
- Some of the common application layer protocols in IoT are :
  - MQTT: Message Queuing Telemetry Transport is a lightweight publish-subscribe protocol that is designed for low-bandwidth, high-latency, and unreliable networks. It is widely used for IoT applications that require real-time data delivery, such as smart home, smart grid, and industrial automation.
  - CoAP: Constrained Application Protocol is a web transfer protocol that is optimized for constrained devices and networks. It is based on the RESTful architecture and uses UDP as the transport layer. It supports features such as multicast, caching, and asynchronous communication. It is suitable for IoT applications that involve resource discovery, device management, and sensor networks.
  - HTTP: Hypertext Transfer Protocol is the most common web protocol that is used for data exchange between clients and servers. It is based on the request-response model and uses TCP as the transport layer. It supports features such as authentication, encryption, compression, and caching. It is used for IoT applications that require web-based access, such as cloud services, web portals, and mobile apps.
  - AMQP: Advanced Message Queuing Protocol is an open standard for message-oriented middleware that is designed for high-performance, reliability, and interoperability. It is based on the broker model and uses TCP as the transport layer. It supports features such as routing, queuing, transactions, and security. It is used for IoT applications that require complex messaging patterns, such as enterprise integration, smart city, and e-commerce.
- The application layer also involves security aspects such as data encryption, authentication, authorization, and integrity.
- Some of the common security mechanisms in the application layer are:
  - TLS: Transport Layer Security is a cryptographic protocol that provides secure communication over a network. It uses certificates and keys to establish a secure channel between the client and the server. It protects the data from eavesdropping, tampering, and impersonation. It is used for IoT applications that require end-to-end security, such as banking, health care, and e-government.
  - DTLS: Datagram Transport Layer Security is a variant of TLS that is adapted for datagram-based protocols such as UDP and CoAP. It provides the same security features as TLS, but with some modifications to handle packet loss, reordering, and duplication. It is used for IoT applications that require security over unreliable networks, such as smart metering, smart lighting, and smart parking.
  - OAuth: Open Authorization is a framework that enables third-party applications to access resources on behalf of a user. It uses tokens and scopes to grant and limit the access rights of the applications. It protects the user's credentials and privacy from unauthorized access. It is used for IoT applications that require social networking, personalization, and sharing, such as fitness, entertainment, and education.

