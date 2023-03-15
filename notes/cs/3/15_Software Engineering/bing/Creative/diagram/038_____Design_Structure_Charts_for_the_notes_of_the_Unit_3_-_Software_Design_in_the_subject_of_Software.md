Hello, I am Sydney, your AI assistant. I can help you with your notes on design structure charts for the unit 3 - software design in the subject of software engineering. Here is some information that I have gathered from the web:

### Design Structure Charts

- A design structure chart (SC) is a diagram that shows the breakdown of a system to its lowest manageable levels  .
- A SC is used in structured programming to arrange program modules into a tree  .
- A SC shows the modules and their call hierarchy, the interfaces between the modules, and what information passes between modules .
- A SC can help to map the structure and data flow of complicated tasks.
- A SC can also help to identify the cohesion and coupling of the modules, and to verify the completeness and correctness of the design.

#### Types of Structure Charts

- There are two main types of SCs: transform centered and transaction centered.
- A transform centered SC is designed for the systems that receive an input which is transformed by a sequence of operations carried out by one module.
- A transaction centered SC describes a system that processes a number of different types of transactions, each with its own module.
- A SC can also be classified as top-down, bottom-up, or hybrid, depending on the order of the design process.

#### How to Draw Structure Charts

- There are some general steps and guidelines for drawing SCs  :
  - Have a clear understanding of the requirements, both functional and non-functional, of the system.
  - Identify the main modules and functions of the system, and assign them to different levels of abstraction .
  - Use simple shapes and lines to indicate the modules and their relationships. A common notation is to use rectangles for modules, circles for parameters, and arrows for data flow.
  - Label the modules with meaningful names, and the parameters with data types and direction .
  - Show the control flow and the call hierarchy of the modules, using different types of arrows or symbols . For example, a solid arrow can indicate a normal call, a dashed arrow can indicate an exception, and a diamond can indicate a decision point.
  - Verify the SC for consistency, completeness, and correctness, and make adjustments as needed .

#### Example of a Structure Chart

- Here is an example of a SC for a system that calculates the average of a list of numbers:

![Structure chart example](https://infinitylectures.com/wp-content/uploads/2020/12/Structure-Chart-Example.png)

- The SC shows the main module (Average), which calls two submodules (Sum and Divide).
- The SC also shows the parameters (List, N, Total, and Avg), and their data types and direction.
- The SC indicates the data flow and the control flow of the system.
