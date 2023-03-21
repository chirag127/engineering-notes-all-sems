 Here is the content in Markdown format with formal tone and without emojis:

### Session Tracking with Http Session for the notes of the Unit 5 - Servlets in the subject of Web Technology

1. HttpSession object is used to track a user across multiple requests.
2. When a user logs in to a web application, a session is created for that user. A session ID is sent to the user in a cookie. This session ID is used to identify the user in subsequent requests.
3. The session object contains attributes which can hold objects/data to be used across requests. For example, once a user logs in, the user object can be stored in the session and used in subsequent requests to identify the user, display username etc.
4. The session object has methods like setAttribute, getAttribute, removeAttribute, invalidate etc to add, retrieve and delete attributes and to invalidate a session.
5. The session data is stored on the server side. By default, session data is stored in memory. It can also be configured to store in a database to persist the data.
6. The session data gets deleted once the user closes the browser. Also, if there is no activity for a configured period of time (session timeout), the session gets invalidated. We can also manually invalidate a session using the invalidate method.
7. HttpSession has methods to get session ID, creation time, last accessed time etc.
8. Some key points to remember:
    - Use sessions to store user specific data.
    - Do not store large objects in session as it can affect performance.
    - Invalidate sessions properly to free up server resources.
    - Sessions are not secure - do not store sensitive data.
    - Sessions are supported only in HTTP and not in REST.

The content does not contain any external links or emojis and is written in a formal tone with points in Markdown format as requested. Please let me know if you would like me to modify or expand the content.