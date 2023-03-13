A Java applet is a small Java application that can be accessed on an Internet server, transported over the Internet, and can be automatically installed and run as part of a web document. An applet is a Java class that extends the java.applet.Applet class. An applet does not have a main() method and is viewed using a Java Virtual Machine (JVM) in a browser .

The following diagram illustrates the basic architecture of a Java applet in core Java:

#### Java Applet in Core Java

```
+------------------+        +-----------------+        +-----------------+
|                  |        |                 |        |                 |
|  Web Server      |        |  Web Browser    |        |  Java Applet    |
|                  |        |                 |        |                 |
|  +------------+  |        |  +-----------+  |        |  +-----------+  |
|  |            |  |        |  |           |  |        |  |           |  |
|  |  HTML Page |  |        |  |  HTML     |  |        |  |  Applet   |  |
|  |  with      |  |        |  |  Parser   |  |        |  |  Class    |  |
|  |  Applet Tag|  |        |  |           |  |        |  |           |  |
|  |            |  |        |  |           |  |        |  |           |  |
|  +------------+  |        |  +-----------+  |        |  +-----------+  |
|                  |        |                 |        |                 |
|  +------------+  |        |  +-----------+  |        |  +-----------+  |
|  |            |  |        |  |           |  |        |  |           |  |
|  |  Applet    |  |        |  |  JVM      |  |        |  |  GUI      |  |
|  |  Class     |  |        |  |           |  |        |  |  Toolkit  |  |
|  |  File      |  |        |  |           |  |        |  |           |  |
|  |            |  |        |  |           |  |        |  |           |  |
|  +------------+  |        |  +-----------+  |        |  +-----------+  |
|                  |        |                 |        |                 |
+------------------+        +-----------------+        +-----------------+
     |                          |    |                         |
     |                          |    |                         |
     |                          |    |                         |
     |                          |    |                         |
     |                          |    |                         |
     |                          |    |                         |
     |                          |    |                         |
     |                          |    |                         |
     |                          |    |                         |
     |                          |    |                         |
     |                          |    |                         |
     +--------------------------+    +-------------------------+
```

The diagram shows the following steps:

- The web server hosts an HTML page with an applet tag that specifies the applet class file.
- The web browser requests the HTML page from the web server.
- The web browser parses the HTML page and finds the applet tag.
- The web browser requests the applet class file from the web server.
- The web server sends the applet class file to the web browser.
- The web browser loads the applet class file into the JVM .
- The JVM creates an instance of the applet class and invokes its init() method to initialize the applet .
- The applet class creates its GUI using the GUI toolkit.
- The JVM invokes the applet's start() method to start the applet.
- The applet interacts with the user and performs its tasks.
- The JVM invokes the applet's stop() method to stop the applet when the user leaves the web page.
- The JVM invokes the applet's destroy() method to release the applet's resources when the browser is closed.