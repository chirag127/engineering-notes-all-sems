### Session Tracking with Http Session in Servlets

- Session tracking is the process of remembering and documenting customer conversions over time.
- Session tracking allows the server to keep track of successive requests made by the same client.
- Session tracking can be done by the server using the HttpSession interface .
- The HttpSession interface provides methods to store, retrieve, and remove attributes associated with a session .
- The session is created between an HTTP client and an HTTP server by the servlet container using HttpSession.
- The servlet container assigns a unique session ID to each session object .
- The session ID is maintained across multiple requests to the server by the client.
- The session ID can be passed in different ways, such as cookies, URL rewriting, or hidden form fields.
- The session object can be obtained by calling the getSession() method of HttpServletRequest.
- The session object will be available to all of the servlets and JSPs that the user accesses until the session is closed due to timeout or error.
- The session object can be invalidated by calling the invalidate() method of HttpSession.

#### Advantages of Session Tracking with Http Session in Servlets

- It is easy to implement and use.
- It is secure and reliable as the session data is stored on the server side.
- It can store any type of object as an attribute.
- It can handle multiple sessions for different clients.

#### Disadvantages of Session Tracking with Http Session in Servlets

- It consumes server memory and resources.
- It may not work if the client disables cookies or changes browsers.
- It may not be scalable for large applications with many concurrent sessions.

#### Example of Session Tracking with Http Session in Servlets

```java
// FirstServlet.java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
public class FirstServlet extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
    // Create a session object if it is already not  created.
    HttpSession session = request.getSession(true);
    // Get session creation time.
    Date createTime = new Date(session.getCreationTime());
    // Get last access time of this web page.
    Date lastAccessTime = new Date(session.getLastAccessedTime());
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
    String title = "Welcome Back to my website";
    Integer visitCount = new Integer(0);
    String visitCountKey = new String("visitCount");
    String userIDKey = new String("userID");
    String userID = new String("ABCD");
    // Check if this is new comer on your web page.
    if (session.isNew()){
      title = "Welcome to my website";
      session.setAttribute(userIDKey, userID);
    } else {
      visitCount = (Integer)session.getAttribute(visitCountKey);
      visitCount = visitCount + 1;
      userID = (String)session.getAttribute(userIDKey);
    }
    session.setAttribute(visitCountKey,  visitCount);
    out.println("<!DOCTYPE html>\n" +
                "<html>\n" +
                "<head><title>" + title + "</title></head>\n" +
                "<body BGCOLOR=\"#FDF5E6\">\n" +
                "<h1 ALIGN=\"CENTER\">" + title + "</h1>\n" +
                "<h2 ALIGN=\"CENTER\">Session Infomation</h2>\n" +
                "<table BORDER=1 ALIGN=\"CENTER\">\n" +
                "<tr BGCOLOR=\"#FFAD00\">\n" +
                "  <th>Info Type<th>Value\n" +
                "<tr>\n" +
                "  <td>ID\n" +
                "  <td>" + session.getId() + "\n" +
                "<tr>\n" +
                "  <td>Creation Time\n" +
                "  <td>" + createTime + "\n" +
                "<tr>\n" +
                "  <td>Time of Last Access\n" +
                "  <td>" + lastAccessTime + "\n" +
                "<tr>\n" +
                "  <td>User ID\n" +
                "  <td>" + userID + "\n" +
                "<tr>\n" +
                "  <td>Number of visits\n" +