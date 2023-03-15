### Constructive Cost Models (COCOMO) for the notes of the Unit 5 - Software Maintenance and Software Project Management in the subject of Software Engineering

- COCOMO stands for **COnstructive COst MOdel**    .
- It is a **regression model** based on **LOC** (Lines of Code) to estimate the **effort, cost, time, and quality** of software projects    .
- It was developed by **Barry W. Boehm** in **1981** and revised later as **COCOMO II** in **1995** .
- The model parameters are derived from fitting a **regression formula** using data from **historical projects** .
- There are three types of COCOMO models: **Basic, Intermediate, and Detailed**    .
- The **Basic COCOMO model** is the simplest and most general one. It assumes a **linear relationship** between the **size** of the software (in LOC) and the **effort** required to develop it (in person-months). It also uses two **constants** called **a** and **b** to represent the **average productivity** and the **complexity** of the software, respectively    .
- The **Basic COCOMO model** has the following formula    :

    `Effort = a * (Size)^b`

    where

    - `Effort` is the effort required to develop the software, in person-months
    - `Size` is the size of the software, in thousands of lines of code (KLOC)
    - `a` and `b` are constants that depend on the type of software project

- The **Basic COCOMO model** also estimates the **development time** (in months) and the **average staff size** (in persons) using the following formulas    :

    `Time = c * (Effort)^d`

    `Staff = Effort / Time`

    where

    - `Time` is the development time, in months
    - `Staff` is the average staff size, in persons
    - `c` and `d` are constants that depend on the type of software project

- The **Basic COCOMO model** classifies software projects into three categories: **Organic, Semi-detached, and Embedded**    .
- The **Organic projects** are those that are **simple, small, and familiar**. They have **low complexity**, **high productivity**, and **short development time**. The values of the constants for organic projects are    :

    `a = 2.4, b = 1.05, c = 2.5, d = 0.38`

- The **Semi-detached projects** are those that are **moderate, medium, and partially familiar**. They have **medium complexity**, **medium productivity**, and **medium development time**. The values of the constants for semi-detached projects are    :

    `a = 3.0, b = 1.12, c = 2.5, d = 0.35`

- The **Embedded projects** are those that are **complex, large, and unfamiliar**. They have **high complexity**, **low productivity**, and **long development time**. The values of the constants for embedded projects are    :

    `a = 3.6, b = 1.20, c