### Session Tracking with Http Session in Servlets

- Session tracking is a mechanism to maintain the state of a user across multiple requests or visits to a web application.
- HTTP is a stateless protocol, which means that each request is independent and does not remember any information from previous requests.
- Session tracking enables the web application to store and retrieve user-specific data, such as preferences, shopping cart items, authentication status, etc.
- One of the ways to implement session tracking is using HTTP session objects, which are provided by the servlet API.
- An HTTP session object is a server-side object that is associated with a unique identifier (session ID) and can store any type of data as attributes.
- The session ID is usually stored as a cookie in the client browser, or as a URL parameter if cookies are disabled.
- The servlet container creates a new session object for each user when the user first visits the web application, and assigns a session ID to it.
- The servlet container also maintains a mapping between the session ID and the session object, and provides methods to access and manipulate the session object.
- The servlet can use the `request.getSession()` method to get the current session object, or create a new one if it does not exist.
- The servlet can use the `session.setAttribute(name, value)` and `session.getAttribute(name)` methods to store and retrieve data as attributes in the session object.
- The servlet can use the `session.invalidate()` method to destroy the session object and remove it from the mapping.
- The servlet can use the `session.setMaxInactiveInterval(seconds)` and `session.getLastAccessedTime()` methods to control the lifetime of the session object.
- The session object is valid until one of the following conditions occurs:
  - The servlet calls the `session.invalidate()` method.
  - The user closes the browser or clears the cookies.
  - The session object expires due to inactivity or timeout.
- Some advantages of using HTTP session objects for session tracking are:
  - They are easy to use and do not require any extra coding or configuration.
  - They are secure and reliable, as the data is stored on the server and not exposed to the client.
  - They can store any type of data as attributes, not just strings.
- Some disadvantages of using HTTP session objects for session tracking are:
  - They consume server memory and resources, which may affect the performance and scalability of the web application.
  - They are not suitable for distributed or clustered environments, as the session data is not shared among different servers or instances.
  - They depend on the client browser's support for cookies or URL rewriting, which may not be available or consistent in some cases.

- A possible mnemonic to remember the methods of the session object is:

  - **GASIL**: Get, Attribute, Set, Invalidate, LastAccessedTime
  - **GASMI**: Get, Attribute, Set, MaxInactiveInterval, Invalidate

- A possible learning trick to understand the concept of session tracking is to compare it with a shopping mall:

  - When a user enters the mall, they are given a token (session ID) that identifies them uniquely.
  - The token is stored in their pocket (cookie) or attached to their clothes (URL parameter).
  - The mall has a locker room (session object) where the user can store their belongings (attributes) and access them later.
  - The user can visit different shops (servlets) in the mall and use their token to access their locker and retrieve or update their belongings.
  - The user can also leave the mall and come back later, as long as they have their token and their locker is not expired or removed.
  - The user can also discard their token and their locker by throwing them away (invalidate) or losing them (close browser or clear cookies).