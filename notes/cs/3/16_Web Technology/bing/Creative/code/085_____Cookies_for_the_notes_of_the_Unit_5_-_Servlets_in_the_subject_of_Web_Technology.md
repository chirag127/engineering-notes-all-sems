Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content on the topic of cookies for the notes of the unit 5 - servlets in the subject of web technology. Here is the content I have written in markdown format:

### Cookies
- Cookies are small pieces of data that are stored by a web browser on the client side.
- Cookies are used to store information about the user's preferences, session state, authentication, etc.
- Cookies are sent by the server to the browser in the response header using the `Set-Cookie` directive.
- Cookies are sent back by the browser to the server in the request header using the `Cookie` directive.
- Cookies have various attributes, such as:
  - `name` : the name of the cookie
  - `value` : the value of the cookie
  - `domain` : the domain for which the cookie is valid
  - `path` : the path for which the cookie is valid
  - `expires` : the expiration date of the cookie
  - `max-age` : the maximum age of the cookie in seconds
  - `secure` : a flag that indicates whether the cookie should be sent only over HTTPS
  - `HttpOnly` : a flag that indicates whether the cookie should be accessible only by HTTP and not by JavaScript
- Cookies can be created, read, updated, and deleted by servlets using the `javax.servlet.http.Cookie` class and the `javax.servlet.http.HttpServletRequest` and `javax.servlet.http.HttpServletResponse` interfaces.
- Cookies can be created by creating a new `Cookie` object and setting its attributes, and then adding it to the response using the `addCookie()` method.
- Cookies can be read by getting an array of `Cookie` objects from the request using the `getCookies()` method, and then iterating over the array and getting the name and value of each cookie.
- Cookies can be updated by creating a new `Cookie` object with the same name and a different value, and then adding it to the response using the `addCookie()` method.
- Cookies can be deleted by creating a new `Cookie` object with the same name and a null value, and then setting its `max-age` attribute to zero, and then adding it to the response using the `addCookie()` method.
- Cookies have some limitations, such as:
  - Cookies are not secure, as they can be intercepted, modified, or stolen by malicious parties.
  - Cookies are not reliable, as they can be disabled, deleted, or expired by the user or the browser.
  - Cookies have a size limit of 4 KB, and a number limit of 20 per domain and 300 per browser.
  - Cookies are not suitable for storing sensitive or large amounts of data.