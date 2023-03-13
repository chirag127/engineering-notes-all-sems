 Here is the content in markdown format for the topic ### Types of beans in Enterprise Java Bean:

### Types of beans in Enterprise Java Bean

The following are the major types of beans in Enterprise Java Bean (EJB):

1. Session Beans:

- Stateless Session Beans: They do not maintain conversational state. They are pooled and reused. Good for scalability.
- Stateful Session Beans: They maintain conversational state. Not pooled and reused. Each client has its own bean instance. Good for transactional operations spanning multiple method calls.

Mnemonics: Stateless beans are 'state-less', stateful beans 'have state'.

2. Message-Driven Beans: They are asynchronous message consumers. They get messages from JMS queues/topics and process them. They have no remote interfaces and are not exposed to clients directly.

3. Entity Beans: They map to the rows in a database table. They have their lifecycle tightly coupled to the database. There are 2 types:

- CMP (Container-Managed Persistence): The EJB container handles the persistence.
- BMP (Bean-Managed Persistence): The bean code handles the persistence using JDBC.

Entity Beans are rarely used now. JPQL and entities (from JPA) are preferred for database access.

Advantages of EJBs:

- Distributed computing: EJBs can be accessed from remote clients.
- Security: EJBs have declarative security via deployment descriptors.
- Transactions: EJBs can be part of JTA transactions.
- Scalability: Stateless Session Beans are pooled and reused.
- Portability: The EJB component is portable across vendors and application servers.

Disadvantages of EJBs:

- Verbosity: EJBs involve a lot of configuration and deployment descriptors.
- Performance overhead: Additional layers of abstraction impact performance.
- Vendor dependence: Although standardized, EJB implementations differ across vendors and versions. Migration/portability can be challenging.

[Include diagrams/codes/tables/examples if helpful]