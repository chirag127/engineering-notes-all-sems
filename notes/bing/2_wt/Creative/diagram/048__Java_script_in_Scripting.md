JavaScript is a scripting or programming language that allows you to implement complex features on web pages. It can also run on other environments, such as Node.js or Electron, using different JavaScript engines. A JavaScript engine is a program that executes and compiles JavaScript into native machine code.

A typical JavaScript application architecture uses the bottom-up approach, always placing the User Interface (UI) at the center of the development at all times. As shown in the diagram, both the UI and the Server directly link to the code behind.

### JavaScript in Scripting

```
+-----------------+       +-----------------+
|                 |       |                 |
|      Server     |       |      Client     |
|                 |       |                 |
+-----------------+       +-----------------+
       |  ^                      |  ^
       |  |                      |  |
       v  |                      v  |
+-----------------+       +-----------------+
|                 |       |                 |
|   Code Behind   |       |   Code Behind   |
|                 |       |                 |
+-----------------+       +-----------------+
       |  ^                      |  ^
       |  |                      |  |
       v  |                      v  |
+-----------------+       +-----------------+
|                 |       |                 |
|     Server      |       |      UI         |
|    Response     |       |                 |
|                 |       |                 |
+-----------------+       +-----------------+
```

Another common JavaScript architecture is the Model-View-Controller (MVC) pattern, which separates the data (model), the presentation (view), and the logic (controller) of the application. This allows for better modularity, reusability, and maintainability of the code. The diagram below shows how the MVC components interact with each other.

### JavaScript in MVC

```
+-----------------+       +-----------------+
|                 |       |                 |
|      Model      |       |      View       |
|                 |       |                 |
+-----------------+       +-----------------+
       |  ^                      |  ^
       |  |                      |  |
       v  |                      v  |
+-----------------+       +-----------------+
|                 |       |                 |
|   Controller    |       |   Controller    |
|                 |       |                 |
+-----------------+       +-----------------+
       |  ^                      |  ^
       |  |                      |  |
       v  |                      v  |
+-----------------+       +-----------------+
|                 |       |                 |
|      Server     |       |      UI         |
|                 |       |                 |
+-----------------+       +-----------------+
```