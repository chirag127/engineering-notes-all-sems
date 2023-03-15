### Session Tracking

Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user across some period of time. Sessions are shared among the servlets accessed by a client.

Some points to remember about session tracking are:

- HTTP protocol is stateless, which means it does not remember any information about the previous requests or responses.
- Session tracking is also known as session management in servlet.
- Session tracking is useful for implementing features such as shopping carts, user authentication, personalization, etc.
- Session tracking requires that a session ID is maintained across multiple requests to the server. The session ID can be passed using different techniques.

Some techniques used for session tracking are:

- Cookies: Cookies are small pieces of data that are stored by the browser and sent to the server with every request. The server can set or read cookies using the `setCookie` and `getCookie` methods of the `HttpServletResponse` and `HttpServletRequest` classes respectively.
- Hidden Form Field: Hidden form fields are input elements of type `hidden` that are embedded in an HTML form. The server can set or read hidden form fields using the `getParameter` and `setParameter` methods of the `HttpServletRequest` and `HttpServletResponse` classes respectively.
- URL Rewriting: URL rewriting is a technique that appends the session ID to the URL of the request. The server can set or read the session ID using the `encodeURL` and `getParameter` methods of the `HttpServletResponse` and `HttpServletRequest` classes respectively.
- HttpSession: HttpSession is an interface that provides a way to store and retrieve objects associated with a session. The server can create or get a session object using the `getSession` method of the `HttpServletRequest` class. The session object can store or retrieve attributes using the `setAttribute` and `getAttribute` methods respectively.