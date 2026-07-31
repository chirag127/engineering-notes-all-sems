## Unit 4 - Enterprise Java Bean

- Enterprise Java Bean (EJB) is a technology for developing scalable, robust and secure enterprise applications in Java.
- EJB is a server-side component that encapsulates the business logic of an application and provides middleware services such as security, transaction management, concurrency, persistence, etc.
- EJB runs inside an EJB container, which is a part of a Java EE application server, such as WildFly, WebLogic, GlassFish, etc.
- EJB has three main types: session beans, entity beans and message-driven beans.

### Session Beans
- Session beans are used to perform operations for a client, such as calculations, database access, business rules, etc.
- Session beans are short-lived and do not persist data across invocations.
- Session beans can be stateless or stateful.
- Stateless session beans do not maintain any conversational state with the client and can be reused by different clients.
- Stateful session beans maintain a conversational state with the client and are dedicated to a single client.
- Session beans are annotated with `@Stateless` or `@Stateful` and implement a business interface.

### Entity Beans
- Entity beans are used to represent persistent data in a relational database, such as customers, orders, products, etc.
- Entity beans are long-lived and can be shared by multiple clients.
- Entity beans can be container-managed or bean-managed.
- Container-managed entity beans delegate the persistence operations to the EJB container, which uses the Java Persistence API (JPA) to map the entity beans to the database tables.
- Bean-managed entity beans implement the persistence operations by themselves, using JDBC or other APIs.
- Entity beans are annotated with `@Entity` and have a primary key attribute.

### Message-Driven Beans
- Message-driven beans are used to process asynchronous messages from a message queue or a topic, such as orders, invoices, notifications, etc.
- Message-driven beans are stateless and do not persist data across invocations.
- Message-driven beans implement the `javax.jms.MessageListener` interface and are annotated with `@MessageDriven`.
- Message-driven beans receive messages from a message destination, which is configured by the `@ActivationConfigProperty` annotation.

### Example
- The following code shows a simple example of an EJB application, which consists of a stateless session bean, an entity bean and a message-driven bean.

```java
// A stateless session bean that performs a calculation
@Stateless
public class CalculatorBean implements Calculator {

    @Override
    public int add(int a, int b) {
        return a + b;
    }
}

// A business interface for the session bean
public interface Calculator {
    int add(int a, int b);
}

// An entity bean that represents a product
@Entity
public class Product {

    @Id
    private int id;
    private String name;
    private double price;

    // getters and setters
}

// A message-driven bean that receives orders
@MessageDriven(activationConfig = {
    @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Queue"),
    @ActivationConfigProperty(propertyName = "destination", propertyValue = "OrderQueue")
})
public class OrderProcessorBean implements MessageListener {

    @PersistenceContext
    private EntityManager em;

    @Override
    public void onMessage(Message message) {
        try {
            // extract the order details from the message
            ObjectMessage objectMessage = (ObjectMessage) message;
            Order order = (Order) objectMessage.getObject();

            // process the order
            for (OrderItem item : order.getItems()) {
                // find the product by id
                Product product = em.find(Product.class, item.getProductId());

                // update the product quantity
                product.setQuantity(product.getQuantity() - item.getQuantity());
            }

            // send a confirmation message
            System.out.println("Order processed: " + order.getId());
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
}
```

### Mnemonics and Learning Tricks
- To remember the three types of EJB, you can use the acronym SEM: Session, Entity, Message-driven.
- To remember the difference between stateless and stateful session beans, you can use the analogy of a hotel: a stateless session bean is like a hotel room that can be occupied by any guest, while a stateful session bean is like a hotel room that is reserved for a specific guest.
- To remember the difference between container-managed and bean-managed entity beans, you can use the analogy of a