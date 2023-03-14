#### Layout managers in AWT

- Layout managers are objects that control the size and position of components inside a container, such as a window or a panel.
- AWT provides five predefined layout managers that implement the java.awt.LayoutManager interface: BorderLayout, FlowLayout, CardLayout, GridLayout, and GridBagLayout.
- Every AWT and Swing container has a default layout manager, which can be changed by using the container.setLayout method.
- Each layout manager has its own rules and behavior for arranging components in different areas of the container.
- The following points describe the main features of each layout manager:

  - BorderLayout: It divides the container into five fixed areas: North, South, East, West, and Center. Only one component can be placed in each area. The Center area gets all the extra space when the container is resized.
  - FlowLayout: It places the components in a single row, starting a new row if the container is not wide enough. It respects the preferred size of the components and aligns them horizontally and vertically.
  - CardLayout: It allows the container to have different components at different times, like a stack of cards. Only one component (card) is visible at a time, and it can be switched by using the CardLayout methods or a control component, such as a combo box.
  - GridLayout: It arranges the components in a grid of rows and columns, with equal size and spacing. The number of rows and columns can be specified or determined by the number of components added to the container.
  - GridBagLayout: It is the most flexible and complex layout manager, which can create any kind of layout by using constraints for each component. The constraints specify the position, size, alignment, and padding of the component in a grid of cells. The cells can span multiple rows and columns, and have different weights for distributing extra space.