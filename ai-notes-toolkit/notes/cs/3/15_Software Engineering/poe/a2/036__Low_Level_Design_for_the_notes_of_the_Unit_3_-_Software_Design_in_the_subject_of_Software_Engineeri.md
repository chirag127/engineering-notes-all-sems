 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Low Level Design for the notes of the Unit 3 - Software Design in the subject of Software Engineering

1. Define components: Identify major components of the system and their responsibilities. For example, for an online shopping system, major components would be:
- Product Catalog: Responsible for storing product information
- Shopping Cart: Responsible for storing products added by users
- Payment Gateway: Responsible for processing payments
- Order Processing: Responsible for processing and fulfilling orders

2. Define interfaces: Describe how the components will interact with each other. What inputs/outputs does each component expect? What protocols/formats will they use to communicate?
For example, the Product Catalog component may expose a REST API to retrieve product information. The Shopping Cart may use this REST API to fetch product details.

3. Allocate responsibilities: Which system will each component be part of? Where will each component be deployed? How will they scale? How will failures be handled?
For example, the Product Catalog may be part of a products microservice deployed on multiple servers. The Payment Gateway may be a third-party service. Order Processing may be part of an orders microservice with redundancy/failover.

4. Estimate volumes: Estimate volumes/throughput/loads for different parts of the system. For example, estimate number of products in catalog, number of add to cart events, number of checkout events, peak traffic volumes, etc. These estimates drive the sizing and scalability requirements.

5. Review and refine: Go through multiple iterations of reviewing the design and refining/improving it. Get feedback from colleagues and refine the design. Handle edge cases and failure scenarios.
The final design should be modular, scalable, robust, and handle failures gracefully. It should have well-defined interfaces and isolate components from each other.