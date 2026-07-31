An applet is a small Java application that can be accessed on an Internet server, transported over the Internet, and can be automatically installed and run as part of a web document . An applet is a Java class that extends the java.applet.Applet class . An applet does not have a main() method and is viewed using a Java Virtual Machine (JVM) .

A Java applet in core Java can be represented by the following diagram:

#### Java Applet in Core Java

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Web Browser    |      |  Web Server     |      |  Java Applet    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  HTML Page      |      |  HTML Page      |      |  Applet Class   |
|  with <applet>  |      |  with <applet>  |      |                 |
|  tag            |      |  tag            |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  JVM            |<---->|  JVM            |<---->|  JVM            |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The diagram shows the following steps:

- The web browser requests an HTML page from the web server that contains an <applet> tag.
- The web server sends the HTML page to the web browser.
- The web browser parses the HTML page and finds the <applet> tag that specifies the name and location of the applet class.
- The web browser requests the applet class from the web server.
- The web server sends the applet class to the web browser.
- The web browser loads the applet class into the JVM and invokes its init() method to initialize the applet.
- The web browser displays the applet as part of the web page.