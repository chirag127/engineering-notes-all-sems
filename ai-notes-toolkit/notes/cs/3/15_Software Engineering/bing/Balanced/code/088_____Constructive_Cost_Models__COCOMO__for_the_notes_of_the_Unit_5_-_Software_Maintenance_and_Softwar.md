### Constructive Cost Models (COCOMO) for the notes of the Unit 5 - Software Maintenance and Software Project Management in the subject of Software Engineering

- COCOMO stands for **COnstructive COst MOdel**    .
- It is a **regression model** based on **LOC** (Lines of Code) that estimates the **effort, cost, time, and quality** of software projects    .
- It was developed by **Barry W. Boehm** in **1981** and revised later as **COCOMO II** in **1995** .
- It uses **historical data** from previous projects to derive the model parameters .
- It has three levels of complexity: **Basic, Intermediate, and Detailed**    .
- The Basic level assumes a **single linear equation** for each project category (Organic, Semi-detached, or Embedded) and uses only the **estimated LOC** as the input    .
- The Intermediate level introduces **cost drivers** that affect the effort and productivity, such as product attributes, hardware attributes, personnel attributes, and project attributes    .
- The Detailed level further divides the project into different **phases** and **modules** and applies the Intermediate level model to each of them    .
- The general formula for COCOMO is:

```
Effort = a * (LOC) ^ b * M
```

where `a` and `b` are constants that depend on the project category, `LOC` is the estimated lines of code, and `M` is the product of the cost drivers    .

- The advantages of COCOMO are:
  - It is **simple** and **easy** to use and understand  .
  - It is **empirical** and **validated** by many projects .
  - It provides **quantitative** and **objective** estimates  .
  - It can be **calibrated** and **adapted** to different environments and domains .

- The disadvantages of COCOMO are:
  - It relies on **LOC** as the main input, which is **difficult** and **inaccurate** to estimate in the early stages of the project  .
  - It does not account for **non-functional** requirements, such as usability, security, reliability, etc  .
  - It does not consider the **dynamics** and **uncertainties** of the software development process, such as changes in requirements, risks, learning curves, etc  .
  - It may not be **applicable** or **representative** for new technologies, paradigms, or domains .