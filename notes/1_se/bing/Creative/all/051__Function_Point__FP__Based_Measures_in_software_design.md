##### Function Point (FP) Based Measures in software design

- Function Point (FP) is a technique to measure the size and complexity of a software system based on the user's view of its functionality, rather than the technical details of its implementation.
- FP is useful for estimating the effort, cost and duration of software projects, as well as for comparing the productivity and quality of different software systems or development processes.
- FP is based on the assumption that the functionality of a software system can be divided into five types of components: external inputs, external outputs, external inquiries, internal logical files and external interface files.
- Each type of component is assigned a complexity level (low, average or high) based on the number and type of data elements and record elements involved.
- A complexity weight is assigned to each complexity level for each type of component, as shown in the table below.

| Component | Low | Average | High |
|-----------|-----|---------|------|
| External input | 3 | 4 | 6 |
| External output | 4 | 5 | 7 |
| External inquiry | 3 | 4 | 6 |
| Internal logical file | 7 | 10 | 15 |
| External interface file | 5 | 7 | 10 |

- The unadjusted function point (UFP) is calculated by multiplying the number of components of each type and complexity level by their corresponding complexity weight, and summing up the results.
- UFP = (number of low complexity external inputs * 3) + (number of average complexity external inputs * 4) + (number of high complexity external inputs * 6) + ... + (number of high complexity external interface files * 10)
- The adjusted function point (AFP) is calculated by applying a technical complexity factor (TCF) to the UFP, to account for the non-functional requirements and technical characteristics of the software system.
- TCF = 0.65 + (0.01 * ∑Fi), where Fi is the value (from 0 to 5) of the ith general system characteristic (GSC), such as data communications, distributed functions, performance, etc. There are 14 GSCs in total, and their values are determined by the analyst based on the user's requirements and the system's specifications.
- AFP = UFP * TCF
- The AFP can be used to estimate the effort, cost and duration of the software project, by applying empirical formulas or models that relate the AFP to these parameters. For example, one such formula is: Effort (in person-months) = 0.4 * AFP^0.93
- The AFP can also be used to compare the productivity and quality of different software systems or development processes, by calculating the FP per person-month (FP/PM) or the defect density per FP (defects/FP) respectively. For example, if system A has an AFP of 500 and was developed by 10 people in 12 months, then its FP/PM is 500 / (10 * 12) = 4.17. If system B has an AFP of 400 and was developed by 8 people in 10 months, then its FP/PM is 400 / (8 * 10) = 5.00. This means that system B has a higher productivity than system A. Similarly, if system A has 50 defects and system B has 40 defects, then their defect densities are 50 / 500 = 0.10 and 40 / 400 = 0.10 respectively. This means that they have the same quality level.

- Some mnemonics and learning tricks for FP based measures are:

  - To remember the five types of components, use the acronym EIEIO: External Input, External Output, External Inquiry, Internal logical file, External Interface file.
  - To remember the complexity weights for each type of component, use the following sentences:
    - External Inputs are easy as 3, 4, 6.
    - External Outputs are a bit more, 4, 5, 7.
    - External Inquiries are the same as inputs, 3, 4, 6.
    - Internal logical files are hard to handle, 7, 10, 15.
    - External Interface files are somewhere in between, 5, 7, 10.
  - To remember the formula for TCF, use the rhyme: TCF is 0.65 plus a bit, 0.01 times the sum of Fi.
  - To remember the formula for AFP, use the wordplay: AFP is UFP times TCF, that's easy as ABC.