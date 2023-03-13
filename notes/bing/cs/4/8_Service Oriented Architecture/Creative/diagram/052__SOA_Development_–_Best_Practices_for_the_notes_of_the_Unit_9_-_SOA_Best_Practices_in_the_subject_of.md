The following diagram illustrates the basic architecture of a service-oriented architecture (SOA) development using best practices:

```
+-----------------+     +-----------------+     +-----------------+
| Business Layer  |     | Service Layer   |     | Data Layer      |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Business    | |     | | Service    | |     | | Data       | |
| | Process     | |     | | Contract   | |     | | Model      | |
| | Management  | |     | +-------------+ |     | +-------------+ |
| +-------------+ |     |                 |     |                 |
|                 |     | +-------------+ |     | +-------------+ |
| +-------------+ |     | | Service    | |     | | Data       | |
| | Business    | |     | | Implementation |     | | Access     | |
| | Rules       | |     | +-------------+ |     | +-------------+ |
| +-------------+ |     |                 |     |                 |
|                 |     | +-------------+ |     | +-------------+ |
| +-------------+ |     | | Service    | |     | | Data       | |
| | Business    | |     | | Registry   | |     | | Integration | |
| | Monitoring  | |     | +-------------+ |     | +-------------+ |
| +-------------+ |     |                 |     |                 |
|                 |     | +-------------+ |     | +-------------+ |
| +-------------+ |     | | Service    | |     | | Data       | |
| | Business    | |     | | Security   | |     | | Security   | |
| | Security    | |     | +-------------+ |     | +-------------+ |
| +-------------+ |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The business layer contains the components that define and execute the business logic and processes of the organization. It includes business process management, business rules, business monitoring and business security.

The service layer contains the components that expose and consume the services that implement the business logic and processes. It includes service contract, service implementation, service registry and service security.

The data layer contains the components that manage and access the data sources that are used by the services. It includes data model, data access, data integration and data security.

Some of the best practices for SOA development are:

- Start with a process that has been previously opened or standardized, and has clear business value and goals.
- Establish a center of excellence (CoE) to ensure consistency and governance of the SOA development life cycle.
- Define completeness of work within services, and avoid creating services that are too granular or too coarse-grained.
- Ensure quality assurance of the services, and use testing tools and frameworks that support SOA testing.
- Deliver substantial business value and measure the return on investment (ROI) of the SOA projects.
- Don't take interoperability for granted, and use common interface standards and protocols for the services.
- Balance performance and security of the services, and use appropriate techniques and tools to optimize and protect them.
- Promote service reusability and discoverability, and use a service registry to publish and find the available services.