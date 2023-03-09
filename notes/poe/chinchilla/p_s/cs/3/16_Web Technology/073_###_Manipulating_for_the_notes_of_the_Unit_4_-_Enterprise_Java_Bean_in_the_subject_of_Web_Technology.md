### Manipulating for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

Enterprise Java Beans (EJB) is a server-side component architecture that enables developers to build scalable, distributed, and transactional applications. EJBs are used to encapsulate business logic and provide a seamless interface between the presentation layer and the database. Manipulating EJBs involves manipulating the state of the EJBs and their lifecycle.

#### Stateful and Stateless EJBs

EJBs can be either stateful or stateless, and it is essential to understand the differences between them when manipulating EJBs.

- **Stateful EJBs** are designed to maintain state information across multiple method invocations by the same client. A stateful EJB is created when a client requests it and is destroyed when the client no longer needs it. Stateful EJBs are useful when the client needs to maintain conversational state, such as in a shopping cart application.

- **Stateless EJBs** do not maintain state information across multiple method invocations by the same client. A new instance of a stateless EJB is created for each client request, and it is destroyed when the request is completed. Stateless EJBs are useful when the client only needs to execute a single transactional operation, such as submitting an order.

#### EJB Lifecycle

Manipulating EJBs involves understanding the EJB lifecycle, which consists of several stages:

1. **Instantiation:** EJBs are created by the EJB container when a client requests them.

2. **Dependency Injection:** The container injects any dependencies that the EJB requires.

3. **Initialization:** The EJB is initialized, and any setup tasks are performed.

4. **Method Invocation:** The client invokes the EJB's methods.

5. **Transaction Management:** The container manages the transactional behavior of the EJB.

6. **Passivation:** If the EJB is stateful and no longer needed, the container may passivate it to free up resources.

7. **Activation:** If the EJB is stateful and needed again, the container may activate it and restore its state.

8. **Removal:** When the client no longer needs the EJB, the container removes it.

#### EJB Annotations

Manipulating EJBs also involves using annotations to configure the EJBs and their behavior. Some essential annotations include:

- **@Stateful** and **@Stateless:** These annotations indicate whether an EJB is stateful or stateless.

- **@EJB:** This annotation is used to inject dependencies into an EJB.

- **@TransactionAttribute:** This annotation is used to specify the transactional behavior of an EJB's methods.

- **@PostConstruct** and **@PreDestroy:** These annotations are used to specify methods that should be executed during the initialization and removal stages of the EJB's lifecycle, respectively.

#### Examples of EJB Manipulation

Here are some examples of EJB manipulation:

- **Creating an EJB:** To create an EJB, you can use the `@Stateful` or `@Stateless` annotation to specify its type and use the `@EJB` annotation to inject any dependencies.

- **Configuring Transactional Behavior:** To configure the transactional behavior of an EJB's methods, you can use the `@TransactionAttribute` annotation to specify whether the method should be executed within a transaction or not.

- **Initializing an EJB:** To initialize an EJB, you can use the `@PostConstruct` annotation to specify a method that should be executed during the initialization stage of the EJB's lifecycle.

- **Passivating and Activating an EJB:** If an EJB is stateful and no longer needed, the container may passivate it to free up resources. To activate the EJB again, the container will restore its state. This process is transparent to the client.

#### Advantages and Disadvantages of EJBs

Here are some advantages and disadvantages of using EJBs:

##### Advantages

- EJBs provide a standardized approach to building server-side components, making it easier for developers to build distributed applications.

- EJBs provide a robust and scalable architecture that can handle high transaction volumes.

- EJBs provide built-in support for transaction management, security, and concurrency control.

##### Disadvantages

- EJBs can be complex and difficult to learn, requiring a significant amount of time and effort to master.

- EJBs can be heavyweight, requiring a lot of resources and memory to run.

- EJBs can be slow to start up, which can affect the performance of the application.

#### Applications of EJBs

Here are some applications of EJBs:

- EJBs are commonly used in enterprise-level applications that require high scalability and reliability.

- EJBs are often used in e-commerce applications, such as online shopping carts and payment processing systems.

- EJBs are used in banking and financial applications