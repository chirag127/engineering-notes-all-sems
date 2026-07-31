#### Java Applet in Core Java

- An applet is a small program that is designed to run within a web page.
- Applets are written in the Java programming language and are executed by a Java Virtual Machine (JVM) within the web browser.
- Applets can be used to create interactive features on a web page, such as games, animations, and calculators.
- To create an applet, you need to extend the `java.applet.Applet` class and override its methods to provide the desired functionality.
- Applets are embedded in a web page using the `<applet>` tag or the `<object>` tag.
- Applets have a number of restrictions for security reasons. For example, they cannot access the local file system or make network connections to any host other than the one from which the applet was loaded.
- Applets have largely been replaced by other technologies, such as JavaScript and HTML5, for creating interactive content on the web.
- However, applets can still be useful for certain applications, such as scientific simulations or educational tools.

Here is an example of a simple applet that displays a message:

```java
import java.applet.Applet;
import java.awt.Graphics;

public class HelloWorldApplet extends Applet {
    public void paint(Graphics g) {
        g.drawString("Hello, world!", 50, 25);
    }
}
```

This applet can be embedded in a web page using the following HTML code:

```html
<applet code="HelloWorldApplet.class" width="200" height="50">
</applet>
```

Advantages of using Java Applets:
- Applets can run on any platform that has a JVM, making them highly portable.
- Applets can be easily distributed over the internet.
- Applets can provide a rich and interactive user experience.

Disadvantages of using Java Applets:
- Applets require a JVM to be installed on the user's computer, which can be a barrier to adoption.
- Applets have a number of security restrictions, which can limit their functionality.
- Applets have largely been replaced by other technologies for creating interactive content on the web.

Mnemonic for remembering the lifecycle methods of an applet: **I** **P**lay **S**occer **D**uring **S**chool **H**ours
- **I**nit: Called when the applet is first loaded.
- **P**aint: Called when the applet needs to be repainted.
- **S**tart: Called when the applet is started.
- **D**estroy: Called when the applet is being destroyed.
- **S**top: Called when the applet is being stopped.
- **H**ide: Called when the applet is being hidden.