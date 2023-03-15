### Session Tracking with Http Session in Servlets

Session tracking is a way to maintain state (data) of a user across multiple requests to the server. Http protocol is stateless, so we need to use some techniques to keep track of the user's information and preferences. One of the techniques is to use HttpSession interface, which is provided by the servlet container.

HttpSession interface allows the server to create a session object and assign it a unique session ID for each user. The session ID is sent to the client as a cookie or as a part of the URL. The client sends back the session ID with each request, and the server uses it to retrieve the session object and the data associated with it.

To use HttpSession interface, we need to do the following steps:

- Get the session object by calling request.getSession() method in the servlet. This method returns the existing session object if there is one, or creates a new one if there is none.
- Store the data in the session object by calling session.setAttribute(String name, Object value) method. This method takes a name and a value as parameters and stores them in the session object. The value can be any Java object that implements Serializable interface.
- Retrieve the data from the session object by calling session.getAttribute(String name) method. This method takes a name as a parameter and returns the value associated with it, or null if there is no such attribute.
- Invalidate the session object by calling session.invalidate() method. This method removes the session object and all its data from the server. The client will not be able to access the session object after this method is called.

Here is an example of a servlet that uses HttpSession interface to store and retrieve the user's name:

```java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class SessionServlet extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {

    // Get the session object
    HttpSession session = request.getSession();

    // Get the user's name from the request parameter
    String name = request.getParameter("name");

    // If the name is not null, store it in the session object
    if (name != null) {
      session.setAttribute("name", name);
    }

    // Get the name from the session object
    name = (String) session.getAttribute("name");

    // Set the content type and character encoding
    response.setContentType("text/html");
    response.setCharacterEncoding("UTF-8");

    // Get the output stream
    PrintWriter out = response.getWriter();

    // Write the HTML response
    out.println("<html>");
    out.println("<head>");
    out.println("<title>Session Servlet</title>");
    out.println("</head>");
    out.println("<body>");
    out.println("<h1>Session Servlet</h1>");
    out.println("<p>Welcome, " + name + "</p>");
    out.println("<p><a href='session.html'>Go back</a></p>");
    out.println("</body>");
    out.println("</html>");

    // Close the output stream
    out.close();
  }
}
```

Here is an example of a HTML file that sends the user's name to the servlet:

```html
<html>
<head>
  <title>Session Example</title>
</head>
<body>
  <h1>Session Example</h1>
  <form action="SessionServlet" method="get">
    <p>Enter your name:</p>
    <input type="text" name="name">
    <input type="submit" value="Submit">
  </form>
</body>
</html>
```