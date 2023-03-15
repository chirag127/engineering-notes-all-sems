### Interface Servlet and the Servlet Life Cycle in Servlets

The `javax.servlet.Servlet` interface defines the methods that all servlets must implement. A servlet class must implement this interface either directly or by extending a class that implements it, such as `javax.servlet.http.HttpServlet`.

The servlet life cycle consists of the following phases:

1. **Servlet instance creation**: The servlet container creates an instance of the servlet class when it is first requested by a client.

2. **Initialization**: The servlet container calls the `init` method of the servlet to initialize it. This method is called only once during the life cycle of the servlet.

3. **Request handling**: The servlet container calls the `service` method of the servlet to handle client requests. This method is called once for each request received by the servlet.

4. **Removal from service**: The servlet container calls the `destroy` method of the servlet to remove it from service. This method is called only once during the life cycle of the servlet, when the servlet is being removed from service.

Here is an example of a simple servlet that implements the `Servlet` interface and overrides the `init`, `service`, and `destroy` methods:

```java
import java.io.IOException;
import javax.servlet.Servlet;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

public class MyServlet implements Servlet {
    private ServletConfig config;

    @Override
    public void init(ServletConfig config) throws ServletException {
        this.config = config;
        System.out.println("Servlet initialized");
    }

    @Override
    public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException {
        System.out.println("Handling request");
    }

    @Override
    public void destroy() {
        System.out.println("Servlet destroyed");
    }

    @Override
    public ServletConfig getServletConfig() {
        return config;
    }

    @Override
    public String getServletInfo() {
        return "MyServlet";
    }
}
```