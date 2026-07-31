A design structure chart is a diagram that shows the hierarchical decomposition of a software system into its modules and the data flow between them. It is a tool for structured design that helps to identify the modules, their interfaces, and the information that passes between them. A design structure chart consists of the following elements:

- A box represents a module, which is a unit of functionality in the software system. The box contains the name of the module and optionally its parameters and return values.
- A line with an arrow represents a control link, which shows the order of execution of the modules. The arrow points from the calling module to the called module.
- A line with a circle represents a data link, which shows the data flow between the modules. The circle contains the name of the data item that is passed between the modules.
- A dashed line represents a library link, which shows the use of a module from an external library. The dashed line points from the calling module to the library module.

Here is an example of a design structure chart for a software system that calculates the area and perimeter of different shapes:

#### Design Structure Charts in Software Design

```
+-----------------+     +-----------------+
|  Main Program   |     |  Input Shape    |
|                 |     |                 |
+-----------------+     +-----------------+
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         +----------------------+
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         v                      v
+-----------------+     +-----------------+
|  Calculate Area |     |  Calculate      |
|                 |     |  Perimeter      |
+-----------------+     +-----------------+
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         +----------------------+
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         v                      v
+-----------------+     +-----------------+
|  Output Results |     |  Exit Program   |
|                 |     |                 |
+-----------------+     +-----------------+
```

The design structure chart shows that the main program calls the input shape module, which asks the user to enter the type and dimensions of a shape. Then, the main program calls the calculate area and calculate perimeter modules, which compute the area and perimeter of the shape based on its type and dimensions. Finally, the main program calls the output results module, which displays the area and perimeter of the shape to the user, and the exit program module, which terminates the program. The data links show that the type and dimensions of the shape are passed from the input shape module to the calculate area and calculate perimeter modules, and the area and perimeter of the shape are passed from the calculate area and calculate perimeter modules to the output results module. The library links show that the calculate area and calculate perimeter modules use some modules from an external library, such as math functions or shape formulas.