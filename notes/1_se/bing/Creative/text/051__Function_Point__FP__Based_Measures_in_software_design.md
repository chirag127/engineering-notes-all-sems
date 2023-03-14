##### Function Point (FP) Based Measures in software design

- Function Point (FP) is an element of software development that helps to approximate the cost of development early in the process. It measures functionality from the user's point of view, based on the user's external view of the functional requirements .
- Function Point Analysis (FPA) is a method or set of rules to functionally size the software work product, which is the output of software new development and improvement projects.
- FPA involves counting the number of function units, which are classified into two types: transactional functional type and data functional type.
  - Transactional functional type consists of external input (EI), external output (EO), and external inquiries (EQ), which are elementary processes that process data or control information that comes from or goes to outside the application's boundary.
  - Data functional type consists of internal logical file (ILF) and external interface file (EIF), which are user identifiable groups of logically related data or control information maintained within or outside the application's boundary.
- Each function unit is assigned a weight based on its complexity, which is determined by the number of data elements and file types referenced by the function unit .
- The unadjusted function point (UFP) is the sum of the weighted function units .
- The UFP is then adjusted by a complexity adjustment factor (CAF), which is calculated by rating 14 general system characteristics (GSCs) on a scale of 0 to 5 according to their influence on the system's functionality .
- The function point (FP) is the product of the UFP and the CAF .
- FP can be used to estimate the cost, duration, and amount of resources required by a software project, as well as to measure the productivity and quality of the software development process .
- FP is independent of the technology used for implementation and can be applied to different types of software projects, such as new development, enhancement, maintenance, and package evaluation .