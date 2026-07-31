### Session Tracking

- Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user (that is, requests originating from the same browser) across some period of time.
- Session tracking is also known as session management in servlet.
- HTTP protocol is stateless, which means it does not remember any information about the previous requests or responses. Therefore, we need to use session tracking techniques to maintain state and data of a user.
- There are four techniques used in session tracking:
  - Cookies: A cookie is a small piece of data that is stored on the client's browser and sent to the server with every request. The server can use the cookie to identify the user and store or retrieve information about the user's session.
  - Hidden Form Field: A hidden form field is a special type of input element that is not visible to the user, but can store some data that is submitted to the server with the form. The server can use the hidden form field to store or retrieve information about the user's session.
  - URL Rewriting: URL rewriting is a technique that appends some extra data to the URL of the request, such as a session ID. The server can use the URL to identify the user and store or retrieve information about the user's session.
  - HttpSession: HttpSession is a Java object that is created by the servlet container and associated with a unique session ID. The server can use the HttpSession object to store or retrieve information about the user's session. The session ID can be transmitted to the client using cookies, hidden form fields, or URL rewriting.
- Session tracking in servlet involves the following steps:
  - Get the associated session object (HttpSession) using request.getSession().
  - To get the specific value out of session object, call getAttribute(String) on the HttpSession object.
  - To set the specific value in session object, call setAttribute(String, Object) on the HttpSession object.
  - To remove the specific value from session object, call removeAttribute(String) on the HttpSession object.
  - To invalidate the session object, call invalidate() on the HttpSession object.