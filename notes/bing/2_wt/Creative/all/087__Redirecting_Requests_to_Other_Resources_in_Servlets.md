### Redirecting Requests to Other Resources in Servlets

- Redirecting requests to other resources in servlets is a technique to transfer the control of a request from one servlet to another servlet, or to a JSP page, or to an HTML file, or to any other web resource.
- There are two ways to redirect requests to other resources in servlets: **forward** and **sendRedirect**.
- **Forward** is a method of the **RequestDispatcher** interface that allows a servlet to forward a request to another resource within the same web application. The original servlet is not aware of the response sent by the destination resource, and the URL in the browser does not change.
- **SendRedirect** is a method of the **HttpServletResponse** interface that allows a servlet to redirect a request to another resource in the same or different web application. The original servlet sends a response with a status code of 302 (Moved Temporarily) and a Location header with the URL of the destination resource. The browser then sends a new request to the destination resource, and the URL in the browser changes.
- The main differences between forward and sendRedirect are:

  - Forward works at the server side, while sendRedirect works at the client side.
  - Forward does not change the URL in the browser, while sendRedirect changes the URL in the browser.
  - Forward can access the request and response objects of the original servlet, while sendRedirect cannot access them.
  - Forward can only redirect to a resource within the same web application, while sendRedirect can redirect to a resource in any web application.
  - Forward is faster than sendRedirect, as it does not involve an extra round trip between the browser and the server.

- The syntax of forward and sendRedirect are:

  - To forward a request to another resource, use the following code:

    ```java
    RequestDispatcher rd = request.getRequestDispatcher("destinationURL");
    rd.forward(request, response);
    ```

  - To redirect a request to another resource, use the following code:

    ```java
    response.sendRedirect("destinationURL");
    ```

- A possible mnemonic to remember the difference between forward and sendRedirect is:

  - Forward is like a **F**erry that takes you to another place within the same island, without changing your ticket.
  - SendRedirect is like a **S**ubway that takes you to another place in a different city, by changing your ticket.