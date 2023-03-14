### Service Oriented Architecture for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

- Service Oriented Architecture (SOA) is an architectural style that focuses on discrete services instead of a monolithic design. 
- A service is a discrete unit of functionality that can be accessed remotely and acted upon and updated independently, such as retrieving a credit card statement online. 
- SOA aims to allow users to combine large chunks of functionality to form applications that are built purely from existing services and combining them in an ad hoc manner. 
- A service presents a simple interface to the requester that abstracts away the underlying complexity acting as a black box. 
- Services use common interface standards and an architectural pattern so they can be rapidly incorporated into new applications. 
- Services communicate with each other by passing data in a well-defined, shared format, or by coordinating an activity between two or more services. 
- Services are loosely coupled, meaning they can be called with little or no knowledge of how the service is implemented underneath, reducing the dependencies between applications. 
- Services can be built from scratch or by exposing functions from legacy systems of record as service interfaces. 
- Services can be written in any programming language, supplied as packaged software applications by a vendor, SaaS applications, or obtained as open source applications. 
- Services are exposed using standard network protocols, such as SOAP/HTTP or RESTful HTTP. 
- Service governance controls the lifecycle for development and at the appropriate stage the services are published in a registry that enables developers to quickly find them and reuse them to assemble new applications or business processes. 
- An Enterprise Service Bus (ESB) is an architectural pattern whereby a centralized software component performs integrations between applications. 

#### Advantages of SOA

- SOA promotes reusability and interoperability of software components, reducing development time and cost.  
- SOA enables flexibility and agility in responding to changing business needs and requirements.  
- SOA facilitates integration and collaboration between different systems and organizations.  
- SOA improves scalability and performance by distributing the workload among multiple services.  
- SOA enhances maintainability and reliability by isolating faults and allowing independent updates of services.  

#### Disadvantages of SOA

- SOA introduces complexity and overhead in designing, developing, testing, and deploying services.  
- SOA requires governance and management of services, such as security, quality, versioning, and monitoring.  
- SOA may face interoperability and compatibility issues due to the diversity of technologies and standards involved.  
- SOA may increase network traffic and latency due to the frequent communication between services.  

#### Examples of SOA

- Amazon Web Services (AWS) is a cloud computing platform that provides various services, such as computing, storage, database, networking, analytics, and security, that can be accessed and combined by users via web service interfaces. 
- Google Maps is a web mapping service that provides various features, such as geocoding, directions, traffic, street view, and satellite imagery, that can be accessed and integrated by users via web service interfaces. 
- Salesforce is a cloud-based software company that provides various services, such as customer relationship management (CRM), marketing, sales, and commerce, that can be accessed and customized by users via web service interfaces. 

#### Mnemonics and learning tricks for SOA

- A possible mnemonic to remember the four properties of a service is **RISC** (Repeatable, Independent, Self-contained, Composable). 
- A possible mnemonic to remember the advantages of SOA is **FRIES** (Flexibility, Reusability, Integration, Efficiency, Scalability).  
- A possible mnemonic to remember the disadvantages of SOA is **COIN** (Complexity, Overhead, Interoperability, Network).  
- A