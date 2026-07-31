### Deployment
- Deployment is the process of installing, configuring, and running a software system on a target platform.
- Deployment diagrams are used to model the physical aspects of a software system, such as the hardware, the network, the nodes, the components, and the artifacts.
- Deployment diagrams show how the components of a system are distributed across different nodes, and how they communicate with each other.
- Deployment diagrams can also show the configuration and properties of the nodes and the components, such as the processor, the memory, the operating system, the middleware, the protocols, etc.
- Deployment diagrams are useful for planning, testing, and managing the deployment of a software system, as well as for analyzing its performance, scalability, reliability, and security.

#### Elements of a deployment diagram
- A node is a physical entity that executes one or more components of a system. A node can represent a device, a server, a workstation, a mobile phone, etc. A node is depicted as a cube with the name of the node and optionally its properties.
- A component is a modular and replaceable part of a system that provides a specific functionality or a set of functionalities. A component can represent a software module, a library, a framework, a subsystem, etc. A component is depicted as a rectangle with two smaller rectangles on the left side and the name of the component and optionally its properties.
- An artifact is a concrete and tangible piece of information that is produced or used by a component. An artifact can represent a source code file, a binary file, a configuration file, a database, a document, etc. An artifact is depicted as a rectangle with the name of the artifact and optionally its properties and a stereotype that indicates its type.
- A deployment specification is a set of parameters that defines how an artifact is deployed on a node. A deployment specification can include the location, the version, the configuration, the dependencies, etc. of an artifact. A deployment specification is depicted as a rectangle with the name of the deployment specification and optionally its properties and a stereotype that indicates its type.
- A dependency is a relationship that indicates that a component or an artifact depends on another component or artifact for its specification or implementation. A dependency is depicted as a dashed arrow with the name of the dependency and optionally its properties and a stereotype that indicates its type.
- An association is a relationship that indicates that two nodes or two components are connected or communicate with each other. An association is depicted as a solid line with the name of the association and optionally its properties and a stereotype that indicates its type.
- A communication path is a special type of association that indicates that two nodes can exchange signals or messages. A communication path is depicted as a solid line with the name of the communication path and optionally its properties and a stereotype that indicates its type.

#### Example of a deployment diagram
The following diagram shows an example of a deployment diagram for a web-based online shopping system.

![Deployment diagram example](https://i.imgur.com/8Yy8w0o.png)

The diagram shows the following elements:

- A node named Web Server that executes two components: Web Application and Database Connector. The Web Server node has a property named IP address that specifies its network address.
- A node named Database Server that executes one component: Database Management System. The Database Server node has a property named IP address that specifies its network address.
- A component named Web Application that provides the user interface and the business logic of the system. The Web Application component has a property named URL that specifies its web address.
- A component named Database Connector that provides the access to the database of the system. The Database Connector component has a property named Driver that specifies the type of database driver it uses.
- A component named Database Management System that provides the storage and manipulation of the data of the system. The Database Management System component has a property named DBMS that specifies the type of database management system it uses.
- An artifact named WebApp.war that represents the web archive file that contains the web application. The WebApp.war artifact has a stereotype named <<executable>> that indicates that it is an executable file.
- An artifact named DBConnector.jar that represents the Java archive file that contains the database connector. The DBConnector.jar artifact has a stereotype named <<library>> that indicates that it is a library file.
- An artifact named OnlineShop.db that represents the database file that contains the data of the system. The OnlineShop.db artifact has a stereotype named <<database>> that indicates that it is a database file.
- A deployment specification named WebApp.war.deploy that defines how the WebApp.war artifact is deployed on the Web Server node. The WebApp.war.deploy deployment specification has a stereotype named <<deploy>> that indicates that it is a deployment specification file.
- A deployment specification