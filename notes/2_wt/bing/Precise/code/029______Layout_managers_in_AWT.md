#### Layout managers in AWT

- AWT (Abstract Window Toolkit) is a Java package that provides a platform-independent interface for creating Graphical User Interfaces (GUIs).
- Layout managers are used to arrange components in a container.
- AWT provides several layout managers, including `BorderLayout`, `FlowLayout`, `GridLayout`, `CardLayout`, and `GridBagLayout`.
- Each layout manager has its own rules for arranging components.
- `BorderLayout` arranges components in five regions: north, south, east, west, and center.
- `FlowLayout` arranges components in a row, with any extra space distributed between the components.
- `GridLayout` arranges components in a grid of rows and columns, with all components having the same size.
- `CardLayout` arranges components as a stack of cards, with only one card visible at a time.
- `GridBagLayout` is the most flexible layout manager, allowing components to be arranged in a grid with varying row heights and column widths.
- The `setLayout` method is used to set the layout manager for a container.
- The `add` method is used to add components to a container, with the layout manager determining the position and size of the component.
- The `pack` method is used to size the container to fit its components.