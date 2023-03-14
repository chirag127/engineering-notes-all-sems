Layout managers in AWT are objects that control the size and position of components inside a container, such as a window or a panel. AWT provides five predefined layout managers: BorderLayout, FlowLayout, CardLayout, GridLayout, and GridBagLayout. Each layout manager has a different way of arranging components and handling window resizing events.

The following diagram illustrates the basic architecture of a layout manager in AWT:

```
+---------------------+
|      Container      |
|                     |
|  +---------------+  |
|  | LayoutManager |  |
|  +---------------+  |
|                     |
|  +-------------+    |
|  | Component 1 |    |
|  +-------------+    |
|                     |
|  +-------------+    |
|  | Component 2 |    |
|  +-------------+    |
|                     |
|        ...          |
|                     |
|  +-------------+    |
|  | Component n |    |
|  +-------------+    |
|                     |
+---------------------+
```

The container is the parent component that holds one or more child components. The container has a reference to a layout manager object that implements the LayoutManager interface. The layout manager is responsible for setting the size and position of each component in the container, according to its own layout algorithm. The container also has a list of components that it contains, and it invokes the layout manager's methods whenever it needs to layout or re-layout its components. The components are the child components that are added to the container, and they have properties such as preferred size, minimum size, maximum size, and alignment that affect how the layout manager arranges them.