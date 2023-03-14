Constructive Cost Models (COCOMO) are a family of software cost estimation models that are based on the number of lines of code (LOC) and other project attributes. They are used to predict the effort, cost, and schedule of software projects. There are three main types of COCOMO models: Basic, Intermediate, and Detailed.

The Basic COCOMO model is the simplest and most general one. It uses only the LOC and a mode (organic, semi-detached, or embedded) to estimate the effort and schedule. The mode reflects the complexity and difficulty of the project. The Basic COCOMO model has the following formulas:

Effort = a * (LOC) ^ b
Schedule = c * (Effort) ^ d

Where a, b, c, and d are constants that depend on the mode. The effort is measured in person-months and the schedule is measured in months.

The Intermediate COCOMO model is more refined and accurate than the Basic COCOMO model. It uses the LOC and a set of 15 cost drivers to estimate the effort and schedule. The cost drivers are factors that affect the productivity and quality of the software development, such as the required reliability, the experience of the team, the use of modern tools, etc. The Intermediate COCOMO model has the following formulas:

Effort = a * (LOC) ^ b * EAF
Schedule = c * (Effort) ^ d * SCED

Where a, b, c, and d are constants that depend on the mode, EAF is the effort adjustment factor, and SCED is the schedule compression factor. The EAF is the product of the ratings of the 15 cost drivers, and the SCED is a factor that reflects the trade-off between the schedule and the effort.

The Detailed COCOMO model is the most detailed and accurate one. It uses the LOC and a set of 17 cost drivers to estimate the effort and schedule for each phase of the software development life cycle, such as requirements analysis, design, coding, testing, etc. The Detailed COCOMO model has the following formulas:

Effort = a * (LOC) ^ b * EAF
Schedule = c * (Effort) ^ d * SCED

Where a, b, c, and d are constants that depend on the mode and the phase, EAF is the effort adjustment factor, and SCED is the schedule compression factor. The EAF and the SCED are the same as in the Intermediate COCOMO model, but they may vary for each phase.

The following diagram illustrates the basic architecture of a COCOMO model:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Basic COCOMO   |     | Intermediate    |     |  Detailed       |
|                 |     | COCOMO          |     |  COCOMO         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  LOC            |     |  LOC            |     |  LOC            |
|  Mode           |     |  Mode           |     |  Mode           |
|                 |     |  Cost Drivers   |     |  Cost Drivers   |
|                 |     |                 |     |  Phases         |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Effort         |     |  Effort         |     |  Effort         |
|  Schedule       |     |  Schedule       |     |  Schedule       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```