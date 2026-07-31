##### Function Point (FP) Based Measures in software design

- Function Point (FP) is a unit of measurement to express the amount of business functionality, an information system (as a product) provides to a user .
- FPs measure software size and are widely accepted as an industry standard for functional sizing.
- FPs are derived using an empirical relationship based on countable measures of software's information domain and assessments of software complexity.
- FPs can be used to estimate project cost and effort, as well as to compare the productivity and quality of different software projects .
- The basic steps of FP based estimation are  :
  - Identify the functions that the software system provides to the user. These functions are classified into five types: external inputs, external outputs, external inquiries, internal logical files, and external interface files.
  - Assign a complexity level (low, average, or high) to each function based on the number of data elements and file types involved.
  - Use a table of complexity weights to calculate the unadjusted function points (UFP) for each function type and sum them up.
  - Calculate the value adjustment factor (VAF) based on 14 general system characteristics that affect the functionality of the software system. The VAF ranges from 0.65 to 1.35.
  - Multiply the UFP by the VAF to get the adjusted function points (AFP).
  - Use a productivity factor (PF) to convert the AFP into effort or cost. The PF depends on the development environment, the programming language, the team experience, and other factors.
- A mnemonic to remember the five function types is **IIEEO** (Inputs, Inquiries, External files, External outputs, and internal logical files).
- A mnemonic to remember the 14 general system characteristics is **DIDRERDUCER** (Distributed data processing, Data communications, Data transactions, Reusability, End-user efficiency, Online data entry, Online update, Complex processing, Installation ease, Operational ease, Multiple sites, Facilitate change, Performance, and Backup and recovery).