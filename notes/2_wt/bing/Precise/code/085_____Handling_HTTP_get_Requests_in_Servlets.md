### Handling HTTP get Requests in Servlets

To handle HTTP GET requests in a servlet, you need to override the `doGet` method of the `HttpServlet` class. Here is an example:

```java
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class MyServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // your code here
    }
}
```

In the `doGet` method, you can access the request parameters using the `request` object and generate a response using the `response` object. For example, to get the value of a request parameter named `name`, you can use the following code:

```java
String name = request.getParameter("name");
```

To send a response to the client, you can use the `response` object's `getWriter` method to get a `PrintWriter` object, and then use its `println` method to write the response. For example, to send a plain text response to the client, you can use the following code:

```java
response.setContentType("text/plain");
PrintWriter out = response.getWriter();
out.println("Hello, " + name);
```
