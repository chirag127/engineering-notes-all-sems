## Unit 2 - Open Grid Services Architecture

- Open Grid Services Architecture (OGSA) is a service-oriented architecture for a grid computing environment for business and scientific use. It was developed within the Open Grid Forum, which was called the Global Grid Forum (GGF) at the time, around 2002 to 2006. 
- OGSA is a distributed interaction and computing architecture based on services, assuring interoperability on heterogeneous systems so that different types of resources can communicate and share information. OGSA is based on several other Web service technologies, such as the Web Services Description Language (WSDL) and the Simple Object Access Protocol (SOAP), but it aims to be largely independent of transport-level handling of data. 
- OGSA has been described as a refinement of a Web services architecture, specifically designed to support grid requirements.  The concept of OGSA is derived from work presented in the 2002 Globus Alliance paper "The Physiology of the Grid" by Ian Foster, Carl Kesselman, Jeffrey M. Nick, and Steven Tuecke. 
- OGSA defines a core set of interfaces, behaviors, resource models, and bindings that enable the integration, virtualization, and management of grid systems and applications.  The document focuses on requirements and the scope of important capabilities required to support Grid systems and applications in both e-science and e-business. The capabilities described are Execution Management, Data, Resource Management, Security, Self-Management, and Information. 
- OGSA is an architectural process in which the GGF's OGSA Working Group collects requirements and maintains a set of informational documents that describe the architecture; a set of normative specifications and profiles that document the precise requirements for a conforming hardware or software component; and software components that adhere to the OGSA specifications and profiles, enabling deployment of grid solutions that are interoperable even though they may be based on implementations from multiple sources. 

### OGSA Framework

- The OGSA framework consists of three layers: the infrastructure layer, the capabilities layer, and the application layer. 

- The infrastructure layer provides the basic mechanisms for creating, naming, discovering, and managing services. It also defines the common behaviors and properties of services, such as lifetime, notification, and security. The infrastructure layer is based on existing Web service standards, such as WSDL, SOAP, UDDI, and WS-Security, as well as extensions such as Web Services Resource Framework (WSRF) and WS-Management. 

- The capabilities layer defines the specific functionalities and interfaces of services that address the key concerns in grid systems, such as execution management, data management, resource management, security, self-management, and information. The capabilities layer is composed of several OGSA services, each of which provides a well-defined set of operations and behaviors. The capabilities layer also defines the common resource models and schemas that enable the interoperability and integration of different types of resources. 

- The application layer consists of the grid applications and services that use the capabilities layer to achieve their goals. The application layer may also define additional domain-specific services and interfaces that are not part of the OGSA standard. The application layer is the most diverse and dynamic layer, as it reflects the specific needs and requirements of different users and communities. 

- The following diagram illustrates the OGSA framework and its layers. 

```
+---------------------+
| Application Layer   |
|                     |
| +-----------------+ |
| | Grid Apps &    | |
| | Services       | |
| +-----------------+ |
+---------------------+
| Capabilities Layer  |
|                     |
| +-----------------+ |
| | Execution      | |
| | Management     | |
| +-----------------+ |
| +-----------------+ |
| | Data           | |
| | Management     | |
| +-----------------+ |
| +-----------------+ |
| | Resource       | |
| | Management     | |
| +-----------------+ |
| +-----------------+ |
| | Security       | |
| +-----------------+ |