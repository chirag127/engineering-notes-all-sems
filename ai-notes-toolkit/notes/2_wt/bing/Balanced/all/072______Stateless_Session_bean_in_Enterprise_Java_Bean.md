#### Stateless Session bean in Enterprise Java Bean

- A stateless session bean is a type of enterprise bean, which is normally used to perform independent operations .
- A stateless session bean does not have any associated client state, but it may preserve its instance state .
- A stateless session bean does not maintain a conversational state between multiple method calls by the container.
- A stateless session bean can be invoked by any client at any time.
- A stateless session bean is typically used for tasks that are atomic and idempotent.
- A stateless session bean is annotated with `@Stateless` or declared in the deployment descriptor.
- A stateless session bean implements a business interface that defines the methods available to the clients.
- A stateless session bean can access other enterprise beans, web services, and resources such as databases and JMS destinations.
- A stateless session bean can use dependency injection to obtain references to other beans and resources.
- A stateless session bean can be pooled and reused by the container to improve performance and scalability .
- A stateless session bean can implement lifecycle callback methods to perform initialization and cleanup tasks.

An example of a stateless session bean is:

```java
@Stateless
public class StatelessEJB implements StatelessEJBRemote {

    @Override
    public String sayHello(String name) {
        return "Hello " + name;
    }
}
```

An example of a client invoking a stateless session bean is:

```java
public class Client {

    @EJB
    private static StatelessEJBRemote statelessEJB;

    public static void main(String[] args) {
        System.out.println(statelessEJB.sayHello("Alice"));
        System.out.println(statelessEJB.sayHello("Bob"));
    }
}
```

The output of the client is:

```
Hello Alice
Hello Bob
```

Note that the stateless session bean does not remember the previous client or the previous method call.

Some possible mnemonics and learning tricks for stateless session bean are:

- Stateless session bean is like a calculator that performs operations without storing any memory or history.
- Stateless session bean is like a hotel receptionist that serves any customer without keeping track of their names or preferences.
- Stateless session bean is like a vending machine that dispenses items without remembering the previous transactions or customers.