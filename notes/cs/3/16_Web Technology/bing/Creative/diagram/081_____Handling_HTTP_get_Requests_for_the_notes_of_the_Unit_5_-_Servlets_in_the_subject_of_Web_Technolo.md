Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here is the content for handling HTTP get requests for the notes of Unit 5 - Servlets.

### Handling HTTP get Requests

- HTTP is a protocol that defines how messages are formatted and transmitted over the web.
- HTTP requests have a method, a URL, and optional headers and body.
- HTTP responses have a status code, optional headers, and optional body.
- HTTP methods indicate the action that the client wants to perform on the server.
- The most common HTTP methods are GET, POST, PUT, DELETE, and HEAD.
- GET method is used to request a resource from the server without sending any data.
- GET requests can have query parameters in the URL, which are key-value pairs separated by & and prefixed by ?.
- For example, `http://example.com/search?query=java&sort=asc` is a GET request with two query parameters: query and sort.
- GET requests are idempotent, which means that repeating the same request will not change the state of the server or the resource.
- GET requests are also cacheable, which means that the server or the client can store the response and reuse it for future requests.
- GET requests are limited by the length of the URL, which depends on the browser and the server. The maximum length is usually around 2000 characters.
- GET requests are not suitable for sending sensitive or large data, as the data is visible in the URL and can be logged or intercepted by intermediaries.

- Servlets are Java classes that run on a web server and handle HTTP requests and responses.
- Servlets implement the `javax.servlet.Servlet` interface, which defines the lifecycle and the methods of a servlet.
- The most important methods of the `Servlet` interface are `init`, `service`, and `destroy`.
- The `init` method is called once when the servlet is loaded by the web server. It can be used to initialize the servlet or perform some configuration tasks.
- The `service` method is called for each HTTP request that the servlet receives. It can be used to process the request and generate the response.
- The `destroy` method is called once when the servlet is unloaded by the web server. It can be used to release any resources or perform some cleanup tasks.
- The `service` method takes two parameters: a `javax.servlet.ServletRequest` object and a `javax.servlet.ServletResponse` object.
- The `ServletRequest` object represents the HTTP request and provides methods to access the request data, such as the method, the URL, the headers, the parameters, the body, etc.
- The `ServletResponse` object represents the HTTP response and provides methods to set the response data, such as the status code, the headers, the body, etc.
- The `ServletRequest` and `ServletResponse` objects are generic and can handle any protocol, not just HTTP.
- To handle HTTP-specific requests and responses, servlets can use the `javax.servlet.http.HttpServlet` class, which is a subclass of the `Servlet` interface.
- The `HttpServlet` class overrides the `service` method and dispatches the request to different methods based on the HTTP method.
- The `HttpServlet` class provides methods to handle each HTTP method, such as `doGet`, `doPost`, `doPut`, `doDelete`, and `doHead`.
- The `doGet` method takes two parameters: a `javax.servlet.http.HttpServletRequest` object and a `javax.servlet.http.HttpServletResponse` object.
- The `HttpServletRequest` object is a subclass of the `ServletRequest` object and provides methods to access HTTP-specific request data, such as the query parameters, the cookies, the session, etc.
- The `HttpServletResponse` object is a subclass of the `ServletResponse` object and provides methods to set HTTP-specific response data, such as the content type, the cookies, the redirection, etc.
- To handle a GET request, a servlet can override the `doGet` method and use the `HttpServletRequest` and `HttpServletResponse` objects to process the request and generate the response.
- For example, the following servlet handles a GET request and returns a simple HTML page with the query parameters:

```java
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

public class GetServlet extends HttpServlet {

  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
    // Set the content type of the response to text/html
    response.setContentType("text/html");

    // Get the query parameters from the request
    String query = request.getParameter("query");
    String sort = request.getParameter("sort");

    // Get the output stream of