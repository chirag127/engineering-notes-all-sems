 Here is the content in markdown format for the topic ### Types of beans for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology:

### Types of beans

The following are the types of beans used in EJB:

1. Session Beans:
- Used for containing business logic.
- Two types:
    - Stateless Session Bean: Does not maintain conversational state. Good for scalability as several instances can be created to handle requests.
    - Stateful Session Bean: Maintains conversational state. Good for workflows or transactions spanning multiple methods. State is maintained for a single client.
- Advantages: Encapsulation of business logic, transaction management, security, scalability, etc.
- Disadvantages: Can be complex to develop and test.

2. Message-driven Beans:
- Used to process messages asynchronously.
- Listen to JMS queues or topics.
- Do not maintain any state.
- Multiple instances can be created to handle messages concurrently.
- Advantages: Decouples message producers and consumers, scalability, asynchronous processing, etc.
- Disadvantages: Additional overhead of using JMS.

3. Entity Beans:
- Used to model data and map to a database.
- Two types:
    - BMP Entity Beans: Developer manages persistence.
    - CMP Entity Beans: Container manages persistence.
- Advantages: Object-relational mapping, transaction management, etc.
- Disadvantages: Complex to develop and inefficient in earlier versions of EJB. CMP entity beans are deprecated.

**Examples and diagrams can be included here for better understanding. The points can be explained in detail with examples and applications. The format can be made more formal by expanding on the sentences and rephrasing them.**