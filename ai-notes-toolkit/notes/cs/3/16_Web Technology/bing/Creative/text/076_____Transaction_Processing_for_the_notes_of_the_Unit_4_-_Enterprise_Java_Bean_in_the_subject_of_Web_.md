### Transaction Processing for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

- Transaction processing is the execution of a series of operations on a set of data, such as a database, in a reliable, consistent, and atomic manner.
- Atomicity means that either all the operations in a transaction are completed successfully, or none of them are, leaving the data in a consistent state.
- Enterprise JavaBeans (EJB) is a technology that supports distributed transactional component-based applications written in Java.
- EJB components are server-side business objects that encapsulate the business logic and data of an application.
- EJB components can participate in transactions that span multiple resources, such as databases, message queues, and web services, using the Java Transaction API (JTA) .
- JTA is a Java EE API that enables Java applications and application servers to perform distributed transactions across XA resources, which are resources that comply with the X/Open Distributed Transaction Processing (DTP) standard.
- JTA is based on the XA architecture, which uses a two-phase commit protocol to ensure atomicity and consistency of distributed transactions.
- EJB components can use either container-managed transactions (CMT) or bean-managed transactions (BMT) to control their transaction boundaries.
- In CMT, the EJB container is responsible for managing the transactions on behalf of the EJB components, based on the transaction attributes specified by the components or the deployment descriptors.
- In BMT, the EJB components are responsible for managing their own transactions, using the methods of the UserTransaction interface .
- CMT is the preferred approach for most EJB components, as it simplifies the development and maintenance of the components, and allows the container to optimize the transaction performance.
- BMT is useful for some advanced scenarios, such as when the EJB components need to access non-XA resources, or when they need to perform nested or multiple transactions in a single method .
- EJB components can also use the TransactionSynchronizationRegistry interface to access the transaction context and register synchronization callbacks that are invoked before and after the transaction completion .
- EJB components can also use the annotations @TransactionAttribute, @TransactionManagement, and @TransactionScoped to specify the transaction behavior and scope of the components or their methods .