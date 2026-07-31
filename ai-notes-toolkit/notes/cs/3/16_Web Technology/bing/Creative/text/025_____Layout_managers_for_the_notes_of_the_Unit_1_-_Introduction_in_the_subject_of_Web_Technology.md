### Layout managers

- A layout manager is an object that controls the size and position (layout) of components inside a container object .
- A container object is a graphical user interface (GUI) component that can hold other components, such as buttons, labels, text fields, etc .
- A layout manager is useful for creating responsive and consistent layouts that can adapt to different screen sizes and resolutions .
- There are different types of layout managers in web technology, such as:
  - FlowLayout: It arranges the components in a container like the words on a page, from left to right and top to bottom .
  - BorderLayout: It divides the container into five regions: north, south, east, west and center, and places the components accordingly .
  - GridLayout: It arranges the components in a container in a grid of rows and columns, with equal size and spacing .
  - GridBagLayout: It is a more flexible version of GridLayout, that allows the components to span multiple rows and columns, and have different size and alignment .
  - CardLayout: It allows the container to have multiple components, but only one component is visible at a time, like a stack of cards .
  - BoxLayout: It arranges the components in a container either horizontally or vertically, with optional gaps and alignment .
- To use a layout manager, we need to create an instance of the layout manager class and set it as the layout for the container object .
- We can also add, remove, or modify the components in the container using the methods of the container class .
- Some examples of layout managers in web technology are shown below:

#### FlowLayout

```java
// Create a container object
Panel panel = new Panel();

// Create a layout manager object
FlowLayout layout = new FlowLayout();

// Set the layout for the container
panel.setLayout(layout);

// Create some components
Button button1 = new Button("Button 1");
Button button2 = new Button("Button 2");
Label label = new Label("Label");

// Add the components to the container
panel.add(button1);
panel.add(button2);
panel.add(label);

// The components will be arranged like this:
// [Button 1] [Button 2] [Label]
```

#### BorderLayout

```java
// Create a container object
Frame frame = new Frame();

// Create a layout manager object
BorderLayout layout = new BorderLayout();

// Set the layout for the container
frame.setLayout(layout);

// Create some components
Button button1 = new Button("Button 1");
Button button2 = new Button("Button 2");
Label label = new Label("Label");
TextArea textArea = new TextArea("Text Area");
Checkbox checkbox = new Checkbox("Checkbox");

// Add the components to the container with the region name
frame.add(button1, BorderLayout.NORTH);
frame.add(button2, BorderLayout.SOUTH);
frame.add(label, BorderLayout.EAST);
frame.add(textArea, BorderLayout.CENTER);
frame.add(checkbox, BorderLayout.WEST);

// The components will be arranged like this:
// +-----------------+
// |    Button 1     |
// +-----------------+
// |Checkbox|Text Area|Label|
// +-----------------+
// |    Button 2     |
// +-----------------+
```

#### GridLayout

```java
// Create a container object
Panel panel = new Panel();

// Create a layout manager object with 2 rows and 3 columns
GridLayout layout = new GridLayout(2, 3);

// Set the layout for the container
panel.setLayout(layout);

// Create some components
Button button1 = new Button("Button 1");
Button button2 = new Button("Button 2");
Button button3 = new Button("Button 3");
Button button4 = new Button("Button 4");
Button button5 = new Button("Button 5");
Button button6 = new Button("Button 6");

// Add the components to the container
panel.add(button1);
panel.add(button2);
panel.add(button3);
panel.add(button4);
panel.add(button5);
panel.add(button6);

// The components will be arranged like this:
// +---------+---------+---------+
// | Button 1| Button 2| Button 3|
//

```
