### URL Connection for the notes of the Unit 3 - Scripting in the subject of Web Technology

In the subject of Web Technology, one of the important topics is URL connection. In this topic, we learn about the process of establishing a connection to a URL through a Java program. Here are some important points to keep in mind while studying this topic:

- A URL (Uniform Resource Locator) is a reference to a web resource on the internet. It can be a web page, an image, a video, or any other type of resource.
- Establishing a connection to a URL is an important step in accessing its contents. This can be achieved using the URLConnection class in Java.
- The URLConnection class provides methods to set and retrieve request properties, connect to the URL, and read the response from the server.
- To establish a connection to a URL, we first create a URL object using the URL class in Java. We can then call the openConnection() method on this object to get a URLConnection object.
- The URLConnection object provides methods to set request properties such as the user agent, accept language, and content type. We can also set the request method (GET or POST) using the setRequestMethod() method.
- Once the request properties are set, we can call the connect() method to establish a connection to the URL.
- After the connection is established, we can read the response from the server using the getInputStream() method. This method returns an input stream that can be used to read the response bytes from the server.
- It is important to close the input stream and the connection after reading the response to free up system resources.

In conclusion, URL connection is an important topic in the subject of Web Technology. By understanding the process of establishing a connection to a URL through a Java program, we can effectively access the contents of web resources on the internet.