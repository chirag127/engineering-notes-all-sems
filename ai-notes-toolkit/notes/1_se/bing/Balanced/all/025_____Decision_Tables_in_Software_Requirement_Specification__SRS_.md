### Decision Tables in Software Requirement Specification (SRS)

- A decision table is a tabular representation of the logic and conditions of a software system. It is used to specify the behavior and outcomes of the system based on different combinations of inputs and rules.
- A decision table consists of four parts: condition stubs, action stubs, condition entries, and action entries. Condition stubs are the names of the input variables or parameters that affect the system's behavior. Action stubs are the names of the output variables or actions that the system performs. Condition entries are the possible values or states of the condition stubs. Action entries are the possible values or states of the action stubs.
- A decision table can be represented in two formats: limited entry and extended entry. In a limited entry format, each condition entry and action entry can only have two values: Y (yes) or N (no). In an extended entry format, each condition entry and action entry can have more than two values, such as numbers, text, or symbols.
- A decision table can be used to document the functional requirements of a software system in a clear and concise way. It can also be used to verify the completeness and consistency of the requirements, as well as to identify and eliminate any conflicts or redundancies. A decision table can also be used to generate test cases and scenarios for the software system.
- A decision table can have some advantages and disadvantages compared to other methods of specifying software requirements. Some of the advantages are:

  - It can handle complex and multiple conditions and actions in a systematic and organized way.
  - It can reduce the ambiguity and misunderstanding of the requirements by using a standard and uniform notation.
  - It can facilitate the communication and collaboration among the stakeholders, such as the developers, testers, and users of the software system.
  - It can improve the quality and reliability of the software system by ensuring the accuracy and completeness of the requirements.

- Some of the disadvantages are:

  - It can become large and cumbersome if there are too many condition stubs and action stubs, or if there are too many possible combinations of condition entries and action entries.
  - It can be difficult to maintain and update if the requirements change frequently or if new requirements are added.
  - It can be challenging to convert a decision table into a natural language or a graphical representation, such as a flowchart or a state diagram.

- An example of a decision table for a software system that calculates the discount and total price of a product based on the customer type and the quantity purchased is shown below:

| Condition Stubs | Condition Entries | Action Stubs | Action Entries |
| --------------- | ----------------- | ------------ | -------------- |
| Customer Type   | Regular (R)       | Discount (%) | 0              |
|                 | Premium (P)       |              | 10             |
| Quantity        | < 10              | Total Price  | Price * Quantity * (1 - Discount/100) |
|                 | >= 10             |              | Price * Quantity * (1 - Discount/100) - 5 |

- The decision table can be read as follows:

  - If the customer type is regular and the quantity is less than 10, then the discount is 0% and the total price is the product of the price and the quantity.
  - If the customer type is regular and the quantity is greater than or equal to 10, then the discount is 0% and the total price is the product of the price and the quantity minus 5.
  - If the customer type is premium and the quantity is less than 10, then the discount is 10% and the total price is the product of the price and the quantity multiplied by 0.9.
  - If the customer type is premium and the quantity is greater than or equal to 10, then the discount is 10% and the total price is the product of the price and the quantity multiplied by 0.9 minus 5.