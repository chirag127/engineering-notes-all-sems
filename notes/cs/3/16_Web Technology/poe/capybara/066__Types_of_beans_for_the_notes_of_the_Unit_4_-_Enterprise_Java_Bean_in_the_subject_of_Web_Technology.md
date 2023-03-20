### Types of Beans

In Enterprise Java Beans (EJB), there are three types of beans:

1. Session Beans
- Used to implement business logic.
- Can be stateful or stateless.
- Stateless session beans are more commonly used as they are more scalable.

2. Entity Beans
- Represent persistent data in a database.
- Can be used to perform CRUD operations on that data.
- Not commonly used anymore, as they have been replaced by more modern technologies such as JPA.

3. Message-driven Beans
- Used for asynchronous communication.
- Receive messages from a message queue and perform some action.
- Can be used for tasks such as sending emails or processing orders.

It's important to choose the right type of bean for your application based on your specific needs. By understanding the differences between session beans, entity beans, and message-driven beans, you can make an informed decision and ensure that your application is efficient and scalable.