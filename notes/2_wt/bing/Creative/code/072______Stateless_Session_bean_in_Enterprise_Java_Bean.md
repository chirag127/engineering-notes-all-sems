A stateless session bean is a type of enterprise bean that does not maintain any state between method invocations. It can be used to implement business logic that does not depend on the state of a specific client. A stateless session bean can be accessed by multiple clients concurrently.

To create a stateless session bean, you need to do the following steps:

1. Create a remote or local interface that defines the business methods of the bean. Annotate the interface with `@Remote` or `@Local` annotation.
2. Create a bean class that implements the interface and annotates it with `@Stateless` annotation. Optionally, you can specify a mapped name for the bean using the `mappedName` attribute of the annotation.
3. Implement the business methods of the bean. You can inject any resources or other beans using the `@Resource`, `@EJB`, `@Inject` or `@PersistenceContext` annotations.
4. Deploy the bean to an application server that supports EJB 3.0 or higher.
5. Access the bean from a client using JNDI lookup or dependency injection.

Here is an example of a stateless session bean that performs a simple addition operation:

#### Stateless Session bean in Enterprise Java Bean
```java
// Remote interface
package com.example;
import javax.ejb.Remote;
@Remote
public interface Adder {
    int add(int a, int b);
}

// Bean class
package com.example;
import javax.ejb.Stateless;
@Stateless(mappedName = "adder")
public class AdderBean implements Adder {
    public int add(int a, int b) {
        return a + b;
    }
}

// Client class
package com.example;
import javax.ejb.EJB;
public class Client {
    @EJB(mappedName = "adder")
    private static Adder adder;
    public static void main(String[] args) {
        int result = adder.add(10, 20);
        System.out.println("Result: " + result);
    }
}
```