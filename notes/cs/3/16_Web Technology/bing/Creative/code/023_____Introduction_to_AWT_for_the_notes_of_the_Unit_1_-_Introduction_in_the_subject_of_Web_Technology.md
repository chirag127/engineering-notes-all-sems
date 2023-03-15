# Introduction to AWT

- AWT stands for **Abstract Window Toolkit**    , which is an **API** (Application Programming Interface) for creating **Graphical User Interface** (GUI) or windows-based applications in Java .
- AWT components are **platform-dependent** , which means they are displayed according to the view of the underlying operating system (OS)  .
- AWT is **heavyweight**, which means its components are using the resources of the OS.
- AWT is part of the **Java Foundation Classes** (JFC), which is the standard API for providing a GUI for a Java program.
- AWT provides various classes and interfaces for creating and managing windows, menus, buttons, text fields, labels, checkboxes, radio buttons, lists, dialogs, scrollbars, etc.  .
- AWT also provides classes and interfaces for handling events, graphics, fonts, colors, images, etc.  .
- AWT follows a **container-component** hierarchy, which means a container can contain components and other containers.
- AWT uses **native peers** , which are the OS-specific implementations of the AWT components .
- AWT uses **layout managers**, which are objects that control the size and position of the components within a container.
- AWT uses **delegation event model**, which means the source component delegates the responsibility of handling an event to a listener object.