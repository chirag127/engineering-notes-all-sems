 Here is the content in markdown format for Unit 4 - Enterprise Java Bean:

## Unit 4 - Enterprise Java Bean

**Enterprise JavaBeans (EJB)** are server-side software components that encapsulate business logic. They are typically used to implement transactional business logic for Java EE applications.

Some key points about EJBs:

- EJBs are scalable, secure and robust enterprise components.
- They follow a component architecture with container-managed lifecycle and resources.
- They support transactions and security through declarative deployment metadata.
- The EJB container provides services such as life cycle management, threading, remoting, transactions, etc. to the enterprise beans.
- There are 3 main types of EJBs:

1. Session Beans - Used for task/business processing. There are two types: Stateless session beans (do not maintain conversational state) and stateful session beans (maintain conversational state).
2. Message-driven beans - Used for asynchronous processing (listening for JMS messages).
3. Entity Beans - Used to represent data/records in a database. Now replaced by JPA entities.

**Advantages of EJBs:**

- Loose coupling - EJBs are loosely coupled through interfaces.
- Container-managed services - The EJB container provides key services to the enterprise beans.
- Scalability - EJB applications can be scaled by simply adding more servers in the cluster.
- Security - EJB supports authentication, authorization, and other security features.
- Transactions - EJBs can participate in transactions that ensures data integrity.
- Remoting - EJBs can be accessed from remote clients using RMI or web services.

**Disadvantages of EJBs:**

- Can be complex to develop and configure.
- Can affect performance if misused.
- Vendor lock-in - EJBs are Java EE technology so you are locked into the Java EE ecosystem.

**Mnemonics/Learning tricks:**

- **SCC** - **S**ession, **C**allback (message-driven), **C**ontainer (entity) beans
- **CREAM** - **C**onversion, **R**emoting, **E**nterprise services (security, transactions), **A**synchronous processing (message-driven beans), **M**anagement/monitoring (through JMX)

**Examples/Use cases:**

- E-commerce website - Use session beans to handle shopping cart/checkout. Use entity beans/JPA to model products and orders. Use message-driven beans for sending order confirmation emails.
- Banking system - Use session beans for transfer funds, apply for loans, etc. Use entity beans/JPA for accounts and transactions. Use message-driven beans to monitor high-value transfers and trigger alerts.