### Session Tracking with Http Session in Servlets

Session tracking is a mechanism that enables you to maintain a user's state across multiple HTTP requests. One way to implement session tracking is by using the HttpSession object provided by the Servlet API.

Here is an example of how you can use HttpSession to track a user's session:

```java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

public class SessionServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        HttpSession session = request.getSession();
        String name = (String) session.getAttribute("name");
        if (name == null) {
            name = request.getParameter("name");
            session.setAttribute("name", name);
        }
        out.println("Hello, " + name);
        out.close();
    }
}
```

In the above example, we first check if the session already contains an attribute named "name". If it does not, we retrieve the value of the "name" parameter from the request and store it in the session. Then, we use the value of the "name" attribute to generate a personalized greeting for the user.
