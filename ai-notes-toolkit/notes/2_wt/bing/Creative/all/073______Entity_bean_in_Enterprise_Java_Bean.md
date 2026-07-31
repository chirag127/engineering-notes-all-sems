#### Entity bean in Enterprise Java Bean

- An entity bean is a type of Enterprise JavaBean (EJB), which is a server-side Java EE component that encapsulates the business logic of an application .
- An entity bean represents persistent data maintained in a database . It can map to a table, a row, or a column in a relational database, or to a document, a collection, or a field in a NoSQL database.
- An entity bean can manage its own persistence (bean-managed persistence or BMP) or can delegate this function to its EJB container (container-managed persistence or CMP) .
- An entity bean is identified by a primary key, which is a unique value that distinguishes one entity bean instance from another .
- An entity bean can have local or remote interfaces, which define the methods that clients can invoke on the entity bean.
- An entity bean can also have a home interface, which defines the methods for creating, finding, and removing entity bean instances.
- An entity bean can be either session-aware or session-independent. A session-aware entity bean is associated with a specific client session and can maintain state across method invocations. A session-independent entity bean is not tied to any client session and does not maintain state.
- An entity bean can be either transaction-aware or transaction-independent. A transaction-aware entity bean participates in transactions that span multiple method invocations or multiple entity beans. A transaction-independent entity bean does not participate in transactions and performs each method invocation as a separate unit of work.

Some possible advantages of using entity beans are:

- They provide a high-level abstraction for accessing and manipulating persistent data, hiding the details of the underlying database.
- They can benefit from the services provided by the EJB container, such as security, concurrency, transaction management, caching, pooling, and lifecycle management.
- They can be reused across different applications and clients, reducing the development and maintenance costs.

Some possible disadvantages of using entity beans are:

- They can introduce performance overhead due to the extra layers of abstraction and communication between the entity bean and the database.
- They can be complex to design and implement, especially for bean-managed persistence, which requires the developer to write the SQL code for accessing the database.
- They can be less flexible and portable than other persistence technologies, such as Java Persistence API (JPA), which is a standard specification for object-relational mapping in Java EE .

Some possible mnemonics and learning tricks for entity beans are:

- Entity beans are like **entities** in a database, they represent persistent data and have a primary key .
- Entity beans can be either **BMP** or **CMP**, which stand for **bean-managed persistence** or **container-managed persistence**, depending on who is responsible for the persistence logic .
- Entity beans can have **local** or **remote** interfaces, which define the methods that clients can invoke on the entity beans.
- Entity beans can also have a **home** interface, which defines the methods for creating, finding, and removing entity bean instances.
- Entity beans can be either **session-aware** or **session-independent**, depending on whether they maintain state across method invocations or not.
- Entity beans can be either **transaction-aware** or **transaction-independent**, depending on whether they participate in transactions or not.

: https://en.wikipedia.org/wiki/Entity_Bean
: https://www.educba.com/entity-beans/
: https://stackoverflow.com/questions/40666486/what-is-the-difference-between-enterprise-java-beanejb-and-entity-java-bean
: https://en.wikipedia.org/wiki/Java_Persistence_API