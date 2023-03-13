The following is a detailed ASCII diagram for Enterprise Architecture for the notes of the Unit 10 - EA and SOA for Business and IT Alignment in the subject of Service Oriented Architecture. The diagram is based on the information from the web search results and is not intended to be a definitive or authoritative representation of the topic.

The diagram shows the four layers of EA: Business, Application, Data, and Technology. Each layer consists of various components that are related to each other and to the other layers. The diagram also shows how SOA can be applied to each layer to enable business-IT alignment, integration, and agility. SOA is an architectural strategy that uses the concept of services as the underlining business-IT alignment entity. Services are reusable, loosely coupled, and standards-based components that provide specific functionality or data to the consumers.

The diagram uses the following symbols and conventions:

- [ ] : A box represents a component or a sub-layer within a layer.
- - : A horizontal line represents a relationship or a dependency between components or sub-layers.
- | : A vertical line represents a hierarchy or a grouping of components or sub-layers.
- / : A diagonal line represents a cross-cutting concern or a shared service that spans across multiple layers or components.
- * : An asterisk represents a service or a service-oriented component that provides or consumes functionality or data.

The diagram is as follows:

```
+-----------------------------------------------------------------------------+
|                                 Business Layer                              |
+-----------------------------------------------------------------------------+
|                                                                             |
| [ Business Strategy ] - [ Business Goals ] - [ Business Processes ]        |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
| [ Business Services* ] - [ Business Rules ] - [ Business Events ]          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
+-----------------------------------------------------------------------------+
|                                 Application Layer                           |
+-----------------------------------------------------------------------------+
|                                                                             |
| [ Application Services* ] - [ Application Components ]                     |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
| [ Application Integration Services* ] - [ Application Integration Patterns ]|
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
+-----------------------------------------------------------------------------+
|                                  Data Layer                                 |
+-----------------------------------------------------------------------------+
|                                                                             |
| [ Data Services* ] - [ Data Sources ]                                      |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
| [ Data Integration Services* ] - [ Data Integration Patterns ]              |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
| [ Data Quality Services* ] - [ Data Quality Rules ]                         |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
+-----------------------------------------------------------------------------+
|                                 Technology Layer                            |
+-----------------------------------------------------------------------------+
|                                                                             |
| [ Infrastructure Services* ] - [ Infrastructure Components ]                |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
| [ Security Services* ] - [ Security Policies ]                             |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
| [ Governance Services* ] - [ Governance Policies ]                          |
|    |                      |                      |                          |
|    |                      |                      |                          |
|    |                      |                      |