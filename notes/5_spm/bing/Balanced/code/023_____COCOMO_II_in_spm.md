### COCOMO II in spm

- COCOMO stands for **COnstructive COst MOdel**, which is a method for estimating the cost, effort, and schedule of software projects.
- COCOMO II is the **revised version** of the original COCOMO model, which was published in 1981 by Barry Boehm.
- COCOMO II is developed at the **University of Southern California** by the Center for Systems and Software Engineering (CSSE).
- COCOMO II consists of **three sub-models** that can be applied at different stages of software development: 
  - **Application Composition Model**: This model is used for estimating the effort and schedule of projects that use rapid application development (RAD) techniques, such as prototyping, application generators, or scripting languages. This model is based on the number of **object points**, which are a measure of the functionality and complexity of the software components.
  - **Early Design Model**: This model is used for estimating the effort and schedule of projects that are in the early stages of design, before the architecture is defined. This model is based on the size of the software in **source lines of code (SLOC)** or **function points (FP)**, and a set of **scale factors** and **cost drivers** that reflect the characteristics of the project, the product, the platform, and the personnel.
  - **Post-Architecture Model**: This model is used for estimating the effort and schedule of projects that have a defined architecture and a detailed design. This model is also based on the size of the software in SLOC or FP, and a set of scale factors and cost drivers, but with more **refined** and **detailed** values. This model also includes a **phase distribution** of the effort and schedule across the software life cycle stages, such as inception, elaboration, construction, and transition.
- COCOMO II provides a **formula** for calculating the effort and schedule of a software project, based on the sub-model, the size, and the adjustment factors. The formula is:

  - **Effort** = A * Size<sup>B</sup> * M
  - **Schedule** = C * Effort<sup>D</sup>
  - Where:
    - A, B, C, and D are **constants** that depend on the sub-model and the software life cycle stage.
    - Size is the **estimated size** of the software in SLOC or FP.
    - M is the **multiplier** that reflects the scale factors and cost drivers.
- COCOMO II is a **parametric** model, which means that it relies on historical data and empirical relationships to calibrate the constants and the adjustment factors. The model can be **tailored** to fit different types of software projects and organizations, by using appropriate data sources and values.
- COCOMO II is a **useful tool** for software project managers, as it can help them to plan, budget, and control the software development process. It can also help them to evaluate the impact of different design decisions, trade-offs, and risks on the project outcomes.