### Service-oriented Analysis and Design (SOAD) Process for the notes of the Unit 2 - Enterprise-Wide SOA in the subject of Service Oriented Architecture

- Service-oriented analysis and design (SOAD) is a methodology that refers to the modeling and design for service-oriented architecture (SOA) applications.
- SOAD aims to develop highly adaptable and reusable services that can meet the requirements of various potential clients and contexts.
- SOAD builds upon existing, well-disciplined and proven methodologies such as object-oriented analysis and design (OOAD), enterprise architecture frameworks and business process modeling (BPM).
- SOAD also considers the following important concepts and aspects:
  - Service categorization and aggregation: grouping and organizing services based on their functionality, granularity, quality and dependencies.
  - Policies and aspects: defining the non-functional requirements and cross-cutting concerns of services, such as security, reliability, performance, etc.
  - Meet-in-the middle processes: aligning the top-down and bottom-up approaches of service identification and specification, by using both business goals and existing assets as inputs.
  - Semantic brokering: resolving the semantic mismatches and interoperability issues among services, by using ontologies, vocabularies and mappings.
  - Service harvesting and knowledge brokering: discovering and reusing existing services and knowledge sources, by using registries, repositories and recommendation systems.
- SOAD is applicable to many applications and architectural styles that are beyond SOA, such as cloud computing and microservices.
- SOAD involves the following key elements:
  - Process model: defining the process and notation by orchestrating OOAD, BPM and enterprise architecture elements. Additional elements can also be defined if required.
  - Instructions: providing a structured way to conceptualize services, by using techniques such as service identification, specification, realization and testing.
  - Standards: providing well-defined quality factors and best practices of service, capability, data and constraint granularity. Roles must also be well-defined, and specify whether it is a developer, architect or analyst who is responsible for each fraction of the work.
  - Artifacts: defining what is not a good service, such as services that are not reusable, and therefore do not qualify as SOA residents.
  - Quality of service: facilitating end-to-end modeling and providing comprehensive tool support.
- A possible mnemonic to remember the key elements of SOAD is **PISAQ** (Process model, Instructions, Standards, Artifacts, Quality of service).
- A possible mnemonic to remember the important concepts and aspects of SOAD is **SCAMPS** (Service categorization and aggregation, Policies and aspects, Meet-in-the middle processes, Semantic brokering, Service harvesting and knowledge brokering).
- An example of a SOAD process model is shown below:

```
+-----------------+     +-----------------+     +-----------------+
| Business Goals  |     | Business Process|     | Service Model   |
| and Strategies  |     | Modeling        |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-----------------+     +-----------------+     +-----------------+
| Service         |     | Service         |     | Service         |
| Identification  |     | Specification   |     | Realization     |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-----------------+     +-----------------+     +-----------------+
| Service         |     | Service         |     | Service         |
| Testing         |     | Deployment      |     | Monitoring      |
+-----------------+     +-----------------+     +-----------------+
```