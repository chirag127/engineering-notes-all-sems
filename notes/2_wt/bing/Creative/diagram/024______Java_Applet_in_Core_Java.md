An applet is a small Java application that can be accessed on an Internet server, transported over the Internet, and can be automatically installed and run as part of a web document . An applet is a Java class that extends the java.applet.Applet class . An applet does not have a main() method and is viewed using a Java Virtual Machine (JVM) . An applet is typically embedded inside an HTML page using the <applet> tag .

A possible ASCII diagram for a Java applet in core Java is:

#### Java Applet in Core Java

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Web Server     |       |  Web Browser    |       |  Java Applet    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  HTML page      |       |  HTML page      |       |  Applet class   |
|  with applet tag|       |  with applet tag|       |  extends Applet |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Applet code    |       |  Applet code    |       |  init()         |
|  (.class file)  |       |  (.class file)  |       |  start()        |
|                 |       |                 |       |  paint()        |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Applet resources|      |  Applet resources|      |  stop()         |
|  (images, sounds, etc.) | (images, sounds, etc.) |  destroy()      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
     |  ^                    |  ^                    |  ^
     |  |                    |  |                    |  |
     |  |                    |  |                    |  |
     |  |                    |  |                    |  |
     |  |                    |  |                    |  |
     v  |                    v  |                    v  |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Internet       |       |  JVM            |       |  Applet Viewer  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```