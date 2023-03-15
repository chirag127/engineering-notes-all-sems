 Here is the content in Markdown format without any emojis or external links:

### Session Tracking with Http Session in Servlets

1. HttpSession object is used to track a user across multiple requests.
2. When a user visits a web application for the first time, the server creates a HttpSession and assigns a unique session ID to it. This session ID is sent back to the browser via cookie or URL rewriting.
3. On subsequent requests, the browser sends back this session ID. The server uses this ID to retrieve the associated HttpSession and thereby track the user.
4. Data can be stored in the HttpSession as attributes. This data persists as long as the session is valid.
5. The validity of a session can be configured using following ways:
- Inactive Interval: If a session is not accessed for a configured time interval, it can be invalidated.
- Max Inactive Interval: A session will be forcibly invalidated after a configured maximum inactive interval.
- Manual Invalidation: A session can be manually invalidated by calling invalidate() method on HttpSession.
6. Session data can be used to store user specific information like login details, shopping cart data, etc and used across multiple requests.
7. However, excessive use of sessions can impact performance. Hence, sessions should only be used when required and data stored in sessions should be minimized.

The content summarizes key points about HttpSession and session tracking in Servlets in a formal tone with points and without any feelings or emojis as instructed. Please let me know if you would like me to modify or expand the content.