# URL Connection

- URLConnection is an abstract class that represents a communication link between a Java application and a URL.
- URLConnection class provides methods to access and manipulate the properties of the URL, such as the header fields, the content type, the content length, the content encoding, etc.
- URLConnection class also provides methods to get input and output streams to read and write data to and from the URL resource.
- URLConnection class has two subclasses: HttpURLConnection and JarURLConnection, which provide additional support for HTTP and JAR protocols respectively.

## How to use URLConnection

- To use URLConnection, we need to create a URL object for the desired URL, and then call the openConnection() method on it to obtain a URLConnection object.
- For example, the following code creates a URL object for the Google homepage, and then opens a connection to it:

```java
URL url = new URL("http://www.google.com");
URLConnection connection = url.openConnection();
```

- We can configure the URLConnection object by setting various properties, such as the connection timeout, the request method, the request properties, etc.
- For example, the following code sets the connection timeout to 10 seconds, the request method to GET, and adds a user-agent request property:

```java
connection.setConnectTimeout(10000);
connection.setRequestMethod("GET");
connection.setRequestProperty("User-Agent", "Mozilla/5.0");
```

- We can read the header fields of the URLConnection object by using the getHeaderField() or getHeaderFields() methods.
- For example, the following code prints the content type and the content length of the URL resource:

```java
System.out.println("Content-Type: " + connection.getHeaderField("Content-Type"));
System.out.println("Content-Length: " + connection.getHeaderField("Content-Length"));
```

- We can get an input stream from the URLConnection object by using the getInputStream() method, and then read data from the URL resource.
- For example, the following code reads and prints the HTML content of the URL resource:

```java
InputStream inputStream = connection.getInputStream();
BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
String line;
while ((line = reader.readLine()) != null) {
    System.out.println(line);
}
reader.close();
```

- We can get an output stream from the URLConnection object by using the getOutputStream() method, and then write data to the URL resource.
- For example, the following code writes some data to the URL resource using a POST request:

```java
connection.setDoOutput(true); // enable output
OutputStream outputStream = connection.getOutputStream();
BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(outputStream));
writer.write("name=John&age=25");
writer.flush();
writer.close();
```

- We can close the connection by calling the disconnect() method on the URLConnection object.
- For example, the following code closes the connection:

```java
connection.disconnect();
```