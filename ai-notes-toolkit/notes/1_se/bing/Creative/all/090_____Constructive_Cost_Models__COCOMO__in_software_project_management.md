# Constructive Cost Models (COCOMO) in software project management

- COCOMO stands for **Constructive Cost Model**  , which is a **software cost estimation model**   that predicts the **effort, cost, and schedule** of a software project based on the **number of lines of code (LOC)**  .
- COCOMO was developed by **Barry W. Boehm** using data from **historical projects** to derive the **model parameters** using a **regression formula**.
- COCOMO has three versions: **COCOMO 81, COCOMO II, and COCOMO III**. COCOMO 81 is the original version, COCOMO II is the updated version that accounts for modern software development practices, and COCOMO III is the latest version that incorporates agile methods and cloud computing.
- COCOMO has three levels of complexity: **basic, intermediate, and detailed**  . Basic COCOMO uses a simple formula to estimate the effort and cost based on the LOC and a **mode**   that reflects the project type (organic, semi-detached, or embedded). Intermediate COCOMO adds **cost drivers**   that adjust the effort and cost based on various factors such as product attributes, hardware constraints, personnel characteristics, and project environment. Detailed COCOMO further divides the project into **subsystems**   and applies the intermediate COCOMO to each subsystem, taking into account the **interactions**   among them.
- COCOMO has several advantages and disadvantages as a software cost estimation model. Some of the advantages are:
  - It is **simple and easy** to use and understand.
  - It is **empirically based** on historical data and validated by many studies.
  - It is **flexible and adaptable** to different project types and development practices.
  - It provides **quantitative and objective** estimates that can be used for planning and control.
- Some of the disadvantages are:
  - It relies on **LOC** as the main input, which is not always available or accurate, and may vary depending on the programming language, coding style, and level of abstraction.
  - It assumes a **linear relationship** between LOC and effort, which may not hold for very large or complex projects.
  - It may not account for **all the factors** that affect the effort and cost, such as quality, reuse, risk, and uncertainty.
  - It may not reflect the **current trends** and technologies in software development, such as agile methods, cloud computing, and artificial intelligence.