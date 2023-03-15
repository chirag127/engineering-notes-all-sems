 Here is the content in markdown format for the topic ### IoT/M2M systems layers and design standardization for the notes of the Unit 1 - Internet of Things (IoT) in the subject of Internet of Things:

### IoT/M2M systems layers and design standardization

The IoT system can be viewed as a stack of layers, each providing a specific set of functions/services to the layers above it. The most common architecture is a three to five layered model:

- Perception layer: This is the bottom-most layer which consists of sensors and actuators. Sensors gather data from the physical world and convert the sensed quantities into electronic signals. Actuators convert electronic signals into actions.
- Network layer: This layer handles the communication between the different components of the IoT system. It can use various wireless and wired technologies (e.g. WiFi, Bluetooth, etc.).
- Processing layer: This layer processes the data from the sensors and determines appropriate actions. It performs tasks such as data cleaning, aggregation, and fusion. It can be implemented using embedded systems or cloud servers.
- Application layer: This layer consists of the applications and services running on the IoT system. It interfaces with the users and supports various use cases (e.g. smart homes, smart cities, industrial IoT, etc.).
- Business layer: This optional layer handles the business aspects of the IoT system such as monetization, business models, privacy, security, etc.

To ensure interoperability between IoT systems and components from different vendors, several standardization organizations have defined reference architectures and frameworks for IoT. Some of the major standards include:

- OneM2M: Service layer standard for M2M/IoT from ETSI and partners
- OCF: Open Connectivity Foundation, focuses on device level interoperability
- IEEE P2413: Architectural framework and reference model for IoT
- ISO/IEC CC standards on IoT reference architecture and framework

The standards typically define layers similar to the generic three to five layered model and specify protocols and interfaces to facilitate interworking between the layers. Following these standards during the design and development of IoT systems can enable device and system interoperability as well as simplify the integration of components from different vendors.