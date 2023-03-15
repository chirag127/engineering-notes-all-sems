#### Stateless Session bean in Enterprise Java Bean
A Stateless Session Bean is a type of Enterprise Java Bean (EJB) that does not maintain conversational state with the client. Here is an example of a Stateless Session Bean:

```java
import javax.ejb.Stateless;

@Stateless
public class MyStatelessBean implements MyStatelessBeanRemote {
    public MyStatelessBean() {}

    public String myMethod() {
        // business logic here
        return "result";
    }
}
```

This bean is annotated with `@Stateless` to indicate that it is a Stateless Session Bean. The business logic is implemented in the `myMethod()` method. This bean can be accessed remotely through the `MyStatelessBeanRemote` interface.