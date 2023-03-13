## Unit 10 - EA and SOA for Business and IT Alignment

The following diagram illustrates the basic architecture of a service-oriented enterprise that aligns business and IT using EA and SOA principles.

```
+-----------------------------------------------------------------+
|                                                                 |
|                       Enterprise Architecture                   |
|                                                                 |
| +-----------------+ +-----------------+ +-----------------+     |
| | Business        | | Information     | | Technology      |     |
| | Architecture    | | Architecture    | | Architecture    |     |
| |                 | |                 | |                 |     |
| | +-------------+ | | +-------------+ | | +-------------+ |     |
| | | Business    | | | | Data        | | | | Application | |     |
| | | Processes   | | | | Models      | | | | Services    | |     |
| | +-------------+ | | +-------------+ | | +-------------+ |     |
| |                 | |                 | |                 |     |
| | +-------------+ | | +-------------+ | | +-------------+ |     |
| | | Business    | | | | Information | | | | Infrastructure|     |
| | | Services    | | | | Services    | | | | Services    | |     |
| | +-------------+ | | +-------------+ | | +-------------+ |     |
| +-----------------+ +-----------------+ +-----------------+     |
|                                                                 |
+-----------------------------------------------------------------+
|                                                                 |
|                       Service Oriented Architecture             |
|                                                                 |
| +-----------------+ +-----------------+ +-----------------+     |
| | Business        | | Service         | | Service         |     |
| | Services Layer  | | Composition     | | Infrastructure  |     |
| |                 | | Layer           | | Layer           |     |
| | +-------------+ | | +-------------+ | | +-------------+ |     |
| | | Business    | | | | Composite   | | | | Service     | |     |
| | | Services    | | | | Services    | | | | Registry    | |     |
| | +-------------+ | | +-------------+ | | +-------------+ |     |
| |                 | |                 | |                 |     |
| | +-------------+ | | +-------------+ | | +-------------+ |     |
| | | Business    | | | | Service     | | | | Service     | |     |
| | | Processes   | | | | Orchestration| | | | Bus         | |     |
| | +-------------+ | | +-------------+ | | +-------------+ |     |
| +-----------------+ +-----------------+ +-----------------+     |
|                                                                 |
+-----------------------------------------------------------------+
```

The diagram shows how EA provides a framework that covers all the dimensions of IT architecture for the enterprise, and SOA provides an architectural strategy that uses the concept of “Services” as the underlining business-IT alignment entity . The diagram also shows how SOA governance begins with alignment to Business, IT, and EA governance, and how the governed SOA processes include planning, design, and operational aspects of SOA. The diagram also shows how the business services layer, the service composition layer, and the service infrastructure layer are the main components of SOA that enable the delivery of business-aligned services .