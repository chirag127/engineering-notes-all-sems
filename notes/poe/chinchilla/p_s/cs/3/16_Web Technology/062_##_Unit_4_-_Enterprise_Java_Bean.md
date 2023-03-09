## Unit 4 - Enterprise Java Bean

Enterprise Java Bean (EJB) is a specification developed by Sun Microsystems (now Oracle) for building distributed applications using Java. EJB provides a framework for developing server-side components that can be deployed on any Java EE-compliant application server.

### Types of Enterprise Java Beans

There are three types of EJBs:

1. Session Beans: Session beans represent business logic that can be invoked by clients. They are lightweight and stateful or stateless. There are two types of session beans: stateless session beans and stateful session beans.

2. Message-Driven Beans: Message-driven beans are used for processing messages asynchronously. They are invoked when a message arrives on a message queue or a topic.

3. Entity Beans: Entity beans represent persistent data that is stored in a database. They are used for data management and can be either container-managed or bean-managed.

### Advantages of Enterprise Java Beans

1. EJBs provide a robust and scalable framework for developing distributed applications.

2. EJBs take care of transactions, security, and other low-level tasks, allowing developers to focus on business logic.

3. EJBs are portable and can be deployed on any Java EE-compliant application server.

4. EJBs support distributed transactions, making it possible to update data across multiple databases.

### Disadvantages of Enterprise Java Beans

1. EJBs can be complex and difficult to develop, requiring a steep learning curve.

2. EJBs can be resource-intensive, requiring a lot of memory and processing power.

3. EJBs can be slow to start up, which can impact application performance.

### Applications of Enterprise Java Beans

1. EJBs are widely used in enterprise applications for developing business logic and managing data.

2. EJBs are used in e-commerce applications for processing transactions and managing inventory.

3. EJBs are used in financial applications for managing transactions, processing payments, and generating reports.

### Example of Enterprise Java Beans

Here is an example of a stateless session bean that calculates the area of a circle:

```
@Stateless
public class CircleAreaBean implements CircleArea {
    public double calculateArea(double radius) {
        return Math.PI * radius * radius;
    }
}
```

In this example, the `CircleAreaBean` class is a stateless session bean that implements the `CircleArea` interface. The `calculateArea` method takes the radius of a circle as an argument and returns the area.