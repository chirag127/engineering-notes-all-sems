# Cookies

- A cookie is a small piece of information that is persisted between the multiple client requests.
- A cookie has a name, a single value, and optional attributes such as a comment, path and domain qualifiers, a maximum age, and a version number.
- A cookie is used to store user preferences, session information, or other data that can be used by the server to identify the user.
- A cookie is sent by the server to the browser in the header of the HTTP response, and the browser stores it on the local machine.
- The browser sends the cookie back to the server in the header of the HTTP request for all the subsequent requests until the cookie is valid or deleted.
- The Servlet API provides the Cookie class to create and manipulate cookies.
- The Cookie class has constructors, methods, and constants to perform various cookie operations.
- Some of the common methods of the Cookie class are:

  - `public Cookie(String name, String value)`: creates a cookie with the given name and value.
  - `public String getName()`: returns the name of the cookie.
  - `public String getValue()`: returns the value of the cookie.
  - `public void setValue(String newValue)`: sets the value of the cookie.
  - `public int getMaxAge()`: returns the maximum age of the cookie in seconds.
  - `public void setMaxAge(int expiry)`: sets the maximum age of the cookie in seconds.
  - `public String getDomain()`: returns the domain name of the cookie.
  - `public void setDomain(String pattern)`: sets the domain name of the cookie.
  - `public String getPath()`: returns the path of the cookie.
  - `public void setPath(String uri)`: sets the path of the cookie.
  - `public boolean getSecure()`: returns true if the cookie is secure, false otherwise.
  - `public void setSecure(boolean flag)`: sets the secure attribute of the cookie.
  - `public String getComment()`: returns the comment of the cookie.
  - `public void setComment(String purpose)`: sets the comment of the cookie.

- To add a cookie to the response object, the `addCookie(Cookie cookie)` method of the HttpServletResponse interface is used.
- To get the cookies from the request object, the `getCookies()` method of the HttpServletRequest interface is used, which returns an array of Cookie objects.
- To delete a cookie, the `setMaxAge(0)` method of the Cookie class is used, which sets the expiry time of the cookie to zero.
- Cookies are one of the state management techniques in session tracking, which is the process of maintaining the state of the user across multiple requests.
- Cookies have some limitations, such as:

  - Cookies are stored on the client side, which may pose security and privacy risks.
  - Cookies are dependent on the browser settings, which may disable or delete cookies.
  - Cookies have a size limit of 4 KB, which may restrict the amount of data that can be stored.
  - Cookies are not supported by all the browsers or devices.