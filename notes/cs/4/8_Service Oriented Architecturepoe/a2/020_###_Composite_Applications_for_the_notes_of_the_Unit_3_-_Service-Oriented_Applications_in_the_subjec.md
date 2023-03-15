 Here is the content in markdown format:

### Composite Applications for the notes of the Unit 3 - Service-Oriented Applications in the subject of Service Oriented Architecture

- Composite Applications are applications that are assembled from existing services. They are built by aggregating multiple services together.
- The services that are aggregated could be both internal services developed within the organization or external services available over the network (internet).
- The aggregation is done using a composition mechanism consisting of software components that implement a workflow or business process.
- The composite application appears to the user as a single, unified application. However, it is actually built from distributed, discrete software components (services) that are accessed over a network.
- Advantages:
-- Increased reuse of services. The composite application reuses existing services rather than building everything from scratch.
-- Flexibility. The workflow in a composite application can be reconfigured by changing the composition of services and the flow between them.
-- Maintainability. Changes to individual services do not affect the composite application, as long as the interface to the service remains unchanged.
- Disadvantages:
-- Complexity. There is added complexity in designing, developing, deploying and managing composite applications built from multiple distributed services.
-- Latency. There may be delays in service execution and data transfer between the services that make up the composite application.
-- Reliability. The composite application depends on the reliability and availability of the underlying services. If a service is down, it affects the composite application.
- Examples: Travel planning applications, e-commerce shopping cart applications, business process management systems.
- To remember: COMpOSITE appLICaTION uses exisTING services; aggreGATES services; appears as SINGLE app.