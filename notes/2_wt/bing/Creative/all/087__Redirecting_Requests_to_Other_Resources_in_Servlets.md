### Redirecting Requests to Other Resources in Servlets

- Servlets are Java programs that run on the server-side and generate dynamic responses to the client request.
- Sometimes, a servlet may need to delegate the request to another resource, such as another servlet, a JSP page, or an HTML file, that are inside or outside the server.
- To achieve this, servlets provide two mechanisms: **forward** and **redirect**.
- Forwarding and redirecting are both about sending a user to different resources, although they have quite different semantics and implications.

#### Forward

- Forwarding a request means passing the request to another resource within the same server without the client being aware of it.
- The original request and response objects are preserved and passed to the destination resource.
- The URL in the browser does not change and the request parameters are still available.
- Forwarding is done by using the **RequestDispatcher** interface, which can be obtained from the servlet context or the request object.
- The **forward()** method of the RequestDispatcher interface takes the request and response objects as parameters and forwards them to the specified resource.
- For example, the following code snippet forwards the request to a servlet named "/forwarded":

```java
protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
  RequestDispatcher dispatcher = getServletContext().getRequestDispatcher("/forwarded");
  dispatcher.forward(req, resp);
}
```

#### Redirect

- Redirecting a request means sending the client a response that instructs it to make a new request to a different resource, which can be inside or outside the server.
- The original request and response objects are discarded and a new request is created by the client.
- The URL in the browser changes and the request parameters are not available unless they are appended to the new URL or stored in the session object.
- Redirecting is done by using the **sendRedirect()** method of the HttpServletResponse interface, which takes the location of the resource as a parameter and sends a temporary redirect response to the client.
- For example, the following code snippet redirects the request to a servlet named "/redirected":

```java
protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
  resp.sendRedirect(req.getContextPath() + "/redirected");
}
```

#### Differences

- Here is a list of major differences between servlet forward and redirect:

| Forward | Redirect |
|---------|----------|
| The request is further processed on the server side | The request is redirected to a different resource |
| The client is not impacted by forward, the URL in the browser stays the same | The client will see the URL change after the redirect |
| The request and response objects will remain the same after forwarding | A new request and response objects will be created after redirecting |
| The request-scope objects will be still available | The request-scope objects will be lost |
| Forwarding is faster and more efficient than redirecting | Redirecting is slower and more costly than forwarding |
| Forwarding can only be done to resources within the same server | Redirecting can be done to resources inside or outside the server |
| Forwarding is normally used within Model-View-Controller (MVC) web development pattern | Redirecting is normally used within Post/Redirect/Get (PRG) web development pattern |

#### Mnemonics and Learning Tricks

- To remember the difference between forward and redirect, you can use the following mnemonics and learning tricks:

  - Forward is like passing a note to someone in the same room, while redirect is like telling someone to go to another room and get a note from there.
  - Forward preserves the original request and response, while redirect creates a new request and response.
  - Forward keeps the same URL, while redirect changes the URL.
  - Forward is faster and more efficient, while redirect is slower and more costly.
  - Forward can only go to the same server, while redirect can go to any server.