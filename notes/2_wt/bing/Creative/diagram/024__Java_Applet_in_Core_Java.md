#### Java Applet in Core Java

A Java applet is a special kind of Java program that runs in a Java enabled browser. It is typically embedded inside a web page and can be automatically installed and run as part of a web document. An applet does not have a main () method, but instead it has a lifecycle that consists of four methods: init (), start (), stop (), and destroy (). An applet class must extend the java.applet.Applet class, which provides the necessary support for applet execution, such as loading and displaying images and playing audio clips. An applet can also use the Abstract Window Toolkit (AWT) classes to create a graphical user interface (GUI) with components such as buttons, labels, text fields, etc.

The following diagram illustrates the basic architecture of a Java applet in Core Java:

```
+------------------+       +-----------------+
| Web Browser      |       | Web Server      |
|                  |       |                 |
| +--------------+ |       | +-------------+ |
| | HTML Page    | |       | | HTML Page   | |
| |              | |       | |             | |
| | +----------+ | |       | | +---------+ | |
| | | Applet   | | |       | | | Applet  | | |
| | |          | | |       | | |         | | |
| | | +------+ | | |       | | | +-----+ | | |
| | | | AWT  | | | |       | | | | AWT | | | |
| | | |      | | | |       | | | |     | | | |
| | | +------+ | | |       | | | +-----+ | | |
| | +----------+ | |       | | +---------+ | |
| +--------------+ |       | +-------------+ |
+------------------+       +-----------------+
         |                         |
         |                         |
         +-------------------------+
               Internet
```