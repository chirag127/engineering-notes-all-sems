#### Layout managers in AWT

- A layout manager is an object that controls the size and position of the components within a container.
- AWT (Abstract Window Toolkit) is a Java package that provides classes and interfaces for creating and managing graphical user interfaces (GUIs).
- AWT provides five layout managers for general use: FlowLayout, BorderLayout, GridLayout, CardLayout, and GridBagLayout .
- Each layout manager has its own rules and strategies for arranging the components in a container.
- The default layout manager for a container depends on the type of the container. For example, the default layout manager for a Frame is BorderLayout, and the default layout manager for a Panel is FlowLayout.
- The layout manager can be changed by using the `container.setLayout` method, where `container` is the name of the container object and `setLayout` is the method that takes a layout manager object as a parameter.
- A custom layout manager can be created by implementing the `java.awt.LayoutManager` interface or extending an existing layout manager class.
- The following table summarizes the features and usage of the five AWT layout managers  :

| Layout Manager | Description | Usage |
| -------------- | ----------- | ----- |
| FlowLayout | Arranges the components in a left-to-right flow, wrapping to the next line when no more space is available. | Suitable for creating simple and dynamic layouts that can adjust to different container sizes and component alignments. |
| BorderLayout | Divides the container into five regions: north, south, east, west, and center. Each region can contain only one component. | Suitable for creating complex and static layouts that have a main component in the center and other components around it. |
| GridLayout | Arranges the components in a grid of rows and columns of equal size. The number of rows and columns can be specified or determined by the container size. | Suitable for creating regular and uniform layouts that can display multiple components of the same size and shape. |
| CardLayout | Arranges the components as a stack of cards, where only one card is visible at a time. The cards can be switched by using the `next`, `previous`, `first`, `last`, or `show` methods. | Suitable for creating dynamic and interactive layouts that can display different components based on user actions or events. |
| GridBagLayout | Arranges the components in a grid of rows and columns of variable size. The size and position of each component can be customized by using a `GridBagConstraints` object that specifies the constraints for the component. | Suitable for creating complex and flexible layouts that can display components of different sizes and shapes with fine-grained control. |