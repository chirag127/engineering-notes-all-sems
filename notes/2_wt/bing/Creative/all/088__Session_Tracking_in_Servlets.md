### Session Tracking in Servlets

- Session tracking is a way to maintain state (data) of a user across multiple requests.
- Session tracking is also known as session management in servlets.
- Session tracking is required because HTTP protocol is stateless, which means that each request is treated as a new one and the server does not remember the previous requests from the same user.
- Session tracking can be used to recognize the user, store user preferences, implement shopping carts, etc.
- Session tracking employs four different techniques: cookies, hidden form fields, URL rewriting, and HttpSession.

#### Cookies
- Cookies are small pieces of data sent by the web server in the response header and stored by the browser.
- Each web client can be assigned a unique session ID by the web server, and the cookies can be used to store the session ID and send it back to the server in subsequent requests.
- Cookies can be turned off by the client, which limits their usability.
- Cookies can be created, read, and deleted by using the javax.servlet.http.Cookie class and its methods.

#### Hidden Form Fields
- Hidden form fields are input elements in an HTML form that are not visible to the user, but can store some information and send it to the server along with the form submission.
- Hidden form fields can be used to store the session ID or any other data that needs to be passed from one servlet to another.
- Hidden form fields can be created by using the <input type="hidden" name="name" value="value"> tag in the HTML form.
- Hidden form fields can be read by using the request.getParameter("name") method in the servlet.

#### URL Rewriting
- URL rewriting is a technique of appending some extra data to the end of the URL, usually in the form of a query string.
- URL rewriting can be used to store the session ID or any other data that needs to be passed from one servlet to another.
- URL rewriting can be done by using the response.encodeURL("url") method in the servlet, which automatically adds the session ID to the URL if cookies are disabled.
- URL rewriting can be read by using the request.getQueryString() method in the servlet.

#### HttpSession
- HttpSession is an interface that defines an object that represents a session between a client and a server.
- HttpSession can be used to store any type of data as attributes, and access them from any servlet that belongs to the same session.
- HttpSession can be created, obtained, and invalidated by using the request.getSession(), request.getSession(boolean), and session.invalidate() methods respectively.
- HttpSession can be used to set and get attributes by using the session.setAttribute("name", value) and session.getAttribute("name") methods respectively.