 Here is the content in markdown format for the topic ### Session Tracking with Http Session for the notes of the Unit 5 - Servlets in the subject of Web Technology:

### Session Tracking with Http Session

- Http Session is a mechanism provided by the servlet container (like Tomcat) to track a user across multiple requests.
- It stores the data/information of a user as objects (key-value pairs) with a session id (cookie).
- The session is created when a user first visits a web application and is destroyed when the user exits/the session times out.
- To use HttpSession, we need to import `javax.servlet.http.HttpSession` and then use `request.getSession()` to get the session and set attributes (key-value pairs) in it.
- We can use `session.setAttribute()` to set attributes (store info) and `session.getAttribute()` to get attributes (retrieve info).
- The session id (cookie) is sent by the browser with every request to identify the user session.
- The session data is maintained by the servlet container in memory or on disk.

Advantages:
- Easy to implement as it is provided by the servlet container.
- Flexible to store user-specific data/state.

Disadvantages:
- The data is lost if the server is restarted.
- The session may timeout if inactive for a configured period of time (configurable).
- Performance decreases if a large amount of data is stored in a session.

**Examples:**
Storing user details in session:
`session.setAttribute("user", user);`

Retrieving user details from session:
`User user = (User) session.getAttribute("user");`

**Applications:**
- Shopping cart data.
- User login/authentication.
- Storing user preferences.

[Detailed diagrams and codes can be added here]