# Session Tracking

Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user across some period of time. State refers to the data associated with a user, such as login information, preferences, shopping cart items, etc. HTTP protocol is stateless, which means that each request is independent and does not remember any information from previous requests. Therefore, session tracking is needed to enable web applications to provide personalized and interactive services to users.

Some points to remember about session tracking are:

- A session is a logical grouping of requests from the same user or browser.
- A session ID is a unique identifier that is assigned to each session by the server.
- A session object is an instance of the `javax.servlet.http.HttpSession` interface that stores the session data on the server side.
- A session object is created by the server when the user makes the first request and is invalidated when the user logs out or the session times out.
- A session object can be accessed by any servlet that belongs to the same web application as the servlet that created the session object.
- A session object can store any type of object as an attribute using the `setAttribute(String name, Object value)` method and can retrieve the attribute value using the `getAttribute(String name)` method.
- A session object can also provide information about the session, such as the session ID, the creation time, the last accessed time, the maximum inactive interval, etc.

There are four techniques used in session tracking:

- Cookies: A cookie is a small piece of data that is sent by the server to the client and stored by the client in a text file or memory. The client sends the cookie back to the server with each subsequent request. The cookie can contain the session ID or any other information that the server wants to store on the client side. Cookies are easy to use and widely supported by browsers, but they have some limitations, such as the size limit, the security risk, and the user's ability to disable them.
- Hidden form fields: A hidden form field is a special type of input element in an HTML form that is not visible to the user, but can store some data that is submitted to the server along with the form. The hidden form field can contain the session ID or any other information that the server wants to store on the client side. Hidden form fields are simple and reliable, but they only work with forms and require the user to submit the form to send the data to the server.
- URL rewriting: URL rewriting is a technique that appends the session ID or any other information to the URL of the request. The server can extract the session ID or the information from the URL and use it to identify the session. URL rewriting is transparent and works with any type of request, but it can make the URL look ugly and long, and it can expose the session ID or the information to the user or other parties.
- HttpSession: HttpSession is a technique that uses the session object on the server side to store the session data. The server sends a cookie or uses URL rewriting to send the session ID to the client, and the client sends the session ID back to the server with each request. The server uses the session ID to retrieve the session object and access the session data. HttpSession is the most convenient and flexible technique, but it requires the server to allocate memory for each session object and to manage the session lifecycle.