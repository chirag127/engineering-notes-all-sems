Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are some notes on the topic of cookies for the unit 5 - Servlets.

### Cookies
- Cookies are small pieces of data that are stored by a web browser on the client side.
- Cookies are used to store information about the user's preferences, session state, authentication, etc.
- Cookies are sent by the server to the browser using the `Set-Cookie` header in the HTTP response.
- Cookies are sent back by the browser to the server using the `Cookie` header in the HTTP request.
- Cookies have various attributes, such as name, value, domain, path, expiry, secure, and httpOnly.
- Cookies can be created, read, updated, and deleted by servlets using the `javax.servlet.http.Cookie` class and the `javax.servlet.http.HttpServletRequest` and `javax.servlet.http.HttpServletResponse` interfaces.
- Cookies can be classified into two types: session cookies and persistent cookies.
- Session cookies are temporary cookies that are deleted when the browser is closed. They do not have an expiry attribute.
- Persistent cookies are permanent cookies that are stored on the disk until they expire or are deleted by the user. They have an expiry attribute that specifies the date and time of their expiration.
- Cookies have some limitations, such as size, number, security, and privacy. Cookies can store up to 4 KB of data, and a browser can store up to 20 cookies per domain. Cookies can be intercepted, modified, or stolen by malicious parties, and can reveal sensitive information about the user. Cookies can be disabled or blocked by the user or the browser settings.