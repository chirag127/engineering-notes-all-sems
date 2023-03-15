### Unit 4 - Enterprise Java Bean

#### Types of beans

Enterprise Java Beans (EJB) is a server-side software element that encapsulates the business logic of an application. It is a specification for developing a distributed business application on the Java platform. There are three types of EJBs:

1. **Session Bean**: Session bean contains business logic that can be invoked by local, remote or webservice client. There are two types of session beans: Stateful session bean and Stateless session bean.
2. **Entity Bean**: An enterprise bean that represents persistent data maintained in a database. An entity bean can manage its own persistence or it can delegate this function to its container.
3. **Message-Driven Bean**: A message-driven bean is an enterprise bean that allows Java EE applications to process messages asynchronously. It acts as a JMS message listener, which is similar to an event listener except that it receives messages instead of events.