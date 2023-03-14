Low-level design (LLD) is a component-level design process that follows a step-by-step refinement process. It describes every module in detail by incorporating the logic behind every component in the system. It delves deep into every specification of every system, providing a micro-level design . Low-level design helps the developers to stay focused without getting deviated from the deliverables. It is one-stop reference material for them.

Low-level design can be created using Unified Modelling Language (UML) diagrams, such as class diagrams, sequence diagrams, activity diagrams, etc. These diagrams show the structure and behavior of the classes, methods, interfaces, and relationships in the system . Low-level design also follows the principles of object-oriented programming, such as inheritance, encapsulation, polymorphism, and abstraction.

### Low Level Design in Software Design

The following is an example of a low-level design for a simple calculator application. It is not a complete design, but it illustrates some of the concepts and components involved.

```
+---------------------+
| Calculator          |
+---------------------+
| - display: String   |
| - result: double    |
| - operation: String |
+---------------------+
| + clear()           |
| + append(digit: int)|
| + setOperation(op: String) |
| + calculate()       |
| + updateDisplay()   |
+---------------------+

The Calculator class represents the main component of the application. It has three attributes: display, result, and operation. The display attribute stores the current input or output of the calculator. The result attribute stores the intermediate or final result of the calculation. The operation attribute stores the current arithmetic operation to be performed.

The Calculator class also has five methods: clear, append, setOperation, calculate, and updateDisplay. The clear method resets the display, result, and operation attributes to their initial values. The append method adds a digit to the display attribute. The setOperation method sets the operation attribute to the given parameter and updates the result attribute with the current display value. The calculate method performs the arithmetic operation on the result and display attributes and updates the display attribute with the new result. The updateDisplay method updates the graphical user interface with the current display value.
```

The following is a sequence diagram that shows the interaction between the Calculator class and the user interface when the user performs a simple addition.

```
+----------------+      +---------------------+
| User Interface |      | Calculator          |
+----------------+      +---------------------+
|                |      | - display: "0"      |
|                |      | - result: 0.0       |
|                |      | - operation: ""     |
+----------------+      +---------------------+
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
+----------------+      +---------------------+
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
+----------------+      +---------------------+
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
+----------------+      +---------------------+
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
+----------------+      +---------------------+
|                |      |                     |
|                |      |                     |
|                |      |                     |
|                |      |                     |
+----------------+      +---------------------+
|                |      |                     |
|                |      |                     |
|                |      |                     |
+----------------+      +---------------------+
|                |      |                     |
|                |      |                     |
+----------------+      +---------------------+
|                |      |                     |
+----------------+      +---------------------+
|                |      |                     |
+----------------+      +---------------------+
|                |      |                     |