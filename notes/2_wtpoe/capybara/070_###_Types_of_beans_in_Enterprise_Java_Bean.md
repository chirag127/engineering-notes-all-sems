### Types of beans in Enterprise Java Bean:

Enterprise Java Beans (EJB) are server-side components in Java EE that provide reusable business logic functionality. There are three types of EJBs:

1. Session Beans:
   - These beans are used to represent a single client session, providing a stateful or stateless behavior.
   - A stateful session bean maintains the state of a conversation with a client, whereas a stateless session bean does not.
   - Mnemonic: S for Session Beans, S for State (stateful/stateless)

2. Entity Beans:
   - These beans represent persistent data in a database and provide a way to interact with the data through the EJB container.
   - They are used to manage the life cycle of an entity, including creating, reading, updating, and deleting records from the database.
   - Mnemonic: E for Entity Beans, E for Entity (persistent data)

3. Message-Driven Beans:
   - These beans are used to process messages asynchronously in a Java Message Service (JMS) queue or topic.
   - They are triggered by incoming messages and perform a specified action in response.
   - Mnemonic: M for Message-Driven Beans, M for Message (asynchronous processing)

Advantages of using EJBs:
- EJBs provide encapsulation, allowing for modular and reusable code.
- They provide declarative transaction management, simplifying the implementation of transactional behavior.
- EJBs can be distributed across multiple servers, allowing for scalability and fault-tolerance.

Disadvantages of using EJBs:
- EJBs can be complex to develop and deploy, requiring a significant amount of configuration and setup.
- They can be slower than other alternatives due to the additional overhead of the EJB container.

Example code for a session bean:
```java
@Stateless
public class MySessionBean implements MySessionBeanRemote {
    public String sayHello() {
        return "Hello, World!";
    }
}
```

Example code for an entity bean:
```java
@Entity
public class Customer {
    @Id
    private Long id;
    private String name;
    // getters and setters
}
```

Example code for a message-driven bean:
```java
@MessageDriven(mappedName = "jms/myQueue")
public class MyMessageBean implements MessageListener {
    public void onMessage(Message message) {
        // process message
    }
}
```

Applications of EJBs:
- EJBs are commonly used in enterprise-level applications that require transactional behavior and scalability.
- They are particularly useful in applications that need to interact with a database or perform asynchronous processing.

Overall, understanding the different types of EJBs and their advantages and disadvantages can be useful for designing and implementing scalable and maintainable enterprise applications.