### Cookies in Servlets

- A cookie is a small piece of information that is persisted between the multiple client requests.
- A cookie has a name, a single value, and optional attributes such as a comment, path and domain qualifiers, a maximum age, and a version number.
- Cookies are used to identify a client when sending a subsequent request, and to pass some data from one servlet to another.
- Cookies are one of the state management techniques in session tracking, as the server treats every client request as a new one.
- To use cookies in Java, we need to use the Cookie class that is defined in the javax.servlet.http package .
- To create a cookie, we need to create an object of Cookie class and pass a name and its value.
- To send a cookie to the client, we need to add it to the response using the addCookie (Cookie) method of HttpServletResponse interface.
- To read a cookie from the client, we need to get all cookies from the request using the getCookies () method of HttpServletRequest interface, and then search for the one we need by comparing their names.
- To set the expiration date, domain, path, security, and version of a cookie, we can use the methods setMaxAge (int), setDomain (String), setPath (String), setSecure (boolean), and setVersion (int) of the Cookie class respectively.
- To get the name, value, comment, domain, max age, path, security, and version of a cookie, we can use the methods getName (), getValue (), getComment (), getDomain (), getMaxAge (), getPath (), getSecure (), and getVersion () of the Cookie class respectively.