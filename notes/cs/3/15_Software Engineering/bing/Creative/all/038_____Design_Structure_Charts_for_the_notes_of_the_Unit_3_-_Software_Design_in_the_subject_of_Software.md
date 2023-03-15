# Design Structure Charts

Design structure charts are graphical representations of the modules and their interactions in a software system. They are used to show the hierarchical decomposition of a system into smaller and manageable units, as well as the data flow and control flow between them. Design structure charts can help in designing, documenting, and understanding software systems.

Some of the main concepts and components of design structure charts are:

- **Module**: A module is a box that contains the name of a function or a procedure that performs a specific task in the system. A module can be further decomposed into submodules if needed. A module can also have parameters that indicate the input and output data of the function or procedure.
- **Call**: A call is a line that connects two modules and shows the direction of control flow between them. A call indicates that the module at the tail of the line invokes the module at the head of the line. A call can have a label that specifies the condition or the frequency of the invocation.
- **Coupling**: Coupling is the degree of interdependence between modules. It measures how much a module depends on the data or the behavior of another module. High coupling means that a change in one module can affect many other modules, which makes the system complex and difficult to maintain. Low coupling means that a module is relatively independent and can be reused or modified easily. Coupling can be reduced by minimizing the number and the complexity of parameters, using local variables, and avoiding global variables.
- **Cohesion**: Cohesion is the degree of relatedness between the elements of a module. It measures how well a module performs a single and well-defined task. High cohesion means that a module has a clear and consistent purpose, which makes the system easy to understand and test. Low cohesion means that a module has multiple and unrelated responsibilities, which makes the system confusing and error-prone. Cohesion can be increased by splitting large and complex modules into smaller and simpler ones, and by grouping related functions or procedures together.

There are different types of design structure charts, depending on the nature and the structure of the system. Some of the common types are:

- **Transform centered structure**: This type of structure chart is suitable for systems that receive an input, transform it through a sequence of operations, and produce an output. The structure chart shows the main input module, the output module, and the intermediate modules that perform the transformations. The data flow is usually from left to right, and the control flow is usually top-down. An example of a transform centered structure chart is shown below:

![Transform centered structure chart](https://infinitylectures.com/wp-content/uploads/2020/10/transform-centered-structure-chart.png)

- **Transaction centered structure**: This type of structure chart is suitable for systems that process different types of transactions, each with its own logic and data. The structure chart shows the main transaction module, which receives the transaction type and dispatches it to the appropriate submodule. The submodules handle the specific transactions and interact with the data modules. The data flow is usually bidirectional, and the control flow is usually bottom-up. An example of a transaction centered structure chart is shown below:

![Transaction centered structure chart](https://infinitylectures.com/wp-content/uploads/2020/10/transaction-centered-structure-chart.png)

- **Call and return structure**: This type of structure chart is suitable for systems that have a main module that controls the overall execution of the system, and several subordinate modules that perform subtasks and return results to the main module. The structure chart shows the main module, the subordinate modules, and the calls and returns between them. The data flow is usually bidirectional, and the control flow is usually top-down and bottom-up. An example of a call and return structure chart is shown below:

![Call and return structure chart](https://infinitylectures.com/wp-content/uploads/2020/10/call-and-return-structure-chart.png)

- **Object oriented structure**: This type of structure chart is suitable for systems that are based on the object oriented paradigm, which models the system as a collection of objects that have attributes and behaviors. The structure chart shows the classes, the objects, and the messages between them. The data flow is usually bidirectional, and the control flow is usually dynamic and event-driven. An example of an object oriented structure chart is shown below:

![Object oriented structure chart](https://infinitylectures.com/wp-content/uploads/2020/10/object-oriented-structure-chart.png)

- **Layered structure**: This type of structure chart is suitable for systems that have a modular and hierarchical architecture, where each layer provides a set of services to the layer