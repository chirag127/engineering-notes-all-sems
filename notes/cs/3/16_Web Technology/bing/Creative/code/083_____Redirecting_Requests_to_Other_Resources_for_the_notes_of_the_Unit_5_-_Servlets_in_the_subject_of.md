# Redirecting Requests to Other Resources

- Sometimes, a servlet may need to delegate the request processing to another resource, such as another servlet, a JSP page, or an HTML file.
- This can be done by using two methods: **forwarding** and **redirection**.
- Forwarding and redirection are different in terms of how the request and response objects are handled, and how the browser perceives the change of resource.

## Forwarding

- Forwarding is the process of passing the request and response objects from one servlet to another servlet within the same web application.
- Forwarding is done by using the **RequestDispatcher** interface, which can be obtained from the **ServletRequest** object by calling the **getRequestDispatcher()** method.
- The **getRequestDispatcher()** method takes a string argument that specifies the path of the resource to which the request should be forwarded.
- The **RequestDispatcher** object then provides the **forward()** method, which takes the request and response objects as parameters and forwards them to the specified resource.
- Forwarding is transparent to the browser, meaning that the browser does not know that the request has been forwarded to another resource, and the URL in the address bar remains unchanged.
- Forwarding is faster and more efficient than redirection, as it does not involve an extra round trip between the browser and the server.
- Forwarding can only be done within the same web application, and the resource path must be relative to the current servlet context.

## Redirection

- Redirection is the process of sending the browser a new URL and instructing it to make a new request to that URL.
- Redirection is done by using the **HttpServletResponse** object, which provides the **sendRedirect()** method.
- The **sendRedirect()** method takes a string argument that specifies the URL of the resource to which the request should be redirected.
- The **sendRedirect()** method sets the response status code to 302 (Found) and adds a **Location** header with the new URL to the response.
- The browser then receives the response and makes a new request to the new URL, which may be handled by a different servlet, a JSP page, an HTML file, or even a different web application or server.
- Redirection is visible to the browser, meaning that the browser knows that the request has been redirected to another resource, and the URL in the address bar changes accordingly.
- Redirection is slower and less efficient than forwarding, as it involves an extra round trip between the browser and the server.
- Redirection can be done to any resource, and the URL can be absolute or relative to the current servlet context.