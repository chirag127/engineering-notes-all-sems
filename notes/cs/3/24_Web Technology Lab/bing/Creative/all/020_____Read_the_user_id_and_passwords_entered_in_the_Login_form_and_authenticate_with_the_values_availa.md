# Read the user id and passwords entered in the Login form and authenticate with the values available in the cookies for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A login form is a web page that allows users to enter their user id and password to access a protected resource or service.
- A cookie is a small piece of data that is stored by the web browser on the user's device. Cookies can be used to store information such as user preferences, session identifiers, authentication tokens, etc.
- To authenticate the user id and password entered in the login form with the values available in the cookies, the following steps can be followed:

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

  - Create a servlet that handles the login request. The servlet should use the `HttpServletRequest` and `HttpServletResponse` objects to access the request and response data. The servlet should also use the `Cookie` class to create, read, and manipulate cookies. For example:

  ```java
  import javax.servlet.*;
  import javax.servlet.http.*;
  import java.io.*;

  public class LoginServlet extends HttpServlet {

    // A method to check if the user id and password are valid
    // This method can be replaced by a database query or any other logic
    private boolean isValid(String user_id, String password) {
      // For simplicity, assume that the valid user id and password are "admin" and "1234"
      return user_id.equals("admin") && password.equals("1234");
    }

    // A method to create a cookie with the user id and password
    private Cookie createCookie(String user_id, String password) {
      // Create a cookie with the name "login" and the value as the user id and password separated by a colon
      Cookie cookie = new Cookie("login", user_id + ":" + password);
      // Set the cookie's max age to one hour (in seconds)
      cookie.setMaxAge(60 * 60);
      // Set the cookie's path to the root of the web application
      cookie.setPath("/");
      // Return the cookie
      return cookie;
    }

    // A method to read the cookie with the user id and password
    private Cookie readCookie(HttpServletRequest request) {
      // Get the array of cookies from the request
      Cookie[] cookies = request.getCookies();
      // If the cookies are not null, loop through them
      if (cookies != null) {
        for (Cookie cookie : cookies) {
          // If the cookie's name is "login", return the cookie
          if (cookie.getName().equals("login")) {
            return cookie;
          }
        }
      }
      // If no cookie is found, return null
      return null;
    }

    // A method to delete the cookie with the user id and password
    private void deleteCookie(HttpServletResponse response) {
      // Create a cookie with the name "login" and an empty value
      Cookie cookie = new Cookie("login", "");
      // Set the cookie's max age to zero (to expire it immediately)
      cookie.setMaxAge(0);
      // Set the cookie's path to the root of the web application
      cookie.setPath("/");
      // Add the cookie to the response
      response.addCookie(cookie);
    }

    // A method to handle the GET request
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
      // Set the content type of the response to text/html
      response.setContentType("text/html");
      // Get the print writer object to write the response
      PrintWriter out = response.getWriter();
      // Read the cookie with the user id and password
      Cookie cookie = readCookie(request);
      // If the cookie is not null, get the cookie value and split it by a colon
      if (cookie != null) {
        String value = cookie.getValue();
        String[] parts = value.split(":");
        // If the parts have length 2, get the user id and password from the parts
        if (parts.length == 2) {
          String user_id = parts[0];
          String password = parts[1