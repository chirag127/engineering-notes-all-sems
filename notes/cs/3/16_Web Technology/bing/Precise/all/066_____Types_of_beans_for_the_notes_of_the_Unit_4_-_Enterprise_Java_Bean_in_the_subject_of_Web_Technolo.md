# Unit 4 - Enterprise Java Bean

### Types of beans

Enterprise Java Beans (EJB) is a server-side software element that encapsulates the business logic of an application. It is a specification for developing a distributed business application on the Java platform. There are three types of EJBs:

1. **Session Bean**: Session bean contains business logic that can be invoked by local, remote or webservice client. There are two types of session beans:
    - **Stateful session bean**: This type of bean maintains the state of the conversation between the client and the bean.
    - **Stateless session bean**: This type of bean does not maintain the state of the conversation between the client and the bean.
2. **Entity Bean**: Entity beans represent persistent data stored in a database. They provide an object-oriented view of the data and allow the data to be accessed and manipulated by the application.
3. **Message-Driven Bean**: Message-driven beans are used to process messages asynchronously. They act as a listener for a particular messaging type, such as JMS, and perform some action when a message is received.