### URL Connection

- URLConnection is an abstract class that represents a communication link between a Java application and a URL.
- URLConnection class provides methods to read and write data to and from any resource referenced by an URL object.
- URLConnection class also provides methods to configure the connection, such as setting the request method, the request properties, the timeout values, etc.
- URLConnection is the superclass of all classes that handle specific protocols, such as HttpURLConnection for HTTP, JarURLConnection for JAR files, etc.
- To use URLConnection, the following steps are required:
  - Create a URL object for the desired resource.
  - Obtain a URLConnection object from the URL object by calling the openConnection() method.
  - Configure the URLConnection object according to the desired properties and features.
  - Read the header fields of the URLConnection object by calling the getHeaderField() method or its variants.
  - Get an input stream from the URLConnection object by calling the getInputStream() method and read data from the resource.
  - Optionally, get an output stream from the URLConnection object by calling the getOutputStream() method and write data to the resource.
  - Close the connection by calling the disconnect() method (for HttpURLConnection) or closing the streams (for other subclasses).

- Example of using URLConnection to connect to a web page and print its content:

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;

public class URLConnectionExample {

    public static void main(String[] args) {
        try {
            // create a URL object
            URL url = new URL("http://www.example.com");

            // obtain a URLConnection object
            URLConnection connection = url.openConnection();

            // get an input stream and wrap it in a BufferedReader
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));

            // read lines from the web page
            String line = null;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // close the reader
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```