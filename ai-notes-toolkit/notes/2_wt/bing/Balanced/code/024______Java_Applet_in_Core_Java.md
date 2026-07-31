#### Java Applet in Core Java

An applet is a small Java application that can be accessed on an Internet server, transported over the Internet, and can be automatically installed and run as part of a web document . An applet is a special kind of Java program that runs in a Java enabled browser. An applet is a Java class that extends the `java.applet.Applet` class . An applet does not have any `main()` method . It is viewed using JVM. JVM creates an instance of the applet class and invokes `init()` method to initialize an applet.

To write code for a Java applet in core Java, you need to follow these steps:

- Create a class that extends the `java.applet.Applet` class and override the `paint()` method to draw something on the applet window.
- Compile the class and create a `.class` file.
- Create an HTML file that embeds the applet using the `<applet>` tag and specifies the applet class name, width, height, and other parameters.
- Save the HTML file and the `.class` file in the same directory.
- Open the HTML file in a Java enabled browser to view the applet.

For example, the following code creates a simple applet that displays "Hello World" on the applet window:

```java
// HelloWorldApplet.java
import java.applet.Applet;
import java.awt.Graphics;

public class HelloWorldApplet extends Applet {
  public void paint(Graphics g) {
    g.drawString("Hello World", 50, 50);
  }
}
```

```html
<!-- HelloWorldApplet.html -->
<html>
<head>
  <title>Hello World Applet</title>
</head>
<body>
  <applet code="HelloWorldApplet.class" width="200" height="100">
  </applet>
</body>
</html>
```