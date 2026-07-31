#### Stateful Session bean in Enterprise Java Bean
A stateful session bean is a type of enterprise bean that maintains conversational state with the client. Here is an example of a stateful session bean:

```java
import javax.ejb.Stateful;

@Stateful
public class ExampleStatefulBean {
    private int counter = 0;

    public void incrementCounter() {
        counter++;
    }

    public int getCounter() {
        return counter;
    }
}
```

This bean maintains a counter that can be incremented and retrieved by the client. The `@Stateful` annotation indicates that this is a stateful session bean. The state of the bean is maintained across multiple method invocations by the same client.