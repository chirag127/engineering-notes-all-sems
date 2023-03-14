#### Introduction to AWT in Core Java

AWT (Abstract Window Toolkit) is an API that is used to develop either GUI or window-based applications in Java. AWT components are platform-dependent which implies that they are displayed according to the view of the operating system. AWT is heavy weight i.e. its components are using the resources of underlying operating system (OS). 

AWT provides a common set of tools for graphical user interface design that work on a variety of platforms. The user interface elements provided by the AWT are implemented using each platform's native GUI toolkit, thereby preserving the look and feel of each platform. This is one of the AWT's strongest points. The disadvantage of such an approach is the fact that a graphical user interface designed on one platform may look different when displayed on another platform. 

A graphical user interface is built of graphical elements called components. Typical components include such items as buttons, scrollbars, and text fields. Components allow the user to interact with the program and provide the user with visual feedback about the state of the program. In the AWT, all user interface components are instances of class Component or one of its subtypes. 

Components do not stand alone, but rather are found within containers. Containers contain and control the layout of components. Containers are themselves components, and can thus be placed inside other containers. 

The following diagram illustrates the basic architecture of AWT in Core Java:

```
+---------------------+
|       Object        |
+---------------------+
          ^
          |
+---------------------+
|      Component      |
+---------------------+
          ^
          |
+---------------------+
|      Container      |
+---------------------+
          ^
          |
+---------------------+
|  Window  |  Panel   |
+---------------------+
          ^
          |
+---------------------+
|       Frame        |
+---------------------+
```

: Java AWT Tutorial - javatpoint
: Introduction to the AWT | InfoWorld
: Introduction to AWT - Core java tutorial for beginners