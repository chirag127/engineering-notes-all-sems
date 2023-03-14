Preventive maintenance (PM) of software is the act of performing regularly scheduled maintenance activities to help prevent unexpected failures in the future. It is also sometimes referred to as CMMS (or computerized maintenance management software.) 

Preventive maintenance software is used to simplify and streamline maintenance operations and prevent downtime. It helps produce stable operations, ensure compliance with warranties and resolve issues impacting production — before they happen. 

There are 4 major types of preventive maintenance: usage-based, calendar/time-based, predictive, and prescriptive. Each type has different triggers, methods, and outcomes for maintenance tasks.

The following diagram illustrates the basic architecture of a preventive maintenance software:

```
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Maintenance     |     |  Preventive      |     |  Maintenance     |
|  Manager         |     |  Maintenance     |     |  Technician      |
|                  |     |  Software        |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  - Creates and   |     |  - Schedules     |     |  - Receives      |
|    assigns       |     |    maintenance   |     |    notifications |
|    maintenance   |     |    tasks based   |     |    and work      |
|    plans         |     |    on type of    |     |    orders        |
|                  |     |    PM            |     |                  |
|  - Monitors      |     |  - Sends alerts  |     |  - Performs      |
|    equipment     |     |    and           |     |    maintenance   |
|    conditions    |     |    notifications |     |    tasks using   |
|                  |     |    to manager    |     |    mobile app    |
|  - Reviews and   |     |    and           |     |                  |
|    analyzes      |     |    technician    |     |  - Reports       |
|    maintenance   |     |                  |     |    results and   |
|    reports       |     |  - Generates     |     |    issues        |
|                  |     |    and stores    |     |                  |
|  - Adjusts       |     |    maintenance   |     |  - Completes     |
|    maintenance   |     |    reports       |     |    actions       |
|    schedules     |     |                  |     |                  |
|    as needed     |     |  - Integrates    |     |                  |
|                  |     |    with other    |     |                  |
|                  |     |    systems       |     |                  |
+------------------+     +------------------+     +------------------+
       |                       |   |   |                   |
       |                       |   |   |                   |
       +-----------------------+   |   +-------------------+
                                   |
                                   |
                                   v
                           +------------------+
                           |                  |
                           |  Equipment       |
                           |                  |
                           +------------------+
                           |                  |
                           |  - Provides      |
                           |    data on       |
                           |    condition,    |
                           |    usage, and    |
                           |    performance   |
                           |                  |
                           |  - Receives      |
                           |    maintenance   |
                           |    commands      |
                           |                  |
                           +------------------+
```