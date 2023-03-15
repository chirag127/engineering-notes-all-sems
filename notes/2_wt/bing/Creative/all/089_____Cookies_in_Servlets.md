### Cookies in Servlets

- A cookie is a small piece of information that is persisted between the multiple client requests.
- A cookie has a name, a single value, and optional attributes such as a comment, path and domain qualifiers, a maximum age, and a version number.
- Cookies are used for state management and session tracking, as the server treats every client request as a new one.
- Cookies are created by the servlet using the `Cookie` class in the Servlet API.
- The `Cookie` class provides various methods to perform different cookie operations, such as `addCookie()` to add cookies to the response object, `getCookies()` to get the array of cookies from the request object, `getName()` and `getValue()` to get the name and value of a cookie, `setMaxAge()` and `getMaxAge()` to set and get the maximum age of a cookie, etc .
- Cookies are sent to the browser by the server using the `addCookie()` method of the `HttpServletResponse` interface.
- Cookies are stored in the browser and sent back to the server for all the subsequent requests until the cookie is valid.
- Cookies can be deleted by the server by setting their maximum age to zero.
- Cookies can be disabled by the browser, which may affect the functionality of the web application.

#### Example of creating and sending a cookie in servlet

```java
//import the required packages
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class CookieExample extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {

    //set the content type of the response
    response.setContentType("text/html");

    //get the PrintWriter object to write the response
    PrintWriter out = response.getWriter();

    //create a cookie with name "user" and value "John"
    Cookie cookie = new Cookie("user", "John");

    //add the cookie to the response object
    response.addCookie(cookie);

    //write some HTML code to the response
    out.println("<html><head><title>Cookie Example</title></head>");
    out.println("<body><h1>Cookie Example</h1>");
    out.println("<p>A cookie has been created and sent to the browser.</p>");
    out.println("</body></html>");

    //close the PrintWriter object
    out.close();
  }
}
```

#### Example of getting and displaying a cookie in servlet

```java
//import the required packages
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class CookieDisplay extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {

    //set the content type of the response
    response.setContentType("text/html");

    //get the PrintWriter object to write the response
    PrintWriter out = response.getWriter();

    //get the array of cookies from the request object
    Cookie[] cookies = request.getCookies();

    //write some HTML code to the response
    out.println("<html><head><title>Cookie Display</title></head>");
    out.println("<body><h1>Cookie Display</h1>");
    out.println("<p>The following cookies are received from the browser:</p>");
    out.println("<table border='1'><tr><th>Name</th><th>Value</th></tr>");

    //loop through the array of cookies and display their name and value
    if (cookies != null) {
      for (Cookie cookie : cookies) {
        out.println("<tr><td>" + cookie.getName() + "</td>");
        out.println("<td>" + cookie.getValue() + "</td></tr>");
      }
    }

    //close the table and the HTML tags
    out.println("</table></body></html>");

    //close the PrintWriter object
    out.close();
  }
}
```

#### Advantages of cookies in servlets

- Cookies are easy to create and use.
- Cookies are supported by most browsers.
- Cookies can store small amounts of data on the client side, reducing the load on the server.
- Cookies can persist the user preferences and settings across multiple requests.

#### Disadvantages of cookies in servlets

- Cookies have a limited size and number.
- Cookies can be disabled or deleted by the user, affecting the functionality of the web application.
- Cookies are not secure, as they can be intercepted or modified by hackers[^2^