#### URL Connection in Networking

- A URL (Uniform Resource Locator) is a unique identifier used to locate a resource on the Internet. It is also referred to as a web address.
- A URL consists of multiple parts, such as a protocol, a domain name, a path, and a query string, that tell a web browser how and where to retrieve a resource.
- For example, the URL https://docs.oracle.com/javase/tutorial/networking/urls/connecting.html has the following parts:

| Part | Value |
| --- | --- |
| Protocol | https |
| Domain name | docs.oracle.com |
| Path | /javase/tutorial/networking/urls/connecting.html |
| Query string | None |

- A URLConnection is a Java class that represents a connection between a Java application and a URL.
- A URLConnection can be used to read from and write to the resource pointed by the URL, as well as to access the header fields and other properties of the connection.
- A URLConnection can be obtained by calling the openConnection() method of the URL class.
- For example, the following code snippet creates a URLConnection object for the URL https://www.example.com/index.html and prints the content type of the resource:

```java
import java.net.*;
import java.io.*;

public class URLConnectionExample {
  public static void main(String[] args) {
    try {
      // Create a URL object
      URL url = new URL("https://www.example.com/index.html");
      
      // Open a connection to the URL
      URLConnection urlConnection = url.openConnection();
      
      // Get the content type of the resource
      String contentType = urlConnection.getContentType();
      
      // Print the content type
      System.out.println("Content type: " + contentType);
    } catch (MalformedURLException e) {
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

- A URLConnection is an abstract class that has many subclasses for different protocols, such as HttpURLConnection, JarURLConnection, and FtpURLConnection.
- A URLConnection provides methods to control and interact with the connection, such as:

  - setRequestProperty(String key, String value): Sets a general request property to be used in the connection.
  - getHeaderField(String name): Returns the value of the named header field in the response.
  - getInputStream(): Returns an input stream that reads from the connection.
  - getOutputStream(): Returns an output stream that writes to the connection.
  - connect(): Opens a communication link to the resource.
  - disconnect(): Closes the connection to the resource.

- A URLConnection can be used for various purposes, such as:

  - Downloading files from a web server.
  - Uploading files to a web server.
  - Sending and receiving data using HTTP methods (GET, POST, PUT, DELETE, etc.).
  - Parsing HTML documents using a HTML parser.
  - Accessing resources inside a JAR file.

- A mnemonic to remember the parts of a URL is: **P**rotocol **D**omain **P**ath **Q**uery, or **PDPQ**.
- A mnemonic to remember the methods of a URLConnection is: **S**et **R**equest **P**roperty, **G**et **H**eader **F**ield, **G**et **I**nput **S**tream, **G**et **O**utput **S**tream, **C**onnect, **D**isconnect, or **SRPGIGCD**.