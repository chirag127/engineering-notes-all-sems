# COCOMO II in SPM

- COCOMO II stands for Constructive Cost Model II, which is a software cost estimation model developed at the University of Southern California  .
- COCOMO II is a revised version of the original COCOMO model published in 1981, which was based on the analysis of 63 software projects  .
- COCOMO II is designed to address the software development practices in the 1990s and 2000s, such as rapid application development, reuse, prototyping, and object-oriented programming .
- COCOMO II consists of three sub-models: Application Composition, Early Design, and Post-Architecture  .
- Application Composition model is used for estimating the effort and schedule of projects that use rapid application development or application generators  .
- Early Design model is used for estimating the effort and schedule of projects in the early stages of development, when only the size and functionality are known  .
- Post-Architecture model is used for estimating the effort and schedule of projects after the architecture and high-level design are completed  .
- COCOMO II uses the following formula to estimate the effort (in person-months) for a software project:

    Effort = A * Size^E * EM

    where:

    - A is a constant that depends on the sub-model and the data source .
    - Size is the estimated size of the software product in thousands of source lines of code (KSLOC) or function points (FP) .
    - E is an exponent that depends on the sub-model and reflects the economies or diseconomies of scale .
    - EM is an effort multiplier that reflects the influence of various cost drivers, such as product complexity, personnel capability, development environment, etc. .

- COCOMO II uses the following formula to estimate the schedule (in months) for a software project:

    Schedule = B * Effort^F * SCM

    where:

    - B is a constant that depends on the sub-model and the data source .
    - Effort is the estimated effort in person-months .
    - F is an exponent that depends on the sub-model and reflects the project's concurrence and flexibility .
    - SCM is a schedule compression multiplier that reflects the trade-off between schedule and effort .

- COCOMO II provides about 20% cost and 70% time estimate accuracy, which can be improved by calibrating the model with historical data and using expert judgment .
- COCOMO II is a useful tool for software project managers, developers, and customers to plan, control, and evaluate software projects .