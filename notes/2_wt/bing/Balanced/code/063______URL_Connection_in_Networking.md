#### URL Connection in Networking

A URL connection is a way to establish a communication link between a program and a resource identified by a URL. A URL connection can be used to read or write data from or to the resource, such as a web page, a file, or a database.

To create a URL connection, you need to:

- Create a URL object that represents the resource you want to connect to.
- Call the `openConnection()` method on the URL object to get a URLConnection object.
- Optionally, configure the URLConnection object by setting its properties or headers, such as the request method, the timeout, or the user-agent.
- If you want to write data to the resource, get an output stream from the URLConnection object by calling the `getOutputStream()` method, and write the data to the stream.
- If you want to read data from the resource, get an input stream from the URLConnection object by calling the `getInputStream()` method, and read the data from the stream.
- Close the input and output streams when you are done.

Here is an example of how to create a URL connection and read the content of a web page:

```java
import java.io.*;
import java.net.*;

public class URLConnectionExample {

  public static void main(String[] args) {
    try {
      // Create a URL object that represents the web page
      URL url = new URL("https://www.example.com");

      // Open a URL connection
      URLConnection urlConnection = url.openConnection();

      // Get an input stream from the URL connection
      InputStream inputStream = urlConnection.getInputStream();

      // Create a buffered reader to read the input stream
      BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));

      // Read and print the lines from the web page
      String line;
      while ((line = bufferedReader.readLine()) != null) {
        System.out.println(line);
      }

      // Close the buffered reader and the input stream
      bufferedReader.close();
      inputStream.close();
    } catch (IOException e) {
      // Handle the exception
      e.printStackTrace();
    }
  }
}
```