### Layout managers

- A layout manager is an object that controls the size and position (layout) of components inside a container object .
- A container object is a graphical user interface (GUI) element that can hold other components, such as buttons, labels, text fields, etc .
- A layout manager determines how the components are sized and positioned inside the container, according to some rules or constraints .
- A layout manager can also adjust the layout dynamically when the container is resized or when components are added or removed .
- There are different types of layout managers in Java, each with its own advantages and disadvantages .
- Some of the common layout managers are:

  - FlowLayout: It arranges the components in a container like the words on a page, from left to right and top to bottom. It is the default layout manager for panels .
  - BorderLayout: It divides the container into five regions: north, south, east, west and center. Each region can hold only one component. It is the default layout manager for frames .
  - GridLayout: It arranges the components in a container in a grid of rows and columns. All the components have the same size and are equally spaced .
  - GridBagLayout: It is a more flexible version of GridLayout. It allows the components to have different sizes and to span multiple rows and columns. It also allows the components to be aligned and padded .
  - CardLayout: It allows the container to have multiple components, but only one component is visible at a time. The user can switch between the components using buttons or tabs .
  - BoxLayout: It arranges the components in a container either horizontally or vertically. It allows the components to have different sizes and alignments. It also allows the components to have gaps and glue between them .

- A layout manager can be set for a container using the `setLayout()` method. For example, `panel.setLayout(new FlowLayout())` sets the layout manager of the panel to FlowLayout .
- A component can be added to a container using the `add()` method. For example, `panel.add(button)` adds the button to the panel. Some layout managers require additional parameters to specify the position or constraints of the component .
- A layout manager can be customized by changing its properties or by creating a subclass of it .
- A layout manager can be combined with other layout managers by using nested containers. For example, a panel with a BorderLayout can have another panel with a GridLayout in its center region .