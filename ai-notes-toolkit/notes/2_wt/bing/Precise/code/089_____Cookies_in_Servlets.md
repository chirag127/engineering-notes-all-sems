### Cookies in Servlets

Here is an example of how to use cookies in servlets:

```java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class CookieExample extends HttpServlet {
 
   public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {
      
      // Create a new cookie
      Cookie cookie = new Cookie("username", "JohnDoe");
      
      // Set the maximum age of the cookie
      cookie.setMaxAge(60*60*24);
      
      // Add the cookie to the response
      response.addCookie(cookie);
      
      // Set the response content type
      response.setContentType("text/html");
      
      PrintWriter out = response.getWriter();
      String title = "Setting Cookies Example";
      String docType =
         "<!doctype html public \"-//w3c//dtd html 4.0 " +
         "transitional//en\">\n";
         
      out.println(docType +
         "<html>\n" +
         "<head><title>" + title + "</title></head>\n" +
         "<body bgcolor=\"#f0f0f0\">\n" +
         "<h1 align=\"center\">" + title + "</h1>\n" +
         "<ul>\n" +
         "  <li><b>Username</b>: "
         + request.getParameter("username") + "\n" +
         "</ul>\n" +
         "</body></html>");
   }
}
```
This code creates a new cookie with the name `username` and the value `JohnDoe`. The maximum age of the cookie is set to one day (60 seconds * 60 minutes * 24 hours). The cookie is then added to the response and sent to the client. The servlet also generates an HTML response that displays the value of the `username` parameter from the request.