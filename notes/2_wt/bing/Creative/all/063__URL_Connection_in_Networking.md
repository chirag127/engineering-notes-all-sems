#### URL Connection in Networking

- A URL (Uniform Resource Locator) is a unique identifier used to locate a resource on the Internet. It is also referred to as a web address .
- A URL is composed of different parts, some mandatory and others optional. The most important parts are highlighted on the URL below:

  ```
  scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]
  ```

  - The scheme indicates the protocol that the browser must use to request the resource. Usually for websites the protocol is HTTPS or HTTP.
  - The authority includes both the domain name and the port, separated by a colon. The domain name indicates which web server is being requested. The port specifies which network port to use to make the connection.
  - The path specifies the location of the resource within the web server. It can be a file, a directory, or a query.
  - The query contains additional parameters that are sent to the web server along with the request. It is commonly used for search results.
  - The fragment identifies a specific part of the resource, such as a section in an HTML document. It is not sent to the web server, but processed by the browser.

- A URL connection is a way of establishing a communication link between a Java program and a URL over the network .
- To create a URL connection, you need to first create a URL object using the URL constructor that takes a string representation of the URL as an argument. For example:

  ```java
  URL url = new URL("https://www.example.com");
  ```

- Then, you can call the openConnection method on the URL object to get a URLConnection object, or one of its protocol-specific subclasses, such as HttpURLConnection. For example:

  ```java
  URLConnection urlConnection = url.openConnection();
  ```

- The URLConnection object allows you to read from and write to the resource specified by the URL. It also provides various methods to access the properties and headers of the resource.
- To initiate the connection, you need to call the connect method on the URLConnection object. This method is implicitly called by other methods that require the connection to be established, such as getInputStream or getOutputStream. For example:

  ```java
  urlConnection.connect();
  ```

- To read from the resource, you can use the getInputStream method to get an InputStream object, and then use a BufferedReader to read the data line by line. For example:

  ```java
  InputStream inputStream = urlConnection.getInputStream();
  BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
  String line;
  while ((line = bufferedReader.readLine()) != null) {
    System.out.println(line);
  }
  bufferedReader.close();
  ```

- To write to the resource, you need to set the doOutput property of the URLConnection object to true, and then use the getOutputStream method to get an OutputStream object, and then use a PrintWriter to write the data. For example:

  ```java
  urlConnection.setDoOutput(true);
  OutputStream outputStream = urlConnection.getOutputStream();
  PrintWriter printWriter = new PrintWriter(outputStream);
  printWriter.println("Hello, world!");
  printWriter.close();
  ```

- To access the properties and headers of the resource, you can use various methods of the URLConnection object, such as getContentLength, getContentType, getLastModified, getHeaderField, etc. For example:

  ```java
  int contentLength = urlConnection.getContentLength();
  String contentType = urlConnection.getContentType();
  long lastModified = urlConnection.getLastModified();
  String server = urlConnection.getHeaderField("Server");
  ```

- A URL connection is an HTTP-centric class; that is, many of its methods are useful only when you are working with HTTP URLs. However, most URL protocols allow you to read from and write to the connection.
- A URL connection is a low-level way of interacting with web resources. For higher-level abstractions, you can use other classes, such as HttpClient, HttpUrlConnection, or Jsoup.