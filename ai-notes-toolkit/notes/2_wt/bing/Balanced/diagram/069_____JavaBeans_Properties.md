A JavaBean property is a named attribute that can be accessed by the user of the object. The attribute can be of any Java data type, including the classes that you define. A JavaBean property may be read, write, read only, or write only  .

A JavaBean property can be bound or constrained. A bound property is one that notifies other objects when its value changes. A constrained property is one that allows other objects to veto its value change.

A JavaBean property can be accessed by using getter and setter methods that follow a naming convention. For example, a property named color would have methods getColor() and setColor(). A boolean property named visible would have methods isVisible() and setVisible().

A JavaBean property can be customized by using a BeanInfo class that provides information about the property, such as its display name, description, editor, etc. A BeanInfo class can also specify the methods and events of a JavaBean.

### JavaBeans Properties

```
+----------------+       +----------------+
| JavaBean       |       | BeanInfo       |
|                |       |                |
| +------------+ |       | +------------+ |
| | Properties | |       | | Properties | |
| +------------+ |       | +------------+ |
| | color      | |       | | color      | |
| | visible    | |       | | visible    | |
| | size       | |       | | size       | |
| +------------+ |       | +------------+ |
|                |       |                |
| +------------+ |       | +------------+ |
| | Methods    | |       | | Methods    | |
| +------------+ |       | +------------+ |
| | getColor() | |       | | getColor() | |
| | setColor() | |       | | setColor() | |
| | isVisible()| |       | | isVisible()| |
| | setVisible()| |       | | setVisible()| |
| | getSize()  | |       | | getSize()  | |
| | setSize()  | |       | | setSize()  | |
| +------------+ |       | +------------+ |
|                |       |                |
| +------------+ |       | +------------+ |
| | Events     | |       | | Events     | |
| +------------+ |       | +------------+ |
| | Property   | |       | | Property   | |
| | Change     | |       | | Change     | |
| | Vetoable   | |       | | Vetoable   | |
| | Change     | |       | | Change     | |
| +------------+ |       | +------------+ |
+----------------+       +----------------+
         |                       |
         |                       |
         +-----------------------+
                   |
                   |
                   V
            +--------------+
            | Builder Tool |
            |              |
            | +----------+ |
            | | Property | |
            | | Editor   | |
            | +----------+ |
            +--------------+
```