# COCOMO II in SPM

- COCOMO II stands for **COnstructive COst MOdel II**, which is a model for estimating the cost, effort, and schedule of software projects.
- COCOMO II is a revised and updated version of the original COCOMO model, which was published in 1981 by Barry Boehm.
- COCOMO II consists of three sub-models, which are applied at different stages of the software development life cycle:
  - **Application Composition Model**: This model is used for rapid prototyping and early design of software systems, using application generators, code reuse, or other high-level tools. It estimates the effort based on the number of object points, which are a measure of the functionality and complexity of the software components.
  - **Early Design Model**: This model is used for estimating the effort and schedule of software projects after the requirements have been defined, but before the architecture has been designed. It estimates the effort based on the size of the software in terms of source lines of code (SLOC) or function points (FP), and adjusts it using a set of cost drivers that reflect the characteristics of the project, the product, the platform, and the personnel.
  - **Post-Architecture Model**: This model is used for estimating the effort and schedule of software projects after the architecture has been designed and detailed design has begun. It estimates the effort based on the size of the software in terms of SLOC or FP, and adjusts it using a set of cost drivers and scaling factors that reflect the complexity, quality, and risk of the project.
- COCOMO II uses the following basic formula to estimate the effort (in person-months) for each sub-model:

  Effort = A * Size^B * M

  where A and B are constants that depend on the sub-model, Size is the software size in SLOC or FP, and M is the product of the cost drivers and scaling factors.

- COCOMO II also provides formulas to estimate the development time (in months) and the number of developers (in persons) for each sub-model, based on the estimated effort and some other parameters.

- COCOMO II is a widely used and well-tested model that can provide accurate and reliable estimates for software projects of different types and sizes. It can also be calibrated and tailored to fit the specific needs and characteristics of an organization or a project   .