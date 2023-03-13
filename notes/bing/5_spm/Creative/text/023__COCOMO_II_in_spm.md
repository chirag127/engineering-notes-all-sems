### COCOMO II in SPM

- COCOMO II stands for Constructive Cost Model II, which is a software cost estimation model developed at the University of Southern California  .
- COCOMO II is an update of the original COCOMO model published in 1981, which was based on the data from the 1970s  .
- COCOMO II aims to address the software development practices in the 1990s and 2000s, such as rapid application development, reuse, prototyping, and object-oriented programming .
- COCOMO II consists of three sub-models: Application Composition, Early Design, and Post-Architecture .
  - Application Composition model is used for estimating the effort and schedule of projects that use rapid application development or integrated computer-aided software engineering tools .
  - Early Design model is used for estimating the effort and schedule of projects in the early stages of software development, when only the size and functionality of the system are known .
  - Post-Architecture model is used for estimating the effort and schedule of projects after the software architecture is defined and the detailed design is underway .
- COCOMO II uses the following formula to estimate the effort (in person-months) of a software project :

  Effort = A * Size<sup>B</sup> * M

  where:

  - A is a constant that depends on the sub-model and the data source .
  - Size is the estimated size of the software product in thousands of source lines of code (KSLOC) or function points (FP) .
  - B is an exponent that reflects the economy or diseconomy of scale .
  - M is a multiplier that reflects the effects of various cost drivers, such as product complexity, personnel capability, development environment, and reuse .

- COCOMO II uses the following formula to estimate the schedule (in months) of a software project :

  Schedule = C * Effort<sup>D</sup>

  where:

  - C is a constant that depends on the sub-model and the data source .
  - Effort is the estimated effort in person-months .
  - D is an exponent that reflects the effects of various schedule drivers, such as required reliability, development flexibility, and team cohesion .

- COCOMO II is a simple and well-tested model that provides about 20% cost and 70% time estimate accuracy. It can be calibrated and tailored to specific organizations and projects using historical data and expert judgment.