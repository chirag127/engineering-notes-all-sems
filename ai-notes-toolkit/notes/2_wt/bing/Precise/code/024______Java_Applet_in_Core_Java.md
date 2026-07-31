#### Java Applet in Core Java
Here is an example of a simple Java Applet that displays "Hello, World!" on the screen:

```java
import java.applet.Applet;
import java.awt.Graphics;

public class HelloWorld extends Applet {
   public void paint(Graphics g) {
      g.drawString("Hello, World!", 20, 20);
   }
}
```

To run this applet, you need to embed it in an HTML file and open it in a web browser that supports Java. Here is an example of an HTML file that embeds the above applet:

```html
<html>
   <body>
      <applet code="HelloWorld.class" width="200" height="200">
      </applet>
   </body>
</html>
```

Save the Java code in a file named `HelloWorld.java` and compile it using the `javac` command. Then, save the HTML code in a file named `hello.html` and open it in a web browser. You should see the message "Hello, World!" displayed on the screen.