## Unit 4 - Service-Oriented Analysis and Design

Service-Oriented Analysis and Design (SOAD) is a methodology that refers to the modeling and design for service-oriented architecture (SOA) applications. SOA is an architectural style that aims to achieve loose coupling among interacting software agents by using services as the fundamental unit of composition. Services are self-contained, reusable, and interoperable components that expose their functionality through standard interfaces and protocols.

A SOAD approach in designing SOA applications requires the following key elements:

- Process Model: Defining process and notation by orchestrating object-oriented analysis and design (OOAD), business process modeling (BPM) and enterprise architecture elements. Additional elements can also be defined if required.
- Instructions: Structured way to conceptualize services.
- Standards: Provide well-defined, quality factors and best practices of service, capability, data and constraint granularity. Roles must be well-defined as well, and lay out whether it is a developer, architect or analyst who is responsible for each fraction of the work.
- Artifacts: Define what is not a good service - such as services that are not reusable - and therefore do not qualify as SOA residents.
- Quality of Service: Facilitates end-to-end modeling and provides comprehensive tool support.

The existing SOA modeling disciplines such as OOAD, EA frameworks, and BPM are not able to meet the requirements when applied independently to SOA applications. Thus, SOAD came into existence to ensure successful and full implementation of SOA applications. SOAD is a holistic modeling methodology that builds upon existing, well-disciplined and proven methodologies: OOAD, EA frameworks and BPM. In addition to this combination of proven methods, the following important concepts and aspects must also be considered in an SOAD approach:

- Service categorization and aggregation
- Policies and aspects
- Meet-in-the middle processes
- Semantic brokering
- Service harvesting and knowledge brokering

SOAD is applicable to many applications such as enterprise applications and architectural styles that are beyond SOA. In addition, current developments of the SOAD approach are also found in the reusable architectural decision model and cloud computing.

The main phases of SOAD are:

- Analysis and Modeling: This phase involves identifying the business and technical requirements, defining the service candidates, and modeling the service contracts and compositions. This phase can be further divided into two sub-phases: service-oriented analysis and service modeling. Service-oriented analysis focuses on identifying and defining the services that are relevant to the business domain and the application context. Service modeling focuses on designing the service contracts and compositions that specify the interface, behavior, and quality of service of each service.
- Design and Implementation: This phase involves designing and implementing the service logic, the service components, and the service infrastructure. This phase can be further divided into two sub-phases: service-oriented design and service implementation. Service-oriented design focuses on applying design principles and patterns to ensure that the services are loosely coupled, reusable, and interoperable. Service implementation focuses on developing the service logic and components using appropriate technologies and platforms, such as web services, REST services, and microservices.
- Testing and Deployment: This phase involves testing and deploying the services and the service compositions. This phase can be further divided into two sub-phases: service testing and service deployment. Service testing focuses on verifying and validating the functionality, performance, and reliability of the services and the service compositions. Service deployment focuses on deploying the services and the service compositions to the target environment, such as a cloud platform or a service registry.

The following table summarizes the main activities, artifacts, and roles involved in each phase of SOAD:

| Phase | Activity | Artifact | Role |
| --- | --- | --- | --- |
| Analysis and Modeling | Identify and define service candidates | Service inventory blueprint | Business analyst, domain expert, service analyst |
|  | Design service contracts and compositions | Service contract, service composition | Service designer, service architect |
| Design and Implementation | Apply design principles and patterns | Service-oriented design document | Service designer, service architect |
|  | Develop service logic and components | Service logic, service component | Service developer, service engineer |
| Testing and Deployment | Verify and validate service functionality, performance, and reliability | Service test plan, service test case, service test report | Service tester, service quality engineer |
|  | Deploy service and service compositions | Service deployment plan, service deployment report | Service deployer, service administrator |

Some of the advantages of SO