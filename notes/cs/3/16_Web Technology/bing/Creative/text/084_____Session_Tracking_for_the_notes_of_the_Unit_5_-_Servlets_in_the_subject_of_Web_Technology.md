### Session Tracking

Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user (that is, requests originating from the same browser) across some period of time. Sessions are shared among the servlets accessed by a client.

Session tracking is also known as session management in servlet. HTTP protocol is stateless, so we need to maintain state using session tracking techniques.

There are four techniques used in session tracking:

- Cookies
- Hidden Form Field
- URL Rewriting
- HttpSession

#### Cookies

Cookies are small pieces of information that are stored by the browser on the client's machine. They are sent by the server to the client along with the response, and then sent back by the client to the server along with the request. Cookies can be used to store user preferences, login information, shopping cart items, etc.

To use cookies for session tracking, the servlet can create a cookie object using the Cookie class, set its name and value, and add it to the response using the addCookie method. The servlet can also set the maximum age, path, domain, and secure attributes of the cookie. The browser will store the cookie and send it back to the server whenever it requests a resource from the same domain and path.

To retrieve the cookies from the request, the servlet can use the getCookies method, which returns an array of Cookie objects. The servlet can then loop through the array and find the cookie with the desired name using the getName method. The servlet can also get the value of the cookie using the getValue method.

#### Hidden Form Field

Hidden form field is a technique that uses a hidden input element in an HTML form to store the session information. The hidden input element has a name and a value, but it is not visible to the user. The servlet can set the value of the hidden input element using the setAttribute method on the request object, and then forward the request to a JSP page that contains the form. The JSP page can use the getAttribute method to get the value of the hidden input element and include it in the form.

When the user submits the form, the hidden input element is sent along with the other form parameters to the server. The servlet can then use the getParameter method to get the value of the hidden input element from the request object.

#### URL Rewriting

URL rewriting is a technique that appends the session information to the end of the URL as a query string. The servlet can use the encodeURL method on the response object to add the session information to the URL. The encodeURL method takes a URL as a parameter and returns a modified URL that contains the session information. The servlet can then use the modified URL to create a link or a redirect.

When the user clicks on the link or follows the redirect, the session information is sent along with the request to the server. The servlet can then use the getSession method on the request object to get the session object associated with the session information.

#### HttpSession

HttpSession is a class that represents a session between a client and a server. It provides methods to store and retrieve session attributes, get and set the session ID, check the session validity, and invalidate the session. The servlet can use the getSession method on the request object to get the session object associated with the current request. If there is no session, the getSession method can create a new session if the parameter is true, or return null if the parameter is false.

To store a session attribute, the servlet can use the setAttribute method on the session object, which takes a name and a value as parameters. To retrieve a session attribute, the servlet can use the getAttribute method on the session object, which takes a name as a parameter and returns the value. To remove a session attribute, the servlet can use the removeAttribute method on the session object, which takes a name as a parameter.

To get the session ID, the servlet can use the getId method on the session object, which returns a string. To check the session validity, the servlet can use the isNew method on the session object, which returns a boolean. To invalidate the session, the servlet can use the invalidate method on the session object, which destroys the session and unbinds any session attributes.