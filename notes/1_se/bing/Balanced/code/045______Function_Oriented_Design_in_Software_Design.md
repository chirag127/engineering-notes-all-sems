#### Function Oriented Design in Software Design

Function Oriented Design is a method to software design where the model is decomposed into a set of interacting units or modules where each unit or module has a clearly defined function  . Thus, the system is designed from a functional viewpoint  .

A generic procedure for Function Oriented Design is as follows:

- Start with a high level description of what the software/program does.
- Identify the major functions and data flows in the system using a Data Flow Diagram (DFD).
- Refine the DFD by adding more details and levels of abstraction.
- Define the data items and their attributes using a Data Dictionary.
- Structure the functions using a Structured Chart.
- Verify and validate the design using various techniques such as coupling, cohesion, modularity, etc.

An example of Function Oriented Design for a simple calculator program is given below:

- The high level description of the program is: The program takes two numbers and an operator as input and performs the corresponding arithmetic operation on the numbers and displays the result.
- The DFD for the program is:

![DFD for calculator program](https://media.geeksforgeeks.org/wp-content/uploads/20190327171604/DFD-for-calculator-program.png)

- The Data Dictionary for the program is:

| Data Item | Description | Attributes |
|-----------|-------------|------------|
| Number1 | First operand | Real number |
| Number2 | Second operand | Real number |
| Operator | Arithmetic operator | One of +, -, *, / |
| Result | Output of the operation | Real number |

- The Structured Chart for the program is:

![Structured Chart for calculator program](https://media.geeksforgeeks.org/wp-content/uploads/20190327171604/Structured-Chart-for-calculator-program.png)

- The design can be verified and validated by checking the following criteria:

  - Coupling: The degree of interdependence between the modules. Low coupling is desirable as it reduces complexity and increases maintainability.
  - Cohesion: The degree of relatedness within a module. High cohesion is desirable as it increases clarity and reusability.
  - Modularity: The degree of decomposition of the system into independent modules. High modularity is desirable as it facilitates parallel development and testing.
  - Functionality: The degree to which the design meets the requirements and specifications of the system. High functionality is desirable as it ensures correctness and reliability.