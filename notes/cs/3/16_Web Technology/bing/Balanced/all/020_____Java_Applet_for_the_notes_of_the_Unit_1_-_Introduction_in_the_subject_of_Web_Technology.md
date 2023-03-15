# Java Applet

- A Java applet is a small application written in the Java programming language, or another programming language that compiles to Java bytecode, and delivered to users in the form of Java bytecode .
- A Java applet can be transferred via the Internet and run by a Java-compatible web browser.
- The main difference between Java-based applications and applets is that applets are typically executed in an AppletViewer or Java-compatible web browser, while applications are executed by the Java Virtual Machine (JVM) directly.
- The user can launch the Java applet from a web page, and the applet is then executed within a JVM in a process separate from the web browser.
- The applet tag was used to embed the Java applet in the HTML document. It provided web applications with interactive and dynamic features that HTML couldn’t offer.
- An applet has limited functionality and access to the user's system, such as file system, network, and clipboard, for security reasons .
- An applet can communicate with other applets running on the same machine or different machines, as well as with the web server that hosts it.
- An applet can also use Java libraries and APIs, such as Swing, AWT, JDBC, RMI, etc., to enhance its functionality and appearance.
- An applet follows a life cycle that consists of four stages: initialization, start, stop, and destroy.
- An applet can be written by extending the java.applet.Applet class or implementing the java.applet.AppletStub and java.applet.AppletContext interfaces.