

### Session Tracking with Http Session

* Session tracking is a process used to maintain the state of a user's interaction with a web application over multiple requests.
* HTTP session tracking is a technique used by web applications to store user's session data across multiple requests.
* Servlets provide a convenient way to maintain session data. They use an object called HttpSession to store session data.
* HttpSession objects are stored in memory on the web server and are identified by a unique session ID.
* The session ID is sent to the client in a cookie or URL parameter and is used to identify the user's session on subsequent requests.
* Servlets can store arbitrary objects in the session using the setAttribute() and getAttribute() methods.
* The session data is removed when the session is invalidated or when the web application is shut down.