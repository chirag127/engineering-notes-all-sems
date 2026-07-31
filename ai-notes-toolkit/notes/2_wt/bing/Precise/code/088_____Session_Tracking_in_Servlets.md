### Session Tracking in Servlets

Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user across some period of time. There are four techniques used for session tracking in servlets: 

1. **Cookies**: A cookie is a small piece of information that is sent by a servlet to a Web browser, saved by the browser, and later sent back to the server. A cookie's value can uniquely identify a client, so cookies are commonly used for session management.

2. **Hidden Form Fields**: Hidden form fields are used when the client fills out an online form, and the form is submitted using either a GET or POST method. The form data is sent to the server-side script, which can then use hidden form fields to maintain the state of the user's session.

3. **URL Rewriting**: URL rewriting is a technique where the session ID is appended to the URL of the next servlet or the next resource to be accessed.

4. **HTTP Session**: An HTTP session is a way to store information on the server side, rather than on the client side. A session is created when a user logs in or adds an item to a shopping cart. The session information is stored on the server and is identified by a session ID.

Here is an example of how to create and use an HTTP session in a servlet:

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

This code creates an HTTP session and stores the user's name in the session. If the user's name is not already stored in the session, it is retrieved from the request parameter and stored in the session. The user's name is then retrieved from the session and displayed to the user. This allows the servlet to maintain state about the user's name across multiple requests.
