##### Function Point (FP) Based Measures in software design

- Function Point (FP) Based Measures are a way of estimating the size and complexity of a software system based on the functionality it provides to the user.
- Function Point (FP) Based Measures are derived from counting the number and types of inputs, outputs, inquiries, files, and interfaces that the software system has or uses.
- Function Point (FP) Based Measures are independent of the programming language, technology, or development methodology used to implement the software system.
- Function Point (FP) Based Measures can be used to compare the productivity and quality of different software projects, to estimate the effort and cost of software development and maintenance, and to plan and control software projects.
- Function Point (FP) Based Measures are calculated using the following steps:

  1. Identify the functional user requirements of the software system and classify them into five types: External Inputs (EI), External Outputs (EO), External Inquiries (EQ), Internal Logical Files (ILF), and External Interface Files (EIF).
  2. Assign a complexity level (low, average, or high) to each functional user requirement based on the number of data elements and file types involved.
  3. Use a table of complexity weights to determine the number of function points (FP) for each functional user requirement based on its type and complexity level.
  4. Sum up the function points (FP) for all the functional user requirements to obtain the unadjusted function point count (UFP).
  5. Apply a value adjustment factor (VAF) to the unadjusted function point count (UFP) based on the degree of influence (0 to 5) of 14 general system characteristics (GSC) such as data communications, distributed functions, performance, etc.
  6. The value adjustment factor (VAF) is calculated as 0.65 + (0.01 * sum of GSC ratings).
  7. The adjusted function point count (AFP) is calculated as UFP * VAF.
  8. The adjusted function point count (AFP) is the final measure of the size and complexity of the software system.

- A mnemonic to remember the five types of functional user requirements is **I FEE**L (Inputs, Files, External, External, Logical).
- A mnemonic to remember the 14 general system characteristics is **DID RAP COPS SAVE PERFECT DATA** (Data communications, Distributed functions, Reusability, Auditability, Performance, Capacity, Online update, Security, Virtual machine, Ease of use, Portability, End-user efficiency, Complexity, Transaction rate).
- An example of calculating the function point count for a simple software system that allows users to create, read, update, and delete (CRUD) records of employees and departments is given below:

  | Functional User Requirement | Type | Complexity | FP |
  | --------------------------- | ---- | ---------- | -- |
  | Create employee record | EI | Low | 3 |
  | Read employee record | EQ | Low | 3 |
  | Update employee record | EI | Average | 4 |
  | Delete employee record | EI | Low | 3 |
  | Create department record | EI | Low | 3 |
  | Read department record | EQ | Low | 3 |
  | Update department record | EI | Average | 4 |
  | Delete department record | EI | Low | 3 |
  | Employee file | ILF | Low | 7 |
  | Department file | ILF | Low | 7 |
  | Total | | | 40 |

  - The unadjusted function point count (UFP) is 40.
  - The value adjustment factor (VAF) is 0.65 + (0.01 * 35) = 1.00, assuming that the software system has an average degree of influence (2.5) for each of the 14 general system characteristics.
  - The adjusted function point count (AFP) is 40 * 1.00 = 40.
  - The function point count for the software system is 40.