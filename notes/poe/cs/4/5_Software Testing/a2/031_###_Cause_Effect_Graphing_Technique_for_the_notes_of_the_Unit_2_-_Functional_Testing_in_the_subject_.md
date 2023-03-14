 Here is the content in markdown format for the given topic:

### Cause Effect Graphing Technique for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

The Cause Effect Graphing Technique is a graphical representation technique used in Functional Testing to analyze the functional requirements and traceability. It helps in identifying the root cause of a defect by mapping the inputs to the expected outputs.

Following are the steps to create a Cause Effect Graph:

1. Identify the input conditions and output conditions from the functional requirement. These will become the nodes of the graph.
2. Connect the input conditions to the output conditions based on the effect relationship. An arrow from input to output denotes the effect.
3. Label the connections with expressions or conditions that relate the inputs to outputs.
4. Repeat step#2 and step#3 to capture all input-output relationships and impacts.
5. Review the graph for completeness and clarity. Identify if any input or impact is missed.

Advantages:

- Helps understand the functional flow in a graphical way. Easy to understand.
- Helps in defect root cause analysis by tracing from output to input.
- Acts as a visual test case design aid.

Disadvantages:

- May become complex for large or complex functional requirements.
- The technician who creates the graph should have good understanding of the requirements.

Examples:

- A graph can be created for an ATM withdrawal functional requirement with inputs like *Customer, Account, Amount* and outputs like *Cash, Receipt, Balance*.
- A graph can be created for an e-commerce checkout process with inputs like *Products, Address, Payment* and outputs like *Order Confirmation, Payment Receipt*.

Applications:

- Requirements analysis
- Test case design
- Defect root cause analysis