### Session Tracking

Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user (that is, requests originating from the same browser) across some period of time. Sessions are shared among the servlets accessed by a client.

Session tracking is also known as session management in servlet. HTTP protocol is a stateless protocol, so we need to maintain state using session tracking techniques.

There are four techniques used in session tracking:

- Cookies
- Hidden Form Field
- URL Rewriting
- HttpSession

#### Cookies

Cookies are small pieces of information that are stored by the browser on the client's machine. They are sent by the server to the client along with the response, and the client sends them back to the server with the next request. Cookies can be used to store user preferences, login details, shopping cart items, etc.

To use cookies for session tracking, we need to do the following steps:

- Create a cookie object using the Cookie constructor, passing the name and value of the cookie.
- Set the maximum age of the cookie using the setMaxAge method, passing the number of seconds the cookie should live.
- Add the cookie to the response using the addCookie method, passing the cookie object.
- Retrieve the cookie from the request using the getCookies method, which returns an array of cookie objects.
- Loop through the array and find the cookie with the desired name using the getName method.
- Get the value of the cookie using the getValue method.

#### Hidden Form Field

Hidden form field is a way to embed hidden data in an HTML form. The data is not visible to the user, but it is sent to the server along with the form submission. Hidden form field can be used to store session information such as user name, password, etc.

To use hidden form field for session tracking, we need to do the following steps:

- Create a hidden input element in the HTML form using the type attribute with the value "hidden".
- Set the name and value attributes of the hidden input element with the session information.
- Retrieve the hidden input element from the request using the getParameter method, passing the name of the hidden input element.

#### URL Rewriting

URL rewriting is a way to append session information to the URL of the request. The session information is added as a query string parameter with the name "jsessionid" and the value of the session ID. URL rewriting can be used when cookies are disabled or not supported by the browser.

To use URL rewriting for session tracking, we need to do the following steps:

- Get the session ID from the request using the getRequestedSessionId method, which returns a string.
- Encode the URL with the session ID using the encodeURL method, passing the URL as a parameter.
- Use the encoded URL for creating links or redirects in the response.

#### HttpSession

HttpSession is an interface that provides a way to identify a user across multiple requests and store information about the user's session. HttpSession is created by the server and associated with a unique session ID. HttpSession can store any type of object as an attribute.

To use HttpSession for session tracking, we need to do the following steps:

- Get the HttpSession object from the request using the getSession method, which returns an HttpSession object. If the session does not exist, the method creates a new session and returns it.
- Set the session attributes using the setAttribute method, passing the name and value of the attribute.
- Get the session attributes using the getAttribute method, passing the name of the attribute.
- Invalidate the session using the invalidate method, which removes the session from the server.