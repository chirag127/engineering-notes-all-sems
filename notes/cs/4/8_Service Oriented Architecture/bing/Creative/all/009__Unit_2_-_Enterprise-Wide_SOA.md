## Unit 2 - Enterprise-Wide SOA

- Service Oriented Architecture (SOA) is an enterprise-wide approach to software development of application components that takes advantage of reusable software components, or services .
- Each service in SOA is comprised of the code and data integrations required to execute a specific business function, such as checking a customer’s credit, signing into a website or processing a mortgage application.
- The service interfaces provide loose coupling, which means that they can be called with little or no knowledge of how the integration is implemented underneath, reducing the dependencies between applications.
- The service interfaces are frequently defined using Web Service Definition Language (WSDL), which is a standard tag structure based on XML (extensible markup language).
- The services are exposed using standard network protocols, such as SOAP (simple object access protocol)/HTTP or Restful HTTP (JSON/HTTP), to send requests to read or change data.
- Service governance controls the lifecycle for development and at the appropriate stage the services are published in a registry that enables developers to quickly find them and reuse them to assemble new applications or business processes.
- SOA enables existing applications to be exposed over loosely-coupled interfaces, each corresponding to a business function, that enables applications in one part of an extended enterprise to reuse functionality in other applications.
- SOA provides four different service types:
  - Functional services (i.e., business services), which are critical for business applications.
  - Enterprise services, which serve to implement functionality that is common across the enterprise, such as security, logging, or auditing.
  - Application services, which provide access to specific application functions, such as CRM, ERP, or SCM.
  - Infrastructure services, which provide low-level technical capabilities, such as messaging, caching, or persistence.
- SOA is an integration architectural style and an enterprise-wide concept. It enables existing applications to be exposed over loosely-coupled interfaces, each corresponding to a business function, that enables applications in one part of an extended enterprise to reuse functionality in other applications.
- SOA is different from a traditional, monolithic architecture in that every service has its own responsibility and can be independently deployed, scaled, and updated.
- SOA is also different from a more recent microservices architecture, which operates at a smaller scope and focuses on building applications as a collection of small, autonomous, and loosely-coupled services.
- SOA emerged in the late 1990s and represents an important stage in the evolution of application development and integration over the last few decades.
- SOA has several benefits, such as :
  - Increased agility and flexibility, as services can be easily composed and recomposed to meet changing business needs and customer expectations.
  - Improved reuse and reduced duplication, as services can be shared and leveraged across multiple applications and domains.
  - Enhanced interoperability and compatibility, as services can communicate using standard protocols and formats, regardless of the underlying technologies and platforms.
  - Reduced complexity and maintenance costs, as services can be independently developed, tested, deployed, and updated, without affecting the rest of the system.
  - Improved scalability and performance, as services can be distributed and load-balanced across multiple servers and locations, and scaled up or down as needed.
- SOA also has some challenges, such as :
  - Increased network traffic and latency, as services communicate over the network, which can affect the response time and reliability of the system.
  - Increased testing and debugging difficulties, as services are distributed and interdependent, which can make it hard to isolate and identify the root cause of errors and failures.
  - Increased governance and management overhead, as services need to be properly designed, documented, registered, monitored, and controlled, to ensure quality, consistency, and security.
  - Increased organizational and cultural changes, as services require a shift in mindset and collaboration, from a siloed and hierarchical approach to a cross-functional and service-oriented one.

A possible mnemonic to remember the four service types in SOA is:

**F**or **E**very **A**pplication, **I**nfrastructure

Functional, Enterprise, Application, Infrastructure