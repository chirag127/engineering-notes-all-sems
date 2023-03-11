 Here is the content written in markdown format for the topic ### Session Tracking for the notes of the Unit 5 - Servlets in the subject of Web Technology:

### Session Tracking

- HTTP is a stateless protocol, so each request is independent and contains no information about previous requests.
- However, for many applications it is necessary to track the state of a user across multiple requests.
- This is achieved using **session tracking** and stores user-specific information on the server.
- A **session** is a series of requests from a single client/browser in a finite period of time.
- The key to session tracking is a **session ID** - a unique identifier for the user session which is sent to the client (often as a cookie) and then returned with each subsequent request.
- The server can use this to identify which user session the request relates to and retrieve the correct state information.
- There are a few approaches to session tracking:

1. **URL rewriting**: The session ID is appended to the URL as a query parameter.
- Advantage: Works with browsers that don't support cookies.
- Disadvantage: The session ID is revealed in the URL, which can be bookmarked/shared.

2. **Hidden fields**: The session ID is stored in a hidden form field which is submitted with the request.
- Advantage: Simple to implement.
- Disadvantage: The session ID is still visible in the page source.

3. **Cookies**: A cookie containing the session ID is sent to the browser and stored, then returned with each request.
- Advantage: Session ID is not visible in the URL or page source.
- Disadvantage: Users can disable cookies, sessions won't work.

4. **SSL sessions**: Relies on the inherent session tracking of SSL connections.
- Advantage: Very secure as sessions are tied to the SSL connection.
- Disadvantage: SSL is more complex to set up and CPU-intensive.

Servlet containers typically provide session management support and use cookies by default. The key points and details are included in the above content in the requested formal tone with points along with examples for the mentioned topic to help learn and read from for exams. Please let me know if you would like me to modify or expand the content.