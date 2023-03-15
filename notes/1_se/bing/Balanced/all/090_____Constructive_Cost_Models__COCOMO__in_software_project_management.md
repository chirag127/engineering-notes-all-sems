# Constructive Cost Models (COCOMO) in software project management

- Constructive Cost Models (COCOMO) are a set of empirical models that estimate the effort, cost and schedule of software projects based on various input parameters such as size, complexity, quality, experience, etc.
- COCOMO was developed by Barry Boehm in 1981 and has been revised and extended over the years to adapt to different types of software projects and development environments.
- COCOMO consists of three levels of models: basic, intermediate and detailed, each with increasing accuracy and complexity.
- Basic COCOMO model estimates the effort and duration of a software project based on a single parameter: the number of delivered source lines of code (SLOC). It also assumes a nominal value for all other factors affecting the project.
- Intermediate COCOMO model refines the basic model by introducing 15 cost drivers that adjust the effort and duration estimates based on the characteristics of the software product, the hardware platform, the personnel and the project attributes.
- Detailed COCOMO model further refines the intermediate model by dividing the software project into different phases or modules and applying different effort multipliers and scale factors for each phase or module.
- COCOMO models use the following formula to estimate the effort (E) in person-months:

  E = a * (KLOC)^b * EM

  where a and b are constants derived from historical data, KLOC is the number of delivered source lines of code in thousands, and EM is the effort multiplier that accounts for the cost drivers.

- COCOMO models use the following formula to estimate the duration (D) in months:

  D = c * (E)^d * SCED

  where c and d are constants derived from historical data, E is the effort in person-months, and SCED is the schedule compression or expansion factor that accounts for the project deadline.

- COCOMO models can be used to support various software project management activities such as planning, budgeting, monitoring, controlling and risk analysis. They can also be used to compare different alternatives and trade-offs in software development.