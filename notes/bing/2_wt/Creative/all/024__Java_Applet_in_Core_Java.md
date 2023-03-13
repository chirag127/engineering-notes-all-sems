#### Java Applet in Core Java

- An applet is a small Java program that runs inside a web browser or an applet viewer.
- An applet can perform various tasks such as animation, calculation, games, etc. that enhance the user experience of a web page.
- An applet is different from a standalone Java application in the following ways:
  - An applet does not have a main method, but an init method that is invoked by the browser or the applet viewer when the applet is loaded.
  - An applet does not use the standard output stream (System.out) or the standard error stream (System.err) for displaying messages, but the graphics methods of the java.awt package or the showStatus method of the java.applet.Applet class.
  - An applet cannot access the local file system or the network resources of the client machine, unless it is signed by a trusted authority or granted permission by the user.
  - An applet has a limited life cycle that is controlled by the browser or the applet viewer. The life cycle methods are init, start, stop, and destroy.
- To create an applet, one needs to do the following steps:
  - Write a Java class that extends the java.applet.Applet class or implements the java.applet.AppletStub and java.applet.AppletContext interfaces.
  - Override the init method to initialize the applet and the paint method to draw the applet on the screen. Optionally, override the start, stop, and destroy methods to handle the applet's life cycle events.
  - Compile the Java class and generate a bytecode file (.class) with the same name as the class.
  - Write an HTML file that contains an <applet> tag or an <object> tag that specifies the name and location of the bytecode file, the width and height of the applet, and any parameters that the applet needs.
  - Save the HTML file and the bytecode file in the same directory or in a subdirectory of the web server's document root.
  - Load the HTML file in a web browser or an applet viewer and see the applet in action.
- An example of a simple applet that displays "Hello, world!" on the screen is given below:

```java
// HelloWorldApplet.java
import java.applet.Applet;
import java.awt.Graphics;

public class HelloWorldApplet extends Applet {
  public void init() {
    // initialization code
  }

  public void paint(Graphics g) {
    // drawing code
    g.drawString("Hello, world!", 50, 50);
  }
}
```

```html
<!-- HelloWorldApplet.html -->
<html>
<head>
  <title>Hello, world!</title>
</head>
<body>
  <applet code="HelloWorldApplet.class" width="200" height="100">
  </applet>
</body>
</html>
```
- Some advantages of using applets are:
  - Applets can run on any platform that supports Java and has a web browser or an applet viewer.
  - Applets can interact with the web page that contains them and with other applets on the same page.
  - Applets can provide dynamic and interactive content that enhances the user experience of a web page.
- Some disadvantages of using applets are:
  - Applets require the user to have a Java-enabled browser or an applet viewer installed on their machine.
  - Applets may take longer to load and run than static content or other scripting languages.
  - Applets may pose security risks if they are not verified or trusted by the user or the browser.
  - Applets are not widely used anymore as they are replaced by other technologies such as Java Web Start, JavaFX, or HTML5.