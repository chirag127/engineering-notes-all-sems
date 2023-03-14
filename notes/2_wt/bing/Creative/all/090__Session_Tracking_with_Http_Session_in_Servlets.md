### Session Tracking with Http Session in Servlets

- Session tracking is the process of maintaining the state of a client-server interaction over multiple requests.
- HTTP is a stateless protocol, which means that each request is treated as a new one and the server does not remember any information about the previous requests from the same client.
- Session tracking is useful for web applications that need to store and retrieve user-specific data, such as online shopping, mailing, or e-commerce applications.
- Servlets provide an interface called HttpSession for session tracking. An HttpSession object represents a unique session between a client and a server.
- The servlet container creates an HttpSession object for each client that requests a servlet for the first time. The container also assigns a unique session ID to the object and sends it back to the client as a cookie or a URL parameter.
- The client then sends the session ID along with each subsequent request to the server. The server uses the session ID to retrieve the corresponding HttpSession object and access the data stored in it.
- The servlet can store and retrieve data in the HttpSession object using the setAttribute(String name, Object value) and getAttribute(String name) methods. The data can be any Java object that implements the Serializable interface.
- The servlet can also check the status of the HttpSession object using the isNew(), isExpired(), and isValid() methods. The servlet can also invalidate the HttpSession object using the invalidate() method, which removes all the data and marks the session as invalid.
- The servlet can also set the timeout period for the HttpSession object using the setMaxInactiveInterval(int interval) method. The timeout period is the maximum time in seconds that the server will keep the session open between client requests. If the client does not make any request within the timeout period, the server will invalidate the session.
- The servlet can also configure the session tracking mechanism using the web.xml file. The servlet can specify the session timeout period, the cookie name, the cookie domain, the cookie path, and the URL rewriting parameter using the <session-config> element.

Here is an example of a servlet that uses HttpSession for session tracking:

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class SessionServlet extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // Get the HttpSession object
    HttpSession session = request.getSession();
    
    // Set the content type and the character encoding of the response
    response.setContentType("text/html");
    response.setCharacterEncoding("UTF-8");
    
    // Get the PrintWriter object to write the response
    PrintWriter out = response.getWriter();
    
    // Check if the session is new
    if (session.isNew()) {
      // Display a welcome message
      out.println("<h1>Welcome to the Session Servlet</h1>");
      // Store the user name in the session
      session.setAttribute("user", "Alice");
    } else {
      // Display a greeting message
      out.println("<h1>Hello, " + session.getAttribute("user") + "</h1>");
    }
    
    // Display the session ID and the creation time
    out.println("<p>Session ID: " + session.getId() + "</p>");
    out.println("<p>Session created at: " + new java.util.Date(session.getCreationTime()) + "</p>");
    
    // Close the PrintWriter object
    out.close();
  }
}
```