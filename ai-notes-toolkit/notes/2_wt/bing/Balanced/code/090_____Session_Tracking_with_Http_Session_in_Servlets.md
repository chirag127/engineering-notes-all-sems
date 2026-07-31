### Session Tracking with Http Session in Servlets

Session tracking is a way to maintain state (data) of a user across multiple requests to the server. Http protocol is stateless, so we need to use some techniques to keep track of the user's information and preferences. One of the techniques is to use the HttpSession interface, which is provided by the servlet container.

The HttpSession interface allows the server to create a session object and assign it a unique session ID for each user. The session ID is sent to the client as a cookie or as a part of the URL. The client sends back the session ID with each request, and the server uses it to retrieve the session object and the associated data.

The session object can store any type of data as attributes, using the setAttribute() and getAttribute() methods. The session object is available to all the servlets and JSPs that the user accesses until the session is invalidated or expired. The session can be invalidated by calling the invalidate() method on the session object, or by setting a timeout value using the setMaxInactiveInterval() method.

The following code shows an example of how to use the HttpSession interface to store and retrieve the user's name as a session attribute.

```java
// In the first servlet, get the user's name from the request parameter and store it as a session attribute
HttpSession session = request.getSession(); // create or get the session object
String name = request.getParameter("name"); // get the user's name from the request
session.setAttribute("name", name); // store the name as a session attribute
// In the second servlet, get the user's name from the session attribute and display it
HttpSession session = request.getSession(); // get the session object
String name = (String) session.getAttribute("name"); // get the name from the session attribute
response.setContentType("text/html");
PrintWriter out = response.getWriter();
out.println("<h1>Hello, " + name + "</h1>"); // display the name
```