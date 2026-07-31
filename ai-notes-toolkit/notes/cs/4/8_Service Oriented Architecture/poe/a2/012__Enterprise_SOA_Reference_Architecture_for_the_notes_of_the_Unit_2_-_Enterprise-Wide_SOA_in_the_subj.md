 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Enterprise SOA Reference Architecture

1. Service registry: Stores information about all services in the SOA including their interfaces and locations. This allows services to be discovered and accessed dynamically.
2. Service broker: Routes requests to appropriate services based on business rules and policies. It can handle load balancing, authentication, and transformation if necessary.
3. Service gateway: Acts as a single entry point to the SOA. It can handle cross-cutting concerns for all services including authentication, monitoring, logging, load balancing, and protocol translation.
4. Services: Individual business functions exposed as services that can be accessed via standard mechanisms. They are self-contained and handle a single business task.
5. Operational management: Includes components to manage governance, security, logging, monitoring, configuration, and deployment of services.
6. Legacy systems: Existing systems are exposed as services or their functionality is reimplemented as services. This enables integration of new SOA capabilities with existing systems.

The above reference architecture shows the major components that would be present in an enterprise SOA. The service registry and service gateway provide mechanisms for service discovery and a single point of access respectively. The service broker allows for mediation between services. Operational management capabilities are required to ensure the SOA can be properly administered. And services would expose business functions needed in the organization, which could include new services or wrappers around legacy systems.