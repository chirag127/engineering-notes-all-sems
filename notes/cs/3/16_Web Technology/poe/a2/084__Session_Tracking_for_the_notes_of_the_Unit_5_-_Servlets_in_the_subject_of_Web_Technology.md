 Here is the content in Markdown format without any emojis or external links:

### Session Tracking for the notes of the Unit 5 - Servlets

1. What is Session Tracking?
- Maintaining the state of a user across multiple requests.
- The server keeps track of the user's identification and stores variables/objects specific to that user.
- This allows servlets to store information about a user and utilize it across requests.

2. Why is Session Tracking required?
- The HTTP protocol is stateless. So each request from a client to a server is separate and independent.
- Session Tracking is required to maintain the state of a user and store user-specific data.
- This enables servlets to personalize responses and remember users between requests.

3. How to enable Session Tracking?
- Import the ```javax.servlet.http.HttpSession``` interface.
- Get a session object by calling ```request.getSession()```.
- If a new session is created, it is assigned a unique session ID via cookies.
- Attributes can be added to sessions via ```session.setAttribute(key, value)```.
- Attributes can be retrieved via ```session.getAttribute(key)```.

4. Session Timeouts
- Inactive sessions timeouts free up server memory.
- The time period after which a session times out is configured via ```session.setMaxInactiveInterval()```.
- Once a session times out, the session and all its attributes are invalidated. A new session will be created on the next request.

The content is written in points in a formal tone without emojis or external links as you specified. Please let me know if you would like me to modify or add anything.