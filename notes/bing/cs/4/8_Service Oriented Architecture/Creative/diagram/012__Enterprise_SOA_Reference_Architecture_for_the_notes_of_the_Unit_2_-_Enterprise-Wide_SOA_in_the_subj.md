The following is a detailed ASCII diagram for Enterprise SOA Reference Architecture for the notes of the Unit 2 - Enterprise-Wide SOA in the subject of Service Oriented Architecture. The diagram is based on the SOA Reference Architecture from The Open Group  , which has nine layers representing nine key clusters of considerations and responsibilities that typically emerge in the process of designing an SOA solution or defining an enterprise architecture standard.

The diagram uses the following symbols:

- [ ] : A box represents a layer or a sub-layer of the SOA Reference Architecture.
- - : A horizontal line represents a boundary or a separation between layers or sub-layers.
- | : A vertical line represents a connection or a dependency between layers or sub-layers.
- / : A diagonal line represents a cross-cutting concern or a capability that spans across multiple layers or sub-layers.
- * : An asterisk represents a service or a component that belongs to a layer or a sub-layer.

The diagram is as follows:

```
[ Operational Systems Layer ]-----------------------------------------------------------------
|                                                                                           |
| * Data Sources * Applications * Devices * Legacy Systems * Cloud Services * Etc.         |
|                                                                                           |
[ Services Layer ]---------------------------------------------------------------------------
|                                                                                           |
| [ Business Services Sub-Layer ]-----------------------------------------------------------|
| |                                                                                       | |
| | * Business Processes * Business Rules * Business Events * Business Policies * Etc.   | |
| |                                                                                       | |
| [ Application Services Sub-Layer ]--------------------------------------------------------|
| |                                                                                       | |
| | * Application Logic * Application Data * Application Integration * Etc.              | |
| |                                                                                       | |
| [ Infrastructure Services Sub-Layer ]-----------------------------------------------------|
| |                                                                                       | |
| | * Security * Messaging * Transactions * Caching * Logging * Etc.                     | |
| |                                                                                       | |
[ Service Consumer Layer ]-------------------------------------------------------------------
|                                                                                           |
| * Portals * Web Applications * Mobile Applications * Desktop Applications * Etc.         |
|                                                                                           |
[ Service Composition Layer ]----------------------------------------------------------------
|                                                                                           |
| * Orchestration * Choreography * Mediation * Routing * Transformation * Etc.             |
|                                                                                           |
[ Service Exposure Layer ]-------------------------------------------------------------------
|                                                                                           |
| * Service Registry * Service Repository * Service Contract * Service Policy * Etc.       |
|                                                                                           |
[ Service Governance Layer ]-----------------------------------------------------------------
|                                                                                           |
| * Governance Processes * Governance Standards * Governance Tools * Governance Roles * Etc.|
|                                                                                           |
[ Quality of Service Layer ]-----------------------------------------------------------------
|                                                                                           |
| * Availability * Reliability * Performance * Scalability * Interoperability * Etc.       |
|                                                                                           |
[ Integration Layer ]------------------------------------------------------------------------
|                                                                                           |
| * Enterprise Service Bus * Adapters * Connectors * Protocols * Formats * Etc.            |
|                                                                                           |
[ Cross-Cutting Capabilities ]---------------------------------------------------------------
|                                                                                           |
| / Monitoring / Management / Testing / Auditing / Metering / Billing / Etc.               |
|                                                                                           |
---------------------------------------------------------------------------------------------
```