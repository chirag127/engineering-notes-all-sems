### AWT controls

- AWT stands for Abstract Window Toolkit, which is a set of APIs for developing graphical user interfaces or web applications in Java .
- AWT controls are components that allow a user to interact with the application in various ways, such as buttons, text fields, checkboxes, lists, etc .
- AWT controls are subclasses of the java.awt.Component class, which is the root class for all AWT components .
- AWT controls can be grouped into two categories: lightweight and heavyweight .
  - Lightweight controls are those that do not have a native peer, which means they are drawn and handled by Java code only. Examples of lightweight controls are Label, Button, Checkbox, etc .
  - Heavyweight controls are those that have a native peer, which means they are drawn and handled by the underlying platform's windowing system. Examples of heavyweight controls are Frame, Dialog, FileDialog, etc .
- AWT controls can be added to containers, which are components that can hold other components. Containers are subclasses of the java.awt.Container class, which is a subclass of the java.awt.Component class .
- AWT containers can be grouped into two categories: top-level and intermediate .
  - Top-level containers are those that have a title bar, border, and menu bar. They are independent windows that can be displayed on the screen. Examples of top-level containers are Frame, Dialog, and FileDialog .
  - Intermediate containers are those that do not have a title bar, border, or menu bar. They are used to organize and layout other components within a top-level container. Examples of intermediate containers are Panel, ScrollPane, and Applet .
- AWT controls can be arranged and aligned within a container using layout managers, which are objects that implement the java.awt.LayoutManager interface. Layout managers are responsible for determining the size and position of the components within a container .
- AWT provides several predefined layout managers, such as BorderLayout, FlowLayout, GridLayout, CardLayout, and GridBagLayout .
- AWT controls can respond to user events, such as mouse clicks, keyboard inputs, etc. Events are objects that represent the occurrence of an action or a change of state in the application .
- AWT supports two types of event handling mechanisms: event delegation model and event inheritance model .
  - Event delegation model is the preferred way of handling events in AWT. It is based on the principle of separating the event source from the event listener. The event source is the component that generates the event, and the event listener is the object that receives and processes the event. The event source and the event listener are connected by an event adapter, which is an object that implements a specific event listener interface .
  - Event inheritance model is the older way of handling events in AWT. It is based on the principle of inheriting the event handling methods from the java.awt.Component class or its subclasses. The event handling methods are defined by the java.awt.event.ComponentListener interface, which is implemented by the java.awt.Component class. The event handling methods are overridden by the subclasses of the java.awt.Component class to provide custom event handling logic .