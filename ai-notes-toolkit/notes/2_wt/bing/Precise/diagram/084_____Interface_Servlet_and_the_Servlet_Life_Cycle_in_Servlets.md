### Interface Servlet and the Servlet Life Cycle in Servlets

Here is an ASCII diagram that illustrates the Servlet Life Cycle in Servlets:

```
 +----------------+
 | Web Container  |
 |                |
 |  +----------+  |
 |  | Servlet  |  |
 |  |          |  |
 |  |  init()  |  |
 |  |          |  |
 |  | service()|  |
 |  |          |  |
 |  | destroy()|  |
 |  +----------+  |
 +----------------+
```

The Servlet interface defines the methods that must be implemented by a servlet. These methods are called by the web container during the lifecycle of the servlet. The lifecycle of a servlet consists of the following stages:

1. **Initialization**: The web container calls the `init()` method of the servlet to initialize it. This method is called only once during the lifecycle of the servlet.

2. **Service**: The web container calls the `service()` method of the servlet to handle requests from clients. This method is called multiple times during the lifecycle of the servlet, once for each request.

3. **Destruction**: The web container calls the `destroy()` method of the servlet to destroy it. This method is called only once during the lifecycle of the servlet, when the servlet is being removed from service.
