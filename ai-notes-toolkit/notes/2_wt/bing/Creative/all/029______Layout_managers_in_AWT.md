#### Layout managers in AWT

- Layout managers are classes that implement the `java.awt.LayoutManager` interface and control the size and position of components within a container.
- AWT provides five predefined layout managers: `FlowLayout`, `BorderLayout`, `GridLayout`, `CardLayout`, and `GridBagLayout`  .
- Each layout manager has its own rules and constraints for arranging components in different ways.
- The default layout manager for a container depends on the type of the container. For example, the default layout manager for a `Frame` is `BorderLayout`, while the default layout manager for a `Panel` is `FlowLayout`.
- To change the layout manager of a container, use the `container.setLayout(layout)` method, where `layout` is an instance of a layout manager class.
- To add a component to a container using a layout manager, use the `container.add(component)` method, or the `container.add(component, constraints)` method if the layout manager requires additional constraints.
- To remove a component from a container using a layout manager, use the `container.remove(component)` method, or the `container.removeAll()` method to remove all components.
- To learn more about each layout manager and see examples of how to use them, refer to the following pages:

  - [BorderLayout](https://docs.oracle.com/javase/tutorial/uiswing/layout/border.html)
  - [BoxLayout](https://docs.oracle.com/javase/tutorial/uiswing/layout/box.html)
  - [CardLayout](https://docs.oracle.com/javase/tutorial/uiswing/layout/card.html)
  - [FlowLayout](https://docs.oracle.com/javase/tutorial/uiswing/layout/flow.html)
  - [GridBagLayout](https://docs.oracle.com/javase/tutorial/uiswing/layout/gridbag.html)
  - [GridLayout](https://docs.oracle.com/javase/tutorial/uiswing/layout/grid.html)
  - [GroupLayout](https://docs.oracle.com/javase/tutorial/uiswing/layout/group.html)
  - [SpringLayout](https://docs.oracle.com/javase/tutorial/uiswing/layout/spring.html)