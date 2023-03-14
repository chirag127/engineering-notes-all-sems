### Composite Applications for the notes of the Unit 3 - Service-Oriented Applications in the subject of Service Oriented Architecture

- A composite application is a software application built by combining multiple existing functions into a new application.
- A composite application can use business sources (e.g., existing modules or even web services) of information, while mashups usually rely on web-based, and often free, sources.
- A composite application can be built using any technology or architecture, and it is not necessary to use service-oriented architecture (SOA) for it.
- However, SOA is a common approach to implementing composite applications, as it provides a set of specifications that describe a programming model for building applications and systems using services.
- SOA extends and complements previous approaches to implementing services and builds on open standards such as web services.
- A service is an addressable interface for a component that can contain one or more operations.
- A component is an application program that implements the business logic and configuration information.
- A component can offer a service to other components and consume functions offered by other services using service-oriented interfaces.
- A component can also contain other components or composites, allowing for a hierarchical construction of composite applications.
- A composite is the unit of deployment in SOA and is described in an XML language called SCDL.
- A composite can contain components, services, references, property declarations, and the wiring that describes the connections between these elements.
- A composite can also have external services and references, which use bindings to describe the access mechanism that external clients or services must use to call or be called by the composite.
- A composite application can contain both new components that are created specifically for the business application and existing components that are reused from other applications.
- A composite application can provide a high-level service that is implemented internally by sets of lower-level services.
- A composite application can benefit from the advantages of SOA, such as reusability, interoperability, loose coupling, scalability, and agility.

#### Mnemonics and learning tricks

- To remember the definition of a composite application, you can use the acronym CAFE: Composite Application is a Functionality Ensemble.
- To remember the elements of a composite, you can use the acronym CRISP: Components, References, Interfaces, Services, Properties.
- To remember the benefits of SOA, you can use the acronym RISLA: Reusability, Interoperability, Scalability, Loose coupling, Agility.

#### ASCII diagram

Here is an example of an ASCII diagram that shows a composite application based on SOA:

```
+-----------------+      +-----------------+      +-----------------+
| External client |      | External client |      | External client |
+-----------------+      +-----------------+      +-----------------+
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         v                       v                       v
+-----------------+      +-----------------+      +-----------------+
| Composite       |      | Composite       |      | Composite       |
| service         |      | service         |      | service         |
+-----------------+      +-----------------+      +-----------------+
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         v                       v                       v
+-----------------+      +-----------------+      +-----------------+
| Component       |      | Component       |      | Component       |
| service         |      | service         |      | service         |
+-----------------+      +-----------------+      +-----------------+
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |