### Session Tracking in Servlets

Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user (that is, requests originating from the same browser) across some period of time. Sessions are shared among the servlets accessed by a client.

There are four techniques used in session tracking:

- Cookies: A cookie is a small piece of information that is sent by the server to the client as part of the response header. The client stores the cookie and sends it back to the server with every subsequent request. The cookie can contain any information that the server wants to associate with the client, such as a session ID, a username, a shopping cart, etc. The server can use the cookie to retrieve the session information for the client.

- Hidden Form Field: A hidden form field is a special type of input element in an HTML form that is not visible to the user. The hidden form field can store any information that the server wants to associate with the client, such as a session ID, a username, a shopping cart, etc. The hidden form field is sent to the server along with the other form data when the user submits the form. The server can use the hidden form field to retrieve the session information for the client.

- URL Rewriting: URL rewriting is a technique that appends the session information to the end of the URL as a query string. For example, if the session ID is 1234, the URL can be rewritten as http://example.com/servlet?sid=1234. The server can use the query string to retrieve the session information for the client.

- HttpSession: HttpSession is an interface that defines an object that provides a way to identify a user across more than one page request or visit to a Web site and to store information about that user. The servlet container creates an HttpSession object for each client that requests a servlet. The servlet can use the HttpSession object to store and retrieve any information about the client, such as a session ID, a username, a shopping cart, etc. The servlet container ensures that the HttpSession object is accessible to all the servlets that belong to the same application and that have the same session ID.

Here is an example of how to use HttpSession to store and retrieve the username of a client in a servlet:

```java
//import the necessary packages
import javax.servlet.*;
import javax.servlet.http.*;

//create a servlet class that extends HttpServlet
public class SessionServlet extends HttpServlet {

  //override the doGet method to handle the GET request
  public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
  
    //get the HttpSession object associated with the request
    HttpSession session = request.getSession();
    
    //get the username parameter from the request
    String username = request.getParameter("username");
    
    //check if the username is null or empty
    if (username == null || username.isEmpty()) {
    
      //get the username attribute from the session
      username = (String) session.getAttribute("username");
      
      //check if the username is still null or empty
      if (username == null || username.isEmpty()) {
      
        //set the username to "Guest"
        username = "Guest";
      }
    }
    else {
    
      //set the username attribute in the session
      session.setAttribute("username", username);
    }
    
    //set the content type of the response to text/html
    response.setContentType("text/html");
    
    //get the PrintWriter object to write the response
    PrintWriter out = response.getWriter();
    
    //write the HTML code to display the username
    out.println("<html>");
    out.println("<head><title>Session Servlet</title></head>");
    out.println("<body>");
    out.println("<h1>Hello, " + username + "!</h1>");
    out.println("</body>");
    out.println("</html>");
    
    //close the PrintWriter object
    out.close();
  }
}
```