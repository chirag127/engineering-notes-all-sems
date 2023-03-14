### SOA Methodology for Enterprise for the notes of the Unit 2 - Enterprise-Wide SOA in the subject of Service Oriented Architecture

- SOA (Service-Oriented Architecture) is an integration architectural style and an enterprise-wide concept that enables existing applications to be exposed over loosely-coupled interfaces, each corresponding to a business function, that enables applications in one part of an extended enterprise to reuse functionality in other applications.
- SOA defines a way to make software components reusable and interoperable via service interfaces. Services use common interface standards and an architectural pattern so they can be rapidly incorporated into new applications.
- SOA services embody the code and data required to execute a complete, discrete business function (e.g. checking a customer’s credit, calculating a monthly loan payment, or processing a mortgage application).
- SOA services are exposed using standard network protocols—such as SOAP (simple object access protocol)/HTTP or Restful HTTP (JSON/HTTP)—to send requests to read or change data.
- SOA services are controlled by service governance that manages the lifecycle, development, and publication of the services in a registry that enables developers to quickly find them and reuse them to assemble new applications or business processes.
- SOA services can be built from scratch but are often created by exposing functions from legacy systems of record as service interfaces.
- SOA represents an important stage in the evolution of application development and integration over the last few decades, as it reduces the complexity and duplication of point-to-point integration and promotes the alignment of business requirements and technology solutions.
- SOA is driven by the enterprise business drivers, such as strategy, competition, market forces, regulatory forces, and so on. They all combine to drive the business architecture (model) and to shape the measurement and feedback for enterprise-wide performance management.
- SOA is based on the business model, which is the representation of the business resources and processes that are required to meet enterprise operational, tactical, and strategic business goals. Having a business model is critical to the successful alignment of services with business goals and objectives, and consequently to the overall SOA implementation’s success.
- SOA is enabled by the semantic information model, which defines the common business information for a given enterprise (such as customer, agreement, etc.). These objects effectively create an ontology of the enterprise data by defining common concepts (and their content) that describe the operations of the enterprise. Using the semantic information model to define business service interfaces leads to the creation of semantically interoperable services — a semantic SOA.
- SOA is supported by other aspects, such as key performance indicators (KPIs) and portfolio rationalization. The KPIs enable quantitative assessment of the impact of SOA and allow business processes and services to be measured and optimized. Portfolio rationalization enables the enterprise to simplify and consolidate infrastructure, applications, and data, where SOA plays a leading role in the implementation of the consolidation activities.
- SOA is implemented by orchestrating business services, which are implemented as enterprise content, semantic messaging, or existing applications. Business services are composed from integration services, which are the basic building blocks of SOA. Integration services provide the functionality to connect, transform, route, and mediate messages between service providers and consumers.
- SOA is composed of business processes, which are the sequences of activities that produce a specific outcome for a particular customer or market. Business processes are defined by business performance optimization, which is the process of analyzing, monitoring, and improving the performance of business processes and services.

A possible mnemonic to remember the main elements of SOA is:

**S**ervices, **O**ntology, **A**lignment

**S**ervices: the reusable and interoperable components that execute business functions

**O**ntology: the common business information model that defines the concepts and data of the enterprise

**A**lignment: the connection between the business drivers, goals, processes, and services

A possible ascii diagram to illustrate the SOA architecture is:

```
+-----------------+     +-----------------+     +-----------------+
| Enterprise      |     | Business        |     | Semantic        |
| Business Drivers|     | Model           |     | Information     |
|                 |     |                 |     | Model           |
+-----------------+     +-----------------+     +-----------------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         V                      V                      V