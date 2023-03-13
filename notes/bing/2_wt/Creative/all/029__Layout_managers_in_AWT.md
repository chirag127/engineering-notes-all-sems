#### Layout managers in AWT

- Layout managers are objects that implement the `LayoutManager` interface and determine the size and position of the components within a container.
- Layout managers are used to arrange components in a consistent and predictable way across different platforms and screen resolutions.
- Layout managers can be set for a container using the `setLayout(LayoutManager)` method. The default layout manager for a `Frame` is `BorderLayout`, and for a `Panel` is `FlowLayout`.
- Some of the common layout managers in AWT are:

  - `BorderLayout`: It divides the container into five regions: `NORTH`, `SOUTH`, `EAST`, `WEST`, and `CENTER`. Each region can contain only one component, and the `CENTER` region expands to fill the remaining space.
  - `FlowLayout`: It arranges the components in a single row, from left to right, and wraps to the next line if there is not enough space. It also allows to specify the alignment (`LEFT`, `CENTER`, or `RIGHT`) and the horizontal and vertical gaps between the components.
  - `GridLayout`: It arranges the components in a grid of rows and columns, with equal size and spacing. It also allows to specify the number of rows and columns, and the horizontal and vertical gaps between the cells.
  - `CardLayout`: It allows to create a stack of components, where only one component is visible at a time. It also provides methods to switch between the components, such as `first()`, `last()`, `next()`, and `previous()`.
  - `GridBagLayout`: It is the most flexible and complex layout manager, which allows to specify the constraints for each component, such as the grid position, size, alignment, padding, and weight. It also allows to create components that span multiple rows or columns, or that resize with the container.

- A mnemonic to remember the layout managers in AWT is: **B**ig **F**ish **G**row **C**razy **G**ills. (BorderLayout, FlowLayout, GridLayout, CardLayout, GridBagLayout)