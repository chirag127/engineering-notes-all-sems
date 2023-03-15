### Handling HTTP get Requests in Servlets

- A servlet can handle HTTP get requests by implementing the `doGet` method of the `HttpServlet` class.
- The `doGet` method takes two parameters: an `HttpServletRequest` object and an `HttpServletResponse` object.
- The `HttpServletRequest` object represents the request from the client, and provides methods to access the request parameters, headers, cookies, etc.
- The `HttpServletResponse` object represents the response to the client, and provides methods to set the response status, headers, cookies, etc.
- The `doGet` method can also use the `getWriter` method of the `HttpServletResponse` object to obtain a `PrintWriter` object, which can be used to write the response body as text or HTML.
- The `doGet` method can also use the `getServletContext` method of the `HttpServlet` class to obtain a `ServletContext` object, which can be used to access the servlet context attributes, resources, etc.
- The `doGet` method can also use the `getServletConfig` method of the `HttpServlet` class to obtain a `ServletConfig` object, which can be used to access the servlet initialization parameters, etc.
- The `doGet` method can also use the `getRequestDispatcher` method of the `HttpServletRequest` or `ServletContext` object to obtain a `RequestDispatcher` object, which can be used to forward the request to another servlet or JSP, or to include the output of another servlet or JSP in the response.
- The `doGet` method can also use the `sendRedirect` method of the `HttpServletResponse` object to redirect the client to another URL.
- The `doGet` method can also use the `sendError` method of the `HttpServletResponse` object to send an error status and message to the client.

- A simple example of a servlet that handles HTTP get requests is:

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class HelloServlet extends HttpServlet {

  // Override the doGet method to handle HTTP get requests
  public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
  
    // Set the response content type to text/html
    response.setContentType("text/html");
    
    // Get a PrintWriter object to write the response body
    PrintWriter out = response.getWriter();
    
    // Write some HTML code to display a greeting message
    out.println("<html>");
    out.println("<head><title>Hello Servlet</title></head>");
    out.println("<body>");
    out.println("<h1>Hello, world!</h1>");
    out.println("</body>");
    out.println("</html>");
    
    // Close the PrintWriter object
    out.close();
  }
}
```

- A mnemonic to remember the methods of the `HttpServletRequest` and `HttpServletResponse` objects is:

  - **P**arameters, **H**eaders, **C**ookies: methods to access the request or response **P**arameters, **H**eaders, **C**ookies, such as `getParameter`, `getHeader`, `getCookie`, etc.
  - **S**tatus, **H**eaders, **C**ookies: methods to set the response **S**tatus, **H**eaders, **C**ookies, such as `setStatus`, `setHeader`, `addCookie`, etc.
  - **W**riter: method to get a `PrintWriter` object to write the response body, such as `getWriter`.
  - **S**ervletContext, **S**ervletConfig: methods to get the `ServletContext` or `ServletConfig` object, such as `getServletContext` or `getServletConfig`.
  - **R**equestDispatcher, **R**edirect, **R**rror: methods to forward, redirect, or send an error, such as `getRequestDispatcher`, `sendRedirect`, or `sendError`.