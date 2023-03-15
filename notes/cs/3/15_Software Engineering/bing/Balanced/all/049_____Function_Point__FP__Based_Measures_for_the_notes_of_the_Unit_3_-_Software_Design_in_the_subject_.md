# Function Point (FP) Based Measures

- Function points are a unit of measurement used to quantify the amount of business functionality being delivered by a software application.
- Function points measure the size of an application system based on the functional view of the system.
- Function points allow software engineers to better measure the size of a project, identify areas in need of optimization, and analyze development performance benchmarks over time.
- Function points are one of the most widely used measures of software size .
- The basis of function points is that the “functionality” of the system, that is, what the system performs, is the measure of the system size .
- Function points are independent of the technology, programming language, or development methodology used to build the software application.
- Function points are calculated by counting the number of inputs, outputs, queries, internal files and external files in the system and adjusting that total for the functional complexity of the system .
- The steps for counting function points are:
  - Identify the type of project (development, enhancement, or maintenance) and the type of count (application or project).
  - Identify the data and transactional functions of the system and classify them into five types: external inputs (EI), external outputs (EO), external inquiries (EQ), internal logical files (ILF), and external interface files (EIF).
  - Assign a complexity level (low, average, or high) to each function based on the number of data elements and file types involved.
  - Assign a weight to each function based on its type and complexity level. The weights are given in the following table:

    | Function Type | Low | Average | High |
    |---------------|-----|---------|------|
    | EI            | 3   | 4       | 6    |
    | EO            | 4   | 5       | 7    |
    | EQ            | 3   | 4       | 6    |
    | ILF           | 7   | 10      | 15   |
    | EIF           | 5   | 7       | 10   |

  - Calculate the unadjusted function point (UFP) by multiplying the number of functions of each type by their corresponding weights and summing up the results.
  - Calculate the value adjustment factor (VAF) by rating the system on 14 general system characteristics (GSC) on a scale of 0 to 5 and summing up the ratings. The GSCs are:

    | GSC | Description |
    |-----|-------------|
    | 1   | Data communications |
    | 2   | Distributed data processing |
    | 3   | Performance |
    | 4   | Heavily used configuration |
    | 5   | Transaction rate |
    | 6   | Online data entry |
    | 7   | End-user efficiency |
    | 8   | Online update |
    | 9   | Complex processing |
    | 10  | Reusability |
    | 11  | Installation ease |
    | 12  | Operational ease |
    | 13  | Multiple sites |
    | 14  | Facilitate change |

  - Calculate the adjusted function point (AFP) by multiplying the UFP by the VAF. The VAF is calculated as VAF = 0.65 + (0.01 * sum of GSC ratings).

- Function points can be used to estimate the effort, cost, and duration of a software project based on historical data and productivity factors.
- Function points can also be used to compare the productivity and quality of different software projects or teams.
- Function points are not suitable for measuring the size of non-functional requirements, such as security, reliability, or usability.
- Function points are also not suitable for measuring the size of software systems that are not based on data and transactional functions, such as real-time, embedded, or scientific systems.