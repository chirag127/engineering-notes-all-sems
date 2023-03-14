### Session Tracking in Servlets

- Session tracking is a way to maintain state (data) of a user across multiple requests.
- Session tracking is also known as session management in servlets.
- Session tracking is needed because HTTP protocol is stateless, which means that each request is treated as a new one and the server does not remember the previous requests from the same user.
- Session tracking can be used to recognize the user, store user preferences, implement shopping carts, etc.
- There are four techniques used in session tracking: cookies, hidden form fields, URL rewriting, and HttpSession.

#### Cookies
- Cookies are small pieces of data sent by the server in the response header and stored by the browser.
- Cookies can store a unique session ID for each user and send it back to the server with each request.
- Cookies can be disabled by the user, which limits their effectiveness.

#### Hidden Form Fields
- Hidden form fields are input elements in an HTML form that are not visible to the user, but can store some data.
- Hidden form fields can store the session ID or other information and pass it to the server when the form is submitted.
- Hidden form fields only work with forms that use the POST method, and can be tampered with by the user.

#### URL Rewriting
- URL rewriting is a technique that appends the session ID or other information to the URL of each request.
- URL rewriting can work with any type of request, and does not depend on the browser settings.
- URL rewriting can make the URL longer and less user-friendly, and can expose the session ID to others.

#### HttpSession
- HttpSession is a Java object that represents a session between a user and a server.
- HttpSession can store any type of data as attributes, and can be accessed by any servlet that belongs to the same application.
- HttpSession can be created by calling the request.getSession() method, and can be invalidated by calling the session.invalidate() method.
- HttpSession can also have a timeout period, which can be set by the server or by the servlet.