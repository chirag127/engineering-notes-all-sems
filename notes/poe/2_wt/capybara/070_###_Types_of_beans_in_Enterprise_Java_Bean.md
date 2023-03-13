### Types of Beans in Enterprise Java Bean

Enterprise Java Bean (EJB) is a server-side software component that is used to develop large-scale, distributed, and transactional applications. EJBs are used to simplify the development of complex applications by providing a standard framework for building and deploying components.

There are three types of beans in EJB: 

1. Session Beans
2. Entity Beans
3. Message-Driven Beans

#### Session Beans

Session beans are used to represent a single client's interaction with an application. These beans are temporary and are created and destroyed for each client request. Session beans can be further divided into two categories:

- Stateful Session Beans: These beans maintain a conversational state with the client. They are created when a client requests a service and are destroyed when the conversation is complete.

- Stateless Session Beans: These beans do not maintain any conversational state with the client. They are created when a client requests a service and are destroyed when the service is complete.

#### Entity Beans

Entity beans represent persistent data in an application. They are used to represent data that needs to be stored in a database. Entity beans can be further divided into two categories:

- Container-Managed Persistence (CMP) Entity Beans: In CMP entity beans, the container is responsible for the persistence of the bean's data. The container automatically generates the SQL code to store and retrieve data from the database.

- Bean-Managed Persistence (BMP) Entity Beans: In BMP entity beans, the developer is responsible for writing the SQL code to store and retrieve data from the database.

#### Message-Driven Beans

Message-driven beans are used to process messages asynchronously. They are used in an application that needs to process a large number of messages.

#### Mnemonics and Learning Tricks

There are currently no widely-used mnemonics or learning tricks for remembering the different types of beans in EJB. However, it can be helpful to understand the purpose and functionality of each type of bean, and to see examples of each type in action.