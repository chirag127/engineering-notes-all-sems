The following is a detailed ASCII diagram for Service-oriented Analysis and Design (SOAD) Process for the notes of the Unit 2 - Enterprise-Wide SOA in the subject of Service Oriented Architecture.

The diagram is based on the SOAD process model defined by  and the key artifacts identified by . The diagram shows the main phases and activities of the SOAD process, as well as the inputs and outputs of each activity. The diagram also shows the variation points that can be used to customize the services for different clients and contexts.

The diagram uses the following symbols:

- [ ]: A phase of the SOAD process
- ->: A flow of information or artifacts from one activity to another
- <>: A variation point that can be used to adapt the services
- (): An input or output of an activity
- {}: A set of artifacts
- *: A reference to a source of information or guidance

The diagram is as follows:

```
[Service Identification] -> [Service Specification] -> [Service Realization] -> [Service Deployment]

[Service Identification]
- Identify business goals and drivers (*EA frameworks, BPM, OOAD)
- Identify business processes and activities (*BPM, OOAD)
- Identify candidate services and capabilities (*BPM, OOAD, service harvesting)
- Categorize and prioritize services and capabilities (*service categorization, service granularity)
- Define service contracts and policies (*service contract, service policy)
- (Business goals, drivers, processes, activities, services, capabilities, contracts, policies) -> [Service Specification]

[Service Specification]
- Specify service interface and behavior (*WSDL, BPEL, UML)
- Specify service quality attributes and constraints (*QoS, SLA, non-functional requirements)
- Specify service dependencies and compositions (*service orchestration, service choreography, service aggregation)
- Specify service variability and adaptation (*variation points, policies, aspects, semantic brokering)
- (Service interface, behavior, quality, dependencies, compositions, variability, adaptation) -> [Service Realization]

[Service Realization]
- Design service implementation and deployment (*service component, service container, service binding)
- Design service testing and verification (*service testing, service verification, service validation)
- Design service monitoring and management (*service monitoring, service management, service governance)
- Implement service components and containers (*programming languages, frameworks, tools)
- Test and verify service components and containers (*testing tools, verification tools, validation tools)
- (Service implementation, deployment, testing, verification, monitoring, management) -> [Service Deployment]

[Service Deployment]
- Deploy service components and containers (*deployment tools, deployment environments)
- Monitor and manage service components and containers (*monitoring tools, management tools, governance tools)
- (Service components, containers, deployment, monitoring, management) -> [Service Identification] (for service evolution)

<> Variation points:
- Service granularity: The level of abstraction and detail of a service or capability
- Service categorization: The classification of services or capabilities based on their functionality, domain, or purpose
- Service aggregation: The grouping of services or capabilities to form a higher-level service or capability
- Service orchestration: The coordination of services or capabilities to achieve a business goal or process
- Service choreography: The collaboration of services or capabilities to achieve a business goal or process
- Service policy: The rules and constraints that govern the behavior and quality of a service or capability
- Service aspect: The cross-cutting concerns that affect the behavior and quality of a service or capability
- Service contract: The agreement between a service provider and a service consumer on the interface, behavior, and quality of a service or capability
- Service binding: The mechanism that connects a service consumer to a service provider
- Service brokering: The mediation of service discovery, selection, and invocation between a service consumer and a service provider
- Service harvesting: The identification and extraction of reusable services or capabilities from existing systems or applications
- Service knowledge: The information and expertise that can be used to design, implement, and manage services or capabilities
```