## Unit 2 - Open Grid Services Architecture

The Open Grid Services Architecture (OGSA) is a service-oriented architecture for a grid computing environment for business and scientific use. It was developed within the Open Grid Forum, which was called the Global Grid Forum (GGF) at the time, around 2002 to 2006.

OGSA is based on several other Web service technologies, such as the Web Services Description Language (WSDL) and the Simple Object Access Protocol (SOAP), but it aims to be largely independent of transport-level handling of data. OGSA has been described as a refinement of a Web services architecture, specifically designed to support grid requirements.

The concept of OGSA is derived from work presented in the 2002 Globus Alliance paper "The Physiology of the Grid" by Ian Foster, Carl Kesselman, Jeffrey M. Nick, and Steven Tuecke. It was developed by GGF working groups which resulted in a document, entitled The Open Grid Services Architecture, Version 1.5 in 2006.

The document focuses on requirements and the scope of important capabilities required to support Grid systems and applications in both e-science and e-business. The capabilities described are Execution Management, Data, Resource Management, Security, Self-Management, and Information. The description of the capabilities is at a high-level and includes, to some extent, the interrelationships between the capabilities.

The following diagram illustrates the basic architecture of OGSA:

```
+---------------------+
|     Application     |
+---------------------+
|     Information     |
+---------------------+
|    Self-Management  |
+---------------------+
|     Security        |
+---------------------+
| Resource Management |
+---------------------+
|      Data           |
+---------------------+
| Execution Management|
+---------------------+
|  Infrastructure     |
+---------------------+
|    Web Services     |
+---------------------+
|    Transport        |
+---------------------+
```

Each capability is composed of a set of services that provide specific functions and behaviors. For example, the Execution Management capability includes services for job management, selection, and reservation. The Data capability includes services for data access, transfer, replication, and integration. The Resource Management capability includes services for resource discovery, allocation, reservation, and monitoring. The Security capability includes services for authentication, authorization, auditing, and encryption. The Self-Management capability includes services for configuration, fault tolerance, and adaptation. The Information capability includes services for metadata management, discovery, and notification.

OGSA is an architectural process in which the OGSA Working Group collects requirements and maintains a set of informational documents that describe the architecture. It also defines a set of normative specifications and profiles that document the precise requirements for a conforming hardware or software component. OGSA aims to enable the deployment of grid solutions that are interoperable even though they may be based on implementations from multiple sources.

OGSA is not a software product or a platform, but rather a set of standards and guidelines for building grid systems and applications. OGSA is intended to be compatible with existing and emerging Web service technologies, and to leverage the benefits of service-oriented architectures, such as loose coupling, interoperability, and composability.