#### Stateless Session bean in Enterprise Java Bean

- A stateless session bean is a type of enterprise bean, which is normally used to perform independent operations .
- A stateless session bean does not have any associated client state, but it may preserve its instance state .
- A stateless session bean does not maintain a conversational state between multiple method calls by the container.
- A stateless session bean can be pooled and shared by multiple clients, and the container can create or destroy instances as needed.
- A stateless session bean is typically used for tasks that are short-lived, atomic, and idempotent.
- A stateless session bean is annotated with `@Stateless` or declared in the deployment descriptor with `<session-type>Stateless</session-type>` .
- A stateless session bean can implement a local, remote, or web service interface .
- A stateless session bean can access other enterprise beans, use the Java Persistence API, use the Java Transaction API, and use the Java Message Service API.

Example of a stateless session bean:

```java
// Annotate the bean with @Stateless
@Stateless
public class StatelessEJB {

    // Declare a business method
    public String sayHello(String name) {
        return "Hello " + name;
    }
}
```

Example of a client accessing a stateless session bean:

```java
// Inject the bean using the @EJB annotation
@EJB
private StatelessEJB statelessEJB;

// Call the business method
public String greet(String name) {
    return statelessEJB.sayHello(name);
}
```

Advantages of stateless session beans:

- They are easy to develop and use.
- They are scalable and efficient, as they do not require the container to maintain any state information.
- They are thread-safe, as they do not have any instance variables that can be modified by concurrent clients.

Disadvantages of stateless session beans:

- They cannot support conversational state or long-running transactions.
- They cannot use the `@PrePassivate` and `@PostActivate` lifecycle callbacks, as they are never passivated by the container.
- They cannot implement the `SessionSynchronization` interface, as they do not participate in session synchronization.

Mnemonics and learning tricks for stateless session beans:

- Remember that stateless session beans are **S**hort-lived, **S**tateless, **S**hared, and **S**calable.
- Remember that stateless session beans are annotated with `@Stateless` or declared as `<session-type>Stateless</session-type>`.
- Remember that stateless session beans can implement a **L**ocal, **R**emote, or **W**eb service interface.
- Remember that stateless session beans can access other **E**nterprise beans, use the **J**ava **P**ersistence API, use the **J**ava **T**ransaction API, and use the **J**ava **M**essage **S**ervice API.