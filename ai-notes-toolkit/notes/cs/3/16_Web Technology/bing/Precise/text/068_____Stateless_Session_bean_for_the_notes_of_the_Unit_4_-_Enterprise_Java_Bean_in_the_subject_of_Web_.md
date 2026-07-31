### Stateless Session Bean

- Stateless session beans are enterprise beans that do not maintain conversational state with clients.
- Each method invocation on a stateless bean is independent of any previous invocation.
- The container can choose to delegate the invocation to any available instance of the bean.
- Stateless session beans are typically used for implementing business logic that does not require maintaining state across method invocations.
- They can also be used for implementing web services, as they can handle multiple requests from multiple clients concurrently.
- Stateless session beans are relatively simple to develop and have a lower overhead compared to stateful session beans.
- They are typically used for implementing services that are short-lived and do not require conversational state.
- Stateless session beans can be accessed by multiple clients concurrently, and the container is responsible for managing the instances and ensuring thread safety.
- The lifecycle of a stateless session bean includes the following stages: creation, method invocation, and removal.
- During creation, the container instantiates the bean and injects any required resources.
- During method invocation, the container delegates client requests to an available instance of the bean.
- During removal, the container removes the bean instance from the pool and releases any resources associated with it.
