#### URL Connection in Networking

- A URL (Uniform Resource Locator) is a unique identifier used to locate a resource on the Internet. It is also referred to as a web address.
- A URL consists of multiple parts -- including a protocol, domain name, path, port, reference, and query -- that tell a web browser how and where to retrieve a resource .
- For example, the URL `https://www.example.com:8080/index.html#section1?name=John` has the following components:
  - Protocol: `https` indicates the secure hypertext transfer protocol
  - Domain name: `www.example.com` identifies the server that hosts the resource
  - Port: `8080` specifies the network port to use to make the connection
  - Path: `/index.html` indicates the specific file or page within the domain
  - Reference: `#section1` points to a named anchor in the HTML file
  - Query: `?name=John` provides additional parameters or search criteria for the resource
- A URLConnection is a Java class that represents a connection between a Java application and a URL .
- A URLConnection allows the application to read from and write to the resource, as well as to access various properties and headers of the resource.
- To create a URLConnection, the application first needs to create a URL object and then call its `openConnection` method.
- For example, the following code creates a URLConnection to the site `example.com`:

```java
import java.net.*;
import java.io.*;

public class URLConnectionExample {
  public static void main(String[] args) throws Exception {
    // Create a URL object
    URL url = new URL("https://www.example.com");
    // Open a connection to the URL
    URLConnection urlConnection = url.openConnection();
    // Connect to the resource
    urlConnection.connect();
    // Do something with the connection ...
  }
}
```

- A URLConnection is an abstract class that has many subclasses for different protocols, such as HttpURLConnection, JarURLConnection, and FileURLConnection.
- Depending on the protocol, a URLConnection may support different features and methods, such as setting request methods, headers, timeouts, caching, etc.
- A URLConnection can also be cast to a protocol-specific subclass to access more functionality.
- For example, the following code casts a URLConnection to a HttpURLConnection and sets the request method to `GET`:

```java
import java.net.*;
import java.io.*;

public class HttpURLConnectionExample {
  public static void main(String[] args) throws Exception {
    // Create a URL object
    URL url = new URL("https://www.example.com");
    // Open a connection to the URL
    URLConnection urlConnection = url.openConnection();
    // Cast the connection to a HttpURLConnection
    HttpURLConnection httpURLConnection = (HttpURLConnection) urlConnection;
    // Set the request method to GET
    httpURLConnection.setRequestMethod("GET");
    // Do something with the connection ...
  }
}
```

- A URLConnection can be used to read from or write to the resource using input and output streams.
- For example, the following code reads the content of a web page using a BufferedReader:

```java
import java.net.*;
import java.io.*;

public class URLConnectionReader {
  public static void main(String[] args) throws Exception {
    // Create a URL object
    URL url = new URL("https://www.example.com");
    // Open a connection to the URL
    URLConnection urlConnection = url.openConnection();
    // Get an input stream from the connection
    InputStream inputStream = urlConnection.getInputStream();
    // Create a buffered reader to read from the input stream
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
    // Read each line from the buffered reader and print it
    String line;
    while ((line = bufferedReader.readLine()) != null) {
      System.out.println(line);
    }
    // Close the buffered reader and the input stream
    bufferedReader.close();
    inputStream.close();
  }
}
```

- Some possible mnemonics and learning tricks for URL connection in networking are:
  - URL: U (use) R (resource) L (locator) to find a resource on the Internet
  - URL components: P (protocol) D (domain) P (port) P (path) R (reference) Q (query)
  - URLConnection: U (use) R (resource) L (