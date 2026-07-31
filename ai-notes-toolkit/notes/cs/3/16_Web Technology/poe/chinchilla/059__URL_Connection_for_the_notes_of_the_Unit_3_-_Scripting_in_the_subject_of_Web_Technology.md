### URL Connection for the notes of the Unit 3 - Scripting in the subject of Web Technology

URL Connection is an essential concept in Web Technology that allows communication between a client and a server. In this unit, we will learn about the basics of URL Connection and how it works in scripting.

Here are the points that you need to focus on while studying about URL Connection in the unit:

1. URL Connection:
   - URL Connection is a class in Java that allows the client to communicate with the server over the internet by opening a connection.
   - It is used to send and receive data to and from a server through a URL.
   - URL Connection is a higher-level API than the Socket API and is used in web programming to connect to web servers.

2. URL:
   - URL (Uniform Resource Locator) is a string of characters that specifies the location of a resource on the internet.
   - It contains the protocol, hostname, port number, and resource path of the resource that is being accessed.
   
3. HttpURLConnection:
   - HttpURLConnection is a subclass of URL Connection class that is used to send and receive data to and from a web server over the internet.
   - It is used to establish and open a connection to the server, send requests, and receive responses.
   - It supports HTTP/1.1 and provides methods for handling HTTP headers, cookies, and redirects.

4. Methods of URL Connection:
   - getInputStream(): It returns an input stream that reads data from the server.
   - getOutputStream(): It returns an output stream that writes data to the server.
   - connect(): It establishes a connection to the server.
   - disconnect(): It terminates the connection to the server.

5. Handling Exceptions:
   - While using URL Connection, we need to handle exceptions like IOException, MalformedURLException, etc.
   - We can use try-catch blocks to handle these exceptions and display appropriate error messages to the user.

6. Examples:
   - We can use URL Connection to send GET and POST requests to a web server and receive responses.
   - We can also use it to download files from the internet or upload files to a web server.

In conclusion, URL Connection is an important concept in Web Technology that allows communication between a client and a server over the internet. By studying the basics of URL Connection and its methods, you can develop web applications that interact with web servers and provide a seamless user experience.