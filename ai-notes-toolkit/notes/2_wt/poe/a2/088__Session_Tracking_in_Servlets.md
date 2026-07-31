 Here is the content in markdown format without any emojis or external links, written in points and in a formal tone:

### Session Tracking in Servlets

1. HttpSession: Servlets can use the HttpSession object to track sessions. When a client accesses a servlet the first time, a session is created and a session ID is sent to the client. In subsequent requests, the client passes on this session ID which is used by the servlets to identify the session. Servlets can store attributes/objects in the session and retrieve them as long as the session is valid.
2. URL rewriting: The session ID can be embedded in the URLs accessed by the client. This is called URL rewriting. The embedded session ID is used by the servlets to track the client's session. The disadvantages are that the actual URL is obscured and the length of the URL increases with a long session ID.
3. Hidden form fields: The session ID can be stored in a hidden form field and sent to the servlets on form submission. This method faces issues if the client disables cookies as the session ID cannot be stored.
4. Cookies: Cookies are the most commonly used method to track sessions in servlets. A cookie containing the session ID is sent to the client by the servlet and stored by the browser. The cookie is sent back to the servlets with every request and enables the servlets to identify the client session.

The points are written in a formal tone with no emojis or external links as per your instructions. Please let me know if you would like me to modify or expand the content in any way.