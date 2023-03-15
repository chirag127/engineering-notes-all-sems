### Cookies

- A cookie is a small piece of information that is persisted between the multiple client requests.
- A cookie has a name, a single value, and optional attributes such as a comment, path and domain qualifiers, a maximum age, and a version number.
- A cookie is created by the server and sent to the browser in the response header .
- The browser stores the cookie on the local machine and sends it back to the server for all the subsequent requests until the cookie is valid.
- The server uses the cookie to identify the user and maintain the state of the session .
- The Cookie class in the Servlet API is used to create and manipulate cookies.
- The addCookie() method of the HttpServletResponse interface is used to add cookies to the response object .
- The getCookies() method of the HttpServletRequest interface is used to get the array of cookies from the request object .
- The getName() and getValue() methods of the Cookie class are used to get the name and value of a cookie .
- The setMaxAge() method of the Cookie class is used to set the expiration time of a cookie .
- The setComment(), setPath(), setDomain(), and setSecure() methods of the Cookie class are used to set the optional attributes of a cookie.
- The getComment(), getPath(), getDomain(), and getSecure() methods of the Cookie class are used to get the optional attributes of a cookie.