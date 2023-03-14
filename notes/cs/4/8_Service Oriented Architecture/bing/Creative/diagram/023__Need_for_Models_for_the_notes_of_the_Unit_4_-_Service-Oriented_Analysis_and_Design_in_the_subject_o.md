The following is a possible diagram for the need for models in service-oriented analysis and design, based on the information from the search results. The diagram is drawn in ASCII art using markdown syntax.

### Need for Models

```
+-------------------+   +-------------------+   +-------------------+
| Business Analysis |-->| Service Analysis  |-->| Service Design    |
+-------------------+   +-------------------+   +-------------------+
| - Identify        |   | - Identify        |   | - Specify         |
|   business goals  |   |   service         |   |   service         |
| - Analyze         |   |   candidates      |   |   contracts       |
|   business        |   | - Model service   |   | - Design service  |
|   processes       |   |   compositions    |   |   logic           |
| - Define          |   | - Define service  |   | - Design service  |
|   business        |   |   requirements    |   |   architecture    |
|   requirements    |   | - Validate        |   | - Validate        |
| - Validate        |   |   service models  |   |   service design  |
|   business models |   +-------------------+   +-------------------+
+-------------------+             |                       |
                                  |                       |
                                  v                       v
                          +-------------------+   +-------------------+
                          | Service           |-->| Service           |
                          | Implementation    |   | Testing           |
                          +-------------------+   +-------------------+
                          | - Implement       |   | - Test service    |
                          |   service logic   |   |   functionality   |
                          | - Deploy service  |   | - Test service    |
                          |   components      |   |   quality         |
                          | - Register        |   | - Test service    |
                          |   service         |   |   interoperability|
                          |   contracts       |   | - Test service    |
                          +-------------------+   |   composition     |
                                                  +-------------------+
```