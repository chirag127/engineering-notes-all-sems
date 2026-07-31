### URL Connection

- URLConnection is an abstract class that represents a communication link between a Java application and a URL.
- URLConnection class provides methods to read and write data to and from any resource referenced by an URL object.
- URLConnection class also provides methods to configure the connection, such as setting the request method, the request properties, the timeout values, etc.
- URLConnection is the superclass of all classes that handle specific protocols, such as HttpURLConnection for HTTP, JarURLConnection for JAR files, etc.
- To obtain a URLConnection object, we need to create a URL object first, and then call the openConnection() method on it.
- For example, the following code creates a URLConnection object for the URL http://www.google.com:

```java
URL url = new URL("http://www.google.com");
URLConnection connection = url.openConnection();
```

- To configure the URLConnection object, we can use methods such as setRequestMethod(), setRequestProperty(), setConnectTimeout(), setReadTimeout(), etc.
- For example, the following code sets the request method to POST, the content type to application/json, and the connection timeout to 10 seconds:

```java
connection.setRequestMethod("POST");
connection.setRequestProperty("Content-Type", "application/json");
connection.setConnectTimeout(10000);
```

- To read the header fields of the URLConnection object, we can use methods such as getHeaderField(), getHeaderFieldKey(), getHeaderFields(), etc.
- For example, the following code prints the header fields and their values:

```java
Map<String, List<String>> headers = connection.getHeaderFields();
for (String key : headers.keySet()) {
  System.out.println(key + ": " + headers.get(key));
}
```

- To get an input stream and read data from the URLConnection object, we can use methods such as getInputStream(), getContent(), getContentEncoding(), getContentLength(), etc.
- For example, the following code reads the data from the input stream and prints it to the console:

```java
InputStream input = connection.getInputStream();
BufferedReader reader = new BufferedReader(new InputStreamReader(input));
String line;
while ((line = reader.readLine()) != null) {
  System.out.println(line);
}
reader.close();
```

- To get an output stream and write data to the URLConnection object, we need to set the doOutput property to true, and then use methods such as getOutputStream(), setFixedLengthStreamingMode(), setChunkedStreamingMode(), etc.
- For example, the following code writes a JSON string to the output stream:

```java
connection.setDoOutput(true);
connection.setFixedLengthStreamingMode(json.length());
OutputStream output = connection.getOutputStream();
output.write(json.getBytes());
output.close();
```

- To close the connection, we can use methods such as disconnect() for HttpURLConnection, or close() for JarURLConnection.
- For example, the following code closes the connection if it is an instance of HttpURLConnection:

```java
if (connection instanceof HttpURLConnection) {
  HttpURLConnection httpConnection = (HttpURLConnection) connection;
  httpConnection.disconnect();
}
```

- URLConnection class is useful for generic URLs, but for protocol-specific features, we should use the subclasses of URLConnection, such as HttpURLConnection, JarURLConnection, etc.
- For example, the following code casts the URLConnection object to HttpURLConnection, and then uses methods such as getResponseCode(), getResponseMessage(), etc:

```java
HttpURLConnection httpConnection = (HttpURLConnection) connection;
int responseCode = httpConnection.getResponseCode();
String responseMessage = httpConnection.getResponseMessage();
System.out.println("Response code: " + responseCode);
System.out.println("Response message: " + responseMessage);
```