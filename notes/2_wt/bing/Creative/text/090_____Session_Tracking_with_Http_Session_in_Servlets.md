### Session Tracking with Http Session in Servlets

- Session tracking is a mechanism to maintain the state of a user across multiple requests.
- Http session is one of the techniques to implement session tracking in servlets.
- Http session is an object that is created by the servlet container and associated with a unique session ID.
- Http session can store any type of data as attributes, which can be accessed by any servlet that belongs to the same session.
- Http session is maintained by using cookies, URL rewriting, or hidden form fields.
- Http session has a predefined timeout period, after which it is invalidated by the servlet container.
- Http session provides methods to create, access, modify, and invalidate the session and its attributes. Some of the methods are:

  - `HttpSession getSession(boolean create)`: Returns the current session associated with the request, or creates a new session if none exists and the create parameter is true.
  - `String getId()`: Returns the unique session ID of the session.
  - `Object getAttribute(String name)`: Returns the value of the specified attribute from the session, or null if no such attribute exists.
  - `void setAttribute(String name, Object value)`: Sets the value of the specified attribute in the session, or removes the attribute if the value is null.
  - `void removeAttribute(String name)`: Removes the specified attribute from the session.
  - `void invalidate()`: Invalidates the session and unbinds any objects bound to it.