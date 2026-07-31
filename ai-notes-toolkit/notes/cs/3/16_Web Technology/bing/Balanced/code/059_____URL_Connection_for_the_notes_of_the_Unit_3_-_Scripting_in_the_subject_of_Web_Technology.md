Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are some notes on URL Connection for Unit 3 - Scripting.

### URL Connection

- A URL connection is a way to establish a communication link between a program and a resource identified by a URL (Uniform Resource Locator).
- A URL connection can be used to read or write data from or to the resource, such as a web page, a file, or a database.
- A URL connection can also be used to get information about the resource, such as its content type, content length, last modified date, etc.
- To create a URL connection, you need to use the `openConnection()` method of the `URL` class, which returns an instance of the `URLConnection` class or one of its subclasses, such as `HttpURLConnection` or `HttpsURLConnection`.
- To use a URL connection, you need to follow these steps:
  - Create a `URL` object with the desired resource address.
  - Call the `openConnection()` method on the `URL` object to get a `URLConnection` object.
  - Set any connection parameters or request properties, such as the connection timeout, the request method, the request headers, etc.
  - Connect to the resource by calling the `connect()` method on the `URLConnection` object.
  - Read or write data from or to the resource by using the input stream or output stream of the `URLConnection` object.
  - Close the connection by calling the `disconnect()` method on the `URLConnection` object (only for HTTP connections).
- Here is an example of using a URL connection to read the content of a web page:

```java
import java.io.*;
import java.net.*;

public class URLConnectionExample {

  public static void main(String[] args) {
    try {
      // Create a URL object with the web page address
      URL url = new URL("https://www.example.com");

      // Open a URL connection
      URLConnection urlConnection = url.openConnection();

      // Get the input stream of the connection
      InputStream inputStream = urlConnection.getInputStream();

      // Create a buffered reader to read the input stream
      BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));

      // Read and print the content of the web page line by line
      String line;
      while ((line = bufferedReader.readLine()) != null) {
        System.out.println(line);
      }

      // Close the buffered reader and the input stream
      bufferedReader.close();
      inputStream.close();

    } catch (MalformedURLException e) {
      // Handle malformed URL exception
      e.printStackTrace();
    } catch (IOException e) {
      // Handle input/output exception
      e.printStackTrace();
    }
  }
}
```