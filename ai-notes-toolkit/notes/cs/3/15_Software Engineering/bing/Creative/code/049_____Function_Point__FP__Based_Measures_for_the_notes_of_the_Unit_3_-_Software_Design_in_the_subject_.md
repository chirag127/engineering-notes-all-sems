### Function Point (FP) Based Measures

- Function points are a unit of measurement used to quantify the amount of business functionality being delivered by a software application.
- Function points measure the size of an application system based on the functional view of the system.
- Function points allow software engineers to better measure the size of a project, identify areas in need of optimization, and analyze development performance benchmarks over time.
- Function points are one of the most widely used measures of software size .
- The basis of function points is that the “functionality” of the system, that is, what the system performs, is the measure of the system size .
- Function points are independent of the programming language, technology, and development methodology used to build the software application.
- Function points are calculated by counting the number of inputs, outputs, queries, internal files and external files in the system and adjusting that total for the functional complexity of the system .
- The steps for counting function points are:
  - Identify the type of project (development, enhancement, or maintenance) and the type of count (application or project).
  - Identify the user requirements and the scope and boundary of the system.
  - Identify and count the data functions (internal logical files and external interface files) and assign complexity weights to them.
  - Identify and count the transactional functions (external inputs, external outputs, and external inquiries) and assign complexity weights to them.
  - Calculate the unadjusted function point (UFP) by summing up the complexity weights of all the data and transactional functions.
  - Determine the value adjustment factor (VAF) by rating 14 general system characteristics (GSCs) on a scale of 0 to 5 and summing up the ratings.
  - Calculate the adjusted function point (AFP) by multiplying the UFP by the VAF.
- Function points can be used to estimate the effort, cost, and duration of a software project by using productivity rates, cost per function point, and delivery rates derived from historical data or industry benchmarks .
- Function points can also be used to measure the productivity, quality, and value of software development and maintenance activities by using metrics such as function points per person-month, defects per function point, and function points per dollar .
- Function points are suitable for measuring the size of management information system (MIS) software, but may not be applicable for other types of software such as real-time, embedded, or scientific software.