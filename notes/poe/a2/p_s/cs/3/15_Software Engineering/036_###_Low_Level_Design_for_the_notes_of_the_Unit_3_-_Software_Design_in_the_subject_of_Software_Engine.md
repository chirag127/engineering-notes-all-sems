 Here is the content in markdown format for the given topic:

### Low Level Design for the notes of the Unit 3 - Software Design in the subject of Software Engineering

Low level design refers to the detailed design of modules, interfaces, and data structures that are required to implement the high level design of a software system. It focuses on decomposing the system into smaller modules, defining the responsibilities and interactions between modules.

Some key points to cover in low level design are:

- Identify major modules and components and their responsibilities. For e.g. in an e-commerce application, major modules could be product catalog, cart, checkout, order management, etc.
- Define interfaces and interactions between modules. For e.g. the cart module may interact with product catalog to retrieve product information and with checkout module to initiate checkout process.
- Refine data model for major entities and data flows between modules. For e.g. product data may flow from product catalog to cart module, order and payment data may flow between checkout and order management modules.
- Estimate resource requirements and performance constraints for individual modules as well as overall system. For e.g. the product catalog may need to support high read throughput, the checkout module may need to support spikes in traffic during sales.
- Evaluate alternatives for major design decisions and their tradeoffs. For e.g. choosing a relational database vs NoSQL database for product catalog, synchronous vs asynchronous interactions between modules, etc.

Advantages of low level design:
- Provides concrete plan to implement the system.
- Identifies and resolves architectural and modularization issues early on.
- Enables estimating efforts and resource requirements more accurately.
- Facilitates discussion and reviews with team members and stakeholders.

Examples of low level design:
- Sequence diagrams to model interactions between modules.
- Class diagrams to model internal structure of major modules.
- Data flow diagrams to model flow of data between modules.

[Include additional details and diagrams if required to explain the concepts]