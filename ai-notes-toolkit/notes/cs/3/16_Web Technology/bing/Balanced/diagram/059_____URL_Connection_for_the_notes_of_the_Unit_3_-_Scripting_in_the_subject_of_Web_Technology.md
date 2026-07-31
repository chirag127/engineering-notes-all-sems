### URL Connection

- URLConnection is an abstract class that represents a communication link between a Java application and a URL resource on the internet .
- URLConnection class provides methods to read and write data to and from any resource referenced by an URL object.
- URLConnection is the superclass of all classes that represent a connection between a Java application and a URL.
- The two subclasses of URLConnection are HttpURLConnection and JarURLConnection, which provide additional support for HTTP-specific and JAR-specific features respectively .
- To use URLConnection, the following steps are required :
  - Create a URL object for the desired resource.
  - Obtain a URLConnection object from the URL object by calling the openConnection() method.
  - Configure the URLConnection object by setting various properties and options, such as connection timeout, request method, request headers, etc.
  - Read the header fields of the URLConnection object by calling the getHeaderField() method or its variants.
  - Get an input stream from the URLConnection object by calling the getInputStream() method and read data from the resource.
  - Get an output stream from the URLConnection object by calling the getOutputStream() method and write data to the resource.
  - Close the connection by calling the disconnect() method (for HttpURLConnection) or the close() method (for JarURLConnection).