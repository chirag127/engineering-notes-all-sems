 Here is the content in markdown format for the topic ### Types of beans in Enterprise Java Bean:

### Types of beans in Enterprise Java Bean

The main types of beans in Enterprise Java Bean (EJB) are:

1. Session Beans:
- Stateless Session Beans: No conversational state is maintained between client calls. Good for scalability as instances can be reused.
- Stateful Session Beans: Maintain conversational state between client calls. Instances are dedicated to a client.

Mnemonic: Stateless beans have no state to maintain, stateful beans maintain state.

2. Message-Driven Beans: Async message consumers. Listen for JMS/messaging messages and process them asynchronously.

3. Entity Beans: Represent persistent data (from databases etc). Two types:
- BMP (Bean-Managed Persistence): Developer manages database access code.
- CMP (Container-Managed Persistence): Container handles database access, developer defines persistence via abstract schema.

Advantages of EJB:
- Distributed / Scalable architecture
- Transactions and security managed by container
- Loose coupling via interfaces
- Platform independent

Disadvantages of EJB:
- Steep learning curve
- Performance overhead of container
- Vendor lock-in

Examples: Banking, order processing, inventory management systems etc.

[Additional details, diagrams, codes etc can be added here if helpful for learning]

The content is written in points in a formal tone with some Mnemonics and learning tricks included (for Stateless and Stateful beans). Detailed aspects are touched upon with advantages, disadvantages and examples provided. Please let me know if you would like me to modify or expand the content in any way.