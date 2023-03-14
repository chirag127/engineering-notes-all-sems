The following is a detailed ascii diagram for Considerations for Service-oriented Applications for the notes of the Unit 3 - Service-Oriented Applications in the subject of Service Oriented Architecture.

```
+-----------------+     +-----------------+     +-----------------+
| Service         |     | Service         |     | Service         |
| Consumer        |     | Inventory       |     | Provider        |
|                 |     |                 |     |                 |
| - Requests      |     | - Contains      |     | - Exposes       |
|   services      |     |   reusable      |     |   services      |
|   using         |     |   and agnostic  |     |   using         |
|   standard      |     |   services      |     |   standard      |
|   protocols     |     | - Standardizes  |     |   protocols     |
| - Interacts     |     |   service data  |     | - Encapsulates  |
|   with services |     |   models        |     |   business      |
|   via loose     |     | - Provides      |     |   logic         |
|   coupling      |     |   service       |     | - Supports      |
| - Composes      |     |   governance    |     |   interoperability
|   services      |     |   and registry  |     | - Improves      |
|   to create     |     |                 |     |   agility and   |
|   applications  |     |                 |     |   scalability   |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
                             |
                             |
                             v
                    +-----------------+
                    | Service-Oriented|
                    | Architecture    |
                    |                 |
                    | - A type of     |
                    |   software      |
                    |   design that   |
                    |   makes         |
                    |   software      |
                    |   components    |
                    |   reusable and  |
                    |   interoperable |
                    |   via service   |
                    |   interfaces    |
                    | - A way to      |
                    |   leverage      |
                    |   legacy        |
                    |   infrastructure|
                    |   in new        |
                    |   markets       |
                    | - A way to      |
                    |   reduce costs  |
                    |   from greater  |
                    |   agility and   |
                    |   more          |
                    |   efficient     |
                    |   development   |
                    +-----------------+
```