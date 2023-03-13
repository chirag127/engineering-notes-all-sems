
### Session Tracking with Http Session in Servlets

* Session tracking is a technique used by web applications to maintain user's state or track user's activities across multiple requests or page views. 
* HttpSession is an interface in the Java Servlet API that provides a way to identify a user across multiple page requests. 
* It allows the servlet container to store information about a user and make it available to multiple servlets within the same application.
* The servlet container uses a cookie or URL rewriting to associate the session identifier with the user's request. 
* When the user sends a request, the servlet container looks for the session identifier and uses it to locate the session object associated with the user. 
* The session object contains all the information associated with the user's session, such as user preferences, shopping cart items, etc. 
* The session object is stored in the server's memory and is destroyed when the session expires or is invalidated.
* Mnemonics for session tracking with HttpSession in Servlets:
  * S - Store information about the user 
  * T - Track user's activities across multiple requests 
  * H - HttpSession interface in the Java Servlet API 
  * U - URL rewriting to associate the session identifier 
  * S - Session object contains all the information associated with the user's session 
  * I - Identify a user across multiple page requests 
  * O - Object is stored in the server's memory 
  * N - Notify the servlet container when the session expires or is invalidated.