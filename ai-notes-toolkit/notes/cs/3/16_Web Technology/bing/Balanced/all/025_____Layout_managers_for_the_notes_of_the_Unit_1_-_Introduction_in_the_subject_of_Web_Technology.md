# Layout managers

- A layout manager is an object that controls the size and position (layout) of components inside a container object .
- A container object is a graphical user interface (GUI) element that can hold other components, such as buttons, labels, text fields, etc .
- A layout manager is useful for creating responsive and consistent layouts that can adapt to different screen sizes and resolutions .
- There are different types of layout managers in web technology, such as:
  - FlowLayout: It arranges the components in a container like the words on a page, from left to right and top to bottom .
  - BorderLayout: It divides the container into five regions: north, south, east, west and center, and places the components accordingly .
  - GridLayout: It arranges the components in a container in a grid of rows and columns, with equal size and spacing .
  - GridBagLayout: It is a more flexible version of GridLayout, that allows the components to span multiple rows and columns, and have different size and alignment .
  - CardLayout: It allows the container to have multiple components, but only one is visible at a time, like a stack of cards .
  - BoxLayout: It arranges the components in a container either horizontally or vertically, with optional gaps and alignment .
- To use a layout manager, we need to create an instance of the layout manager class and set it as the layout for the container object .
- We can also customize the layout manager by setting its properties, such as alignment, gaps, insets, etc .
- Some examples of layout managers in web technology are:

```java
//Creating a container object
Container c = new Container();

//Creating a layout manager object
FlowLayout fl = new FlowLayout();

//Setting the layout manager for the container
c.setLayout(fl);

//Creating some components
Button b1 = new Button("Button 1");
Button b2 = new Button("Button 2");
Label l1 = new Label("Label 1");

//Adding the components to the container
c.add(b1);
c.add(b2);
c.add(l1);
```

This code will create a container with a flow layout and three components, as shown below:

![Flow layout example](https://www.javatpoint.com/images/awt/flowlayout.png)

```java
//Creating a container object
Container c = new Container();

//Creating a layout manager object
BorderLayout bl = new BorderLayout();

//Setting the layout manager for the container
c.setLayout(bl);

//Creating some components
Button b1 = new Button("Button 1");
Button b2 = new Button("Button 2");
Label l1 = new Label("Label 1");
Label l2 = new Label("Label 2");
Label l3 = new Label("Label 3");

//Adding the components to the container with specified regions
c.add(b1, BorderLayout.NORTH);
c.add(b2, BorderLayout.SOUTH);
c.add(l1, BorderLayout.EAST);
c.add(l2, BorderLayout.WEST);
c.add(l3, BorderLayout.CENTER);
```

This code will create a container with a border layout and five components, as shown below:

![Border layout example](https://www.javatpoint.com/images/awt/borderlayout.png)