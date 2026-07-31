#### Stateless Session bean in Enterprise Java Bean

A stateless session bean is a type of enterprise bean that implements business logic without maintaining any state related to a specific client. It can be invoked by multiple clients concurrently, and the container can pool and reuse the bean instances to improve performance.

To create a stateless session bean, you need to follow these steps:

1. Create a remote or local interface that defines the business methods of the bean. Annotate the interface with `@Remote` or `@Local` annotation.
2. Create a bean class that implements the interface and the business logic. Annotate the class with `@Stateless` annotation and optionally specify a mapped name for the bean.
3. Optionally, you can also use dependency injection to access other resources or beans from the bean class, such as `@EJB`, `@Resource`, `@PersistenceContext`, etc.
4. Deploy the bean class and the interface to the application server, such as GlassFish, JBoss, etc.
5. Create a client application that looks up and invokes the bean using the JNDI name or the mapped name of the bean.

Here is an example of a stateless session bean that performs a simple addition operation:

```java
// The remote interface
package com.javatpoint;
import javax.ejb.Remote;
@Remote
public interface AdderImplRemote {
    int add (int a,int b);
}

// The bean class
package com.javatpoint;
import javax.ejb.Stateless;
@Stateless(mappedName="st1")
public class AdderImpl implements AdderImplRemote{
    public int add(int a,int b){
        return a+b;
    }
}

// The client application
package com.javatpoint;
import javax.naming.InitialContext;
public class Client {
    public static void main(String[] args) {
        try {
            // Look up the bean using the mapped name
            AdderImplRemote remote=(AdderImplRemote)new InitialContext().lookup("st1");
            // Invoke the add method
            System.out.println(remote.add(10,20));
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```