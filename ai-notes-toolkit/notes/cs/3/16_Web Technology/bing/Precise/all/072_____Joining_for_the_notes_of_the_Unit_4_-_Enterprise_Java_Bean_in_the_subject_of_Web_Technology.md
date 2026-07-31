### Unit 4 - Enterprise Java Bean

Enterprise Java Beans (EJB) is a server-side component architecture for the Java Platform, Enterprise Edition (Java EE). EJB is used to simplify the development of large, distributed applications by providing a container-managed environment for components.

1. **Types of EJBs**: There are three types of EJBs: session beans, entity beans, and message-driven beans.
    - **Session beans** represent a single client inside the server and can be either stateful or stateless.
    - **Entity beans** represent persistent data and are used to manage data in a database.
    - **Message-driven beans** are used to process messages asynchronously.

2. **EJB Container**: The EJB container is responsible for managing the lifecycle of EJBs, providing services such as transaction management, security, and concurrency control.

3. **EJB Interfaces**: EJBs have two interfaces: the home interface and the remote interface. The home interface is used to create, find, and remove EJBs, while the remote interface is used to invoke business methods on the EJB.

4. **Deployment Descriptor**: The deployment descriptor is an XML file that contains information about the EJBs in an application, such as their types, interfaces, and security settings.

5. **EJB Transactions**: EJBs support container-managed transactions, which means that the container is responsible for managing transactions on behalf of the EJBs. EJBs can also use bean-managed transactions, where the bean is responsible for managing its own transactions.

6. **EJB Security**: EJBs support role-based security, where access to EJB methods is controlled based on the roles assigned to the user. The container is responsible for enforcing security constraints specified in the deployment descriptor.

7. **EJB QL**: EJB QL is a query language used to retrieve data from entity beans. It is similar to SQL, but is designed to be independent of the underlying database.

8. **EJB Best Practices**: Some best practices for using EJBs include using stateless session beans for better scalability, using message-driven beans for asynchronous processing, and using container-managed transactions for simpler transaction management.
