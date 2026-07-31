# Cookies

Cookies are small text files that are stored on the client's computer by the server. They are used to store information about the user's interactions with the website. Cookies are used for a variety of purposes, including:

1. **Session management**: Cookies can be used to store information about the user's session, such as login information or shopping cart contents.

2. **Personalization**: Cookies can be used to store user preferences, such as language or display settings.

3. **Tracking**: Cookies can be used to track user behavior on a website, such as pages visited or items clicked.

Cookies are sent from the server to the client's browser in the HTTP response header. The browser then stores the cookie on the client's computer. When the client makes subsequent requests to the server, the browser sends the cookie back to the server in the HTTP request header.

Cookies have several limitations. They can only store a small amount of data, typically 4KB. They are also sent with every HTTP request, which can increase the amount of data being transmitted. Additionally, cookies can be blocked or deleted by the user, which can affect the functionality of the website.

In the context of Servlets, cookies can be created and managed using the `javax.servlet.http.Cookie` class. Cookies can be added to the response using the `addCookie()` method of the `HttpServletResponse` object. Cookies can be retrieved from the request using the `getCookies()` method of the `HttpServletRequest` object.

Overall, cookies are a useful tool for managing state and personalizing the user experience on a website. However, their limitations and potential privacy concerns should be taken into consideration when using them.