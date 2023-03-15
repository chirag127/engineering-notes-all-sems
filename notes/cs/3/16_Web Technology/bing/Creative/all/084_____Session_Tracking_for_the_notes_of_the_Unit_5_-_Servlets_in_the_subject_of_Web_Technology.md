# Session Tracking

Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user across some period of time. Sessions are shared among the servlets accessed by a client.

## Why Session Tracking?

HTTP protocol is stateless, which means that each request is independent and does not remember the previous requests or responses. This makes it difficult to implement applications that require user authentication, shopping carts, personalization, etc. Session tracking is a way to overcome this limitation and maintain state (data) of a user.

## How Session Tracking Works?

Session tracking basically requires that a session ID is maintained across multiple requests to the server. This means that each time a given client makes a request to the server, it passes the same session ID. The server can use this ID to lookup the session information it maintains.

## Techniques of Session Tracking

There are four techniques used in session tracking:

- **Cookies**: Cookies are small pieces of data that are stored by the browser on the client side. The server can send cookies to the client and the client can send them back to the server in subsequent requests. Cookies can be used to store the session ID and other information about the user.
- **Hidden Form Field**: Hidden form fields are input elements of type hidden that are not visible to the user. They can be used to store the session ID and other information in a form. The form data is sent to the server when the user submits the form.
- **URL Rewriting**: URL rewriting is a technique of appending the session ID and other information to the URL of the request. The server can extract the session ID and other information from the URL and use them to maintain the session. URL rewriting can be used when cookies are disabled by the client.
- **HttpSession**: HttpSession is an interface that provides a way to create and manage sessions on the server side. The server can create a session object for each client and associate a unique session ID with it. The session ID can be sent to the client using cookies, hidden form fields, or URL rewriting. The session object can store attributes (key-value pairs) that can be accessed by the servlets. The session object also provides methods to invalidate, check, and modify the session.