## Unit 4 - Enterprise Java Bean

Here is an example of an Enterprise Java Bean (EJB) code:

```java
import javax.ejb.Stateless;

@Stateless
public class ExampleBean {

    public String sayHello(String name) {
        return "Hello, " + name + "!";
    }
}
```

This is a simple example of a stateless session bean that has a method `sayHello` which takes a `String` parameter `name` and returns a greeting message. The `@Stateless` annotation indicates that this bean is a stateless session bean.
