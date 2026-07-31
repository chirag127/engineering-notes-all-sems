### Session Tracking

Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user (that is, requests originating from the same browser) across some period of time. Sessions are shared among the servlets accessed by a client.

Session tracking is also known as session management in servlet. HTTP protocol is stateless, so we need to maintain state using session tracking techniques.

There are four techniques used in session tracking:

- Cookies
- Hidden Form Field
- URL Rewriting
- HttpSession

#### Cookies

Cookies are small pieces of information that are stored by the browser on the client's machine. They are sent by the server to the client along with the response, and then sent back by the client to the server along with the request. Cookies can be used to store user preferences, login details, shopping cart items, etc.

To use cookies for session tracking, the servlet needs to:

- Create a Cookie object using the constructor `Cookie(String name, String value)`
- Set the maximum age of the cookie using the method `setMaxAge(int seconds)`
- Add the cookie to the response using the method `addCookie(Cookie cookie)`
- Retrieve the cookie from the request using the method `getCookies()`
- Get the name and value of the cookie using the methods `getName()` and `getValue()`

#### Hidden Form Field

Hidden form field is a technique that uses a hidden input element in an HTML form to store the session information. The hidden input element has a name and a value, but it is not visible to the user. The hidden input element is sent by the server to the client along with the response, and then sent back by the client to the server along with the request.

To use hidden form field for session tracking, the servlet needs to:

- Create a hidden input element in the HTML form using the syntax `<input type="hidden" name="name" value="value">`
- Set the name and value of the hidden input element using the parameters of the request
- Retrieve the name and value of the hidden input element using the methods `getParameter(String name)` and `getParameterValues(String name)`

#### URL Rewriting

URL rewriting is a technique that appends the session information to the end of the URL as a query string. The query string is a part of the URL that starts with a question mark (?) and contains name-value pairs separated by ampersands (&). The query string is sent by the server to the client along with the response, and then sent back by the client to the server along with the request.

To use URL rewriting for session tracking, the servlet needs to:

- Encode the URL with the session information using the method `encodeURL(String url)`
- Send the encoded URL to the client using the methods `sendRedirect(String url)` or `getWriter().println(String url)`
- Retrieve the session information from the URL using the methods `getParameter(String name)` and `getParameterValues(String name)`

#### HttpSession

HttpSession is an interface that provides a way to identify a user across multiple requests and store information about the user. HttpSession is created by the server and associated with a unique session ID. The session ID is sent by the server to the client using a cookie or URL rewriting, and then sent back by the client to the server along with the request.

To use HttpSession for session tracking, the servlet needs to:

- Get the HttpSession object associated with the request using the method `getSession()`
- Set the session attributes using the method `setAttribute(String name, Object value)`
- Get the session attributes using the method `getAttribute(String name)`
- Remove the session attributes using the method `removeAttribute(String name)`
- Invalidate the session using the method `invalidate()`

: https://www.cs.fsu.edu/~jtbauer/cis3931/tutorial/servlets/client-state/session-tracking.html
: https://www.javatpoint.com/session-tracking-in-servlets