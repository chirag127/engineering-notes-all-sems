### Read the user id and passwords entered in the Login form and authenticate with the values available in the cookies for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A login form is a web page that allows users to enter their user id and password to access a protected resource or service.
- A cookie is a small piece of data that is stored by the web browser on the user's device. Cookies can be used to store user preferences, session information, authentication tokens, and other data.
- JDDC (Java Database Driver Connectivity) is a Java API that allows Java applications to connect to various types of databases and execute SQL queries and commands.
- ODBC (Open Database Connectivity) is a standard API that allows applications to access data from different database management systems using a common interface.
- Session tracking is a technique that allows web servers to maintain the state of a user's interaction with a web application across multiple requests. Session tracking can be implemented using cookies, URL rewriting, hidden form fields, or HTTP headers.
- To read the user id and password entered in the login form and authenticate with the values available in the cookies, the following steps can be followed:

  - Create a login form using HTML and CSS. The form should have two input fields for user id and password, and a submit button. For example:

```html
<form action="login" method="POST">
  <label for="user_id">User ID:</label>
  <input type="text" id="user_id" name="user_id" required>
  <label for="password">Password:</label>
  <input type="password" id="password" name="password" required>
  <button type="submit">Login</button>
</form>
```

  - Create a servlet that handles the login request. The servlet should read the user id and password from the request parameters, and compare them with the values stored in the cookies. If the values match, the servlet should redirect the user to the protected resource or service. If the values do not match, the servlet should display an error message. For example:

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class LoginServlet extends HttpServlet {
  public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // Get the user id and password from the request parameters
    String user_id = request.getParameter("user_id");
    String password = request.getParameter("password");

    // Get the cookies from the request
    Cookie[] cookies = request.getCookies();

    // Check if the cookies are not null and contain the user id and password
    if (cookies != null && cookies.length > 0) {
      // Loop through the cookies and find the ones with the name "user_id" and "password"
      String cookie_user_id = null;
      String cookie_password = null;
      for (Cookie cookie : cookies) {
        if (cookie.getName().equals("user_id")) {
          cookie_user_id = cookie.getValue();
        }
        if (cookie.getName().equals("password")) {
          cookie_password = cookie.getValue();
        }
      }

      // Compare the user id and password with the cookie values
      if (user_id.equals(cookie_user_id) && password.equals(cookie_password)) {
        // Authentication successful, redirect the user to the protected resource or service
        response.sendRedirect("protected");
      } else {
        // Authentication failed, display an error message
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<p>Invalid user id or password.</p>");
      }
    } else {
      // No cookies found, display an error message
      response.setContentType("text/html");
      PrintWriter out = response.getWriter();
      out.println("<p>No cookies found.</p>");
    }
  }
}
```

  - To store the user id and password in the cookies, the following steps can be followed:

    - Create a servlet that handles the registration request. The servlet should read the user id and password from the request parameters, and create two cookies with the name "user_id" and "password" and the value as the user id and password respectively. The servlet should also set the maximum age and the path of the cookies, and add them to the response. For example:

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class RegisterServlet extends HttpServlet {
  public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // Get the user id and password from the request parameters
    String user_id = request.getParameter("user_id");
    String password = request.getParameter("password");

    // Create two cookies with the name "user_id

```
