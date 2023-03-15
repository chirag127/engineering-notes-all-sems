#### Scripting in Servlets

Servlets can use scripting elements to generate dynamic content. Here is an example of a simple servlet that uses scripting elements to generate an HTML page:

```java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class HelloWorld extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
    out.println("<html>");
    out.println("<head><title>Hello World</title></head>");
    out.println("<body>");
    out.println("<h1>Hello World</h1>");
    out.println("</body></html>");
  }
}
```

This servlet uses the `doGet` method to handle HTTP GET requests. The `response.setContentType` method is used to set the MIME type of the response. The `response.getWriter` method returns a `PrintWriter` object that can be used to send character data to the client. The servlet uses the `println` method of the `PrintWriter` object to generate the HTML page.
