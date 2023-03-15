 Here is the content in markdown format for the topic ### Patterns for SOA for the notes of the Unit 3 - Service-Oriented Applications in the subject of Service Oriented Architecture:

## Patterns for SOA

The following are some common patterns used in SOA:

### Service Façade:
- A single interface that provides simplified access to a set of services.
- Acts as an entry point into a set of services.
- Hides the complexity of underlying services.
- Example: A shopping cart service can act as a façade to product, pricing and payment services.

Advantages:
- Simplifies access to a set of services.
- Decouples service consumers from underlying services.

Disadvantages:
- May introduce additional latency.
- May obscure access to individual services.

### Service Composition:
- Combining multiple services into a new composite service.
- The composite service orchestrates the constituent services to achieve a goal.
- Example: A travel planning service can compose flight, hotel and car rental services.

Advantages:
- Reuses existing services to build new functionality.
- Delivers higher-level business functions.

Disadvantages:
- May impact performance if communication overhead is significant.
- Implementing error handling and compensation logic can be complex.

### Service Aggregation:
- Provide a single service interface to multiple underlying services that offer similar/overlapping functionality.
- The aggregated service determines which underlying service to invoke based on criteria such as load, location, etc.
- Example: A product information service can aggregate data from multiple product data sources.

Advantages:
- Presents a unified interface to clients.
- Allows scaling/load balancing across multiple services.

Disadvantages:
- May require complex logic to route requests to appropriate services.
- Underlying services must have consistent interfaces and data.

[Detailed diagrams, code examples and more points can be added here if required.]