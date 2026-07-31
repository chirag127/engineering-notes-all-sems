#### Stateless Session bean in Enterprise Java Bean

- A stateless session bean is a type of enterprise bean, which is normally used to perform independent operations .
- A stateless session bean does not have any associated client state, but it may preserve its instance state .
- A stateless session bean does not maintain a conversational state between multiple method calls by the container.
- A stateless session bean can be invoked by multiple clients concurrently.
- A stateless session bean is typically used for implementing business logic that does not depend on the state of a specific client.
- A stateless session bean is annotated with `@Stateless` or declared in the deployment descriptor with `<session-type>Stateless</session-type>`.
- A stateless session bean can implement a local, remote, or web service interface.
- A stateless session bean can inject other enterprise beans, resources, or services using the `@Inject` or `@Resource` annotations.
- A stateless session bean can access the `SessionContext` object using the `@Resource` annotation.
- A stateless session bean can use the `@PostConstruct` and `@PreDestroy` annotations to perform initialization and cleanup tasks.
- A stateless session bean can use the `@AroundInvoke` annotation to intercept method calls.
- A stateless session bean can use the `@Asynchronous` annotation to execute a method asynchronously.
- A stateless session bean can use the `@Schedule` or `@Schedules` annotations to create timer services.
- A stateless session bean can use the `@TransactionAttribute` annotation to specify the transaction attribute for a method.
- A stateless session bean can use the `@RolesAllowed`, `@PermitAll`, or `@DenyAll` annotations to specify the security roles for a method.

An example of a stateless session bean is:

```java
@Stateless
public class CalculatorBean implements Calculator {

    @Resource
    private SessionContext ctx;

    @PostConstruct
    public void init() {
        // perform initialization tasks
    }

    @PreDestroy
    public void destroy() {
        // perform cleanup tasks
    }

    @AroundInvoke
    public Object log(InvocationContext ic) throws Exception {
        // log the method invocation
        return ic.proceed();
    }

    @Asynchronous
    public Future<Integer> add(int a, int b) {
        // perform addition asynchronously
        return new AsyncResult<>(a + b);
    }

    @Schedule(second = "*/10", minute = "*", hour = "*")
    public void printTime() {
        // print the current time every 10 seconds
        System.out.println(new Date());
    }

    @TransactionAttribute(TransactionAttributeType.REQUIRED)
    public int subtract(int a, int b) {
        // perform subtraction in a transaction
        return a - b;
    }

    @RolesAllowed("admin")
    public int multiply(int a, int b) {
        // perform multiplication only for admin role
        return a * b;
    }

    @PermitAll
    public int divide(int a, int b) {
        // perform division for any role
        return a / b;
    }
}
```

Some advantages of stateless session beans are:

- They are easy to develop and maintain.
- They are scalable and can handle multiple requests concurrently.
- They do not consume memory or resources for storing client state.

Some disadvantages of stateless session beans are:

- They cannot support conversational state or long-running transactions.
- They cannot use the `@Remove` annotation to remove a bean instance.
- They cannot implement the `SessionSynchronization` interface to receive transaction notifications.