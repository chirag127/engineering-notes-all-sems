##### Function Point (FP) Based Measures in software design

- Function point (FP) is a technique to measure the size and complexity of a software system based on the functionality it provides to the user.
- FP is based on the assumption that the size of a software system is proportional to the number and types of functions it performs, such as inputs, outputs, inquiries, logical files, and external interfaces.
- FP can be used to estimate the effort, cost, and duration of software development and maintenance projects, as well as to compare the productivity and quality of different software systems or teams.
- FP can be calculated using the following steps:

  1. Identify the functional user requirements of the software system and classify them into five types: external inputs (EI), external outputs (EO), external inquiries (EQ), internal logical files (ILF), and external interface files (EIF).
  2. Assign a complexity weight to each function type based on the number of data elements and record types involved. The complexity weights are given in the table below.

| Function type | Low | Average | High |
|---------------|-----|---------|------|
| EI            | 3   | 4       | 6    |
| EO            | 4   | 5       | 7    |
| EQ            | 3   | 4       | 6    |
| ILF           | 7   | 10      | 15   |
| EIF           | 5   | 7       | 10   |

  3. Count the number of functions of each type and complexity level and multiply them by the corresponding complexity weight to obtain the unadjusted function point (UFP) count.
  4. Apply a technical complexity factor (TCF) to adjust the UFP count for the non-functional requirements and technical characteristics of the software system. The TCF is calculated as:

  TCF = 0.65 + 0.01 * ∑Fi

  where Fi is the rating (from 0 to 5) of the influence of the ith general system characteristic (GSC) on the software system. There are 14 GSCs defined by the FP method, such as data communications, distributed functions, performance, reusability, etc.
  5. Multiply the UFP count by the TCF to obtain the adjusted function point (AFP) count, which is the final measure of the software system size and complexity.

- FP can be used to estimate the effort required to develop or maintain a software system by applying a productivity factor (PF) to the AFP count. The PF is usually derived from historical data or industry benchmarks and reflects the average number of hours or person-months needed to deliver one FP. The effort estimate is then given by:

  Effort = AFP * PF

- FP can also be used to estimate the cost and duration of a software project by applying cost and schedule factors to the effort estimate. The cost factor reflects the average cost per hour or person-month of the project team, while the schedule factor reflects the average time compression or expansion factor for different project sizes. The cost and duration estimates are then given by:

  Cost = Effort * Cost factor

  Duration = Effort^0.33 * Schedule factor

- FP can also be used to compare the productivity and quality of different software systems or teams by calculating the FP per unit of effort, cost, or time, or the defect density per FP. These metrics can help to identify the best practices and areas for improvement in software development and maintenance.