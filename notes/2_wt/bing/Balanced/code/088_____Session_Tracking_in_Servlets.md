### Session Tracking in Servlets

Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user (that is, requests originating from the same browser) across some period of time. Sessions are shared among the servlets accessed by a client.

There are four techniques used in session tracking:

- Cookies
- Hidden Form Field
- URL Rewriting
- HttpSession

The most commonly used technique is HttpSession, which is an interface that provides a way to identify a user across more than one page request or visit to a website and to store information about that user.

To use HttpSession, you need to do the following steps:

- Get the HttpSession object by calling the `request.getSession()` method in the servlet. This method returns the current session associated with the request, or if the request does not have a session, it creates one.
- Set the attributes in the HttpSession object by calling the `session.setAttribute(String name, Object value)` method. This method binds an object to the session, using the name specified. You can store any type of object in the session, such as strings, integers, or custom classes.
- Get the attributes from the HttpSession object by calling the `session.getAttribute(String name)` method. This method returns the object bound with the specified name in the session, or null if no object is bound under the name.
- Invalidate the HttpSession object by calling the `session.invalidate()` method. This method invalidates the session and removes any objects that were bound to it. You should call this method when the user logs out or the session expires.

Here is an example of how to use HttpSession in a servlet:

```java
// Import required packages
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

// Extend HttpServlet class
public class SessionServlet extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
    
    // Set response content type
    response.setContentType("text/html");
    
    // Get the HttpSession object
    HttpSession session = request.getSession();
    
    // Set an attribute in the session
    session.setAttribute("name", "John");
    
    // Get an attribute from the session
    String name = (String) session.getAttribute("name");
    
    // Print the attribute value
    PrintWriter out = response.getWriter();
    out.println("<h1>Hello, " + name + "</h1>");
    
    // Invalidate the session
    session.invalidate();
  }
}
```