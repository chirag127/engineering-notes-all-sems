### A Parametric Productivity Model in spm

- A parametric productivity model is a mathematical model that relates the output of a software project to the input factors, such as size, complexity, quality, resources, etc.
- A parametric productivity model can be used to estimate the cost, effort, schedule, and quality of a software project, as well as to compare different alternatives and optimize the project plan.
- A parametric productivity model is based on empirical data and statistical analysis, and it can be calibrated to fit the specific characteristics of a software organization or domain.
- One of the most widely used parametric productivity models in software engineering is COCOMO (Constructive Cost Model), which was developed by Barry Boehm in 1981 and revised in 2000.
- COCOMO consists of three levels of models: basic, intermediate, and detailed, which differ in the number and complexity of the input factors and the equations used to calculate the output.
- The basic COCOMO model estimates the effort (in person-months) required to develop a software project based on the size (in thousands of source lines of code) and the mode (organic, semi-detached, or embedded) of the project. The mode reflects the degree of novelty, flexibility, and reliability required for the project.
- The basic COCOMO model has the following equation:

  Effort = a * (Size) ^ b

  where a and b are constants that depend on the mode of the project.

- The intermediate COCOMO model refines the basic model by introducing 15 cost drivers that account for the attributes of the product, the hardware, the personnel, and the project. The cost drivers are rated on a scale from very low to very high, and each rating has a corresponding multiplier that affects the effort estimation. The intermediate COCOMO model has the following equation:

  Effort = a * (Size) ^ b * EAF

  where EAF is the effort adjustment factor, which is the product of the multipliers of the 15 cost drivers.

- The detailed COCOMO model further refines the intermediate model by dividing the software project into different phases, such as planning, design, coding, testing, and integration, and estimating the effort and schedule for each phase separately. The detailed COCOMO model also considers the reuse and reengineering of existing software components, and the impact of risk analysis and management on the project.
- A mnemonic to remember the three levels of COCOMO models is:

  Basic COCOMO: Size and Mode

  Intermediate COCOMO: Size, Mode, and Cost Drivers

  Detailed COCOMO: Size, Mode, Cost Drivers, and Phases

- A parametric productivity model in spm can be implemented using various software tools, such as SPM, FSL, and AFNI, which allow the user to specify the input factors, perform the calculations, and visualize the results.
- A parametric productivity model in spm can be validated and evaluated using various criteria, such as accuracy, reliability, consistency, simplicity, generality, and adaptability.