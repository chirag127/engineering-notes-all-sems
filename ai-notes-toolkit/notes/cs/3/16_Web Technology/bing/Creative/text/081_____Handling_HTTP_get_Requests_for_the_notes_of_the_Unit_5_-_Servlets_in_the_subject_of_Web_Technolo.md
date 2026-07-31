### Handling HTTP get Requests for the notes of the Unit 5 - Servlets in the subject of Web Technology

- HTTP get requests are used to retrieve information from a web server based on the parameters specified in the URL.
- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- To handle HTTP get requests in a servlet, the following steps are required:

  1. Create a Java class that extends the `HttpServlet` class and overrides the `doGet` method.
  2. Annotate the class with the `@WebServlet` annotation and specify the URL pattern that maps to the servlet.
  3. In the `doGet` method, obtain the request parameters from the `HttpServletRequest` object using the `getParameter` or `getParameterValues` methods.
  4. Perform any business logic or data processing based on the request parameters.
  5. Generate the response content using the `PrintWriter` object obtained from the `HttpServletResponse` object using the `getWriter` method.
  6. Set the response content type using the `setContentType` method of the `HttpServletResponse` object.
  7. Optionally, set any response headers using the `setHeader` or `addHeader` methods of the `HttpServletResponse` object.
  8. Close the `PrintWriter` object using the `close` method.

- Example:

  ```java
  import java.io.IOException;
  import java.io.PrintWriter;
  import javax.servlet.annotation.WebServlet;
  import javax.servlet.http.HttpServlet;
  import javax.servlet.http.HttpServletRequest;
  import javax.servlet.http.HttpServletResponse;

  @WebServlet("/hello")
  public class HelloServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
      // Get the name parameter from the request
      String name = request.getParameter("name");
      if (name == null) {
        name = "World";
      }

      // Generate the response content
      PrintWriter out = response.getWriter();
      out.println("<html>");
      out.println("<head><title>Hello Servlet</title></head>");
      out.println("<body>");
      out.println("<h1>Hello, " + name + "!</h1>");
      out.println("</body>");
      out.println("</html>");

      // Set the response content type
      response.setContentType("text/html");

      // Close the PrintWriter
      out.close();
    }
  }
  ```

- To test the servlet, deploy it on a web server (such as Tomcat) and access the URL `http://localhost:8080/hello?name=Sydney` from a web browser. The browser should display the following output:

  ```html
  <html>
  <head><title>Hello Servlet</title></head>
  <body>
  <h1>Hello, Sydney!</h1>
  </body>
  </html>
  ```