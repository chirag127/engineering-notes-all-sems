### COSMIC Full Function Points in SPM

COSMIC Full Function Points (CFFP) is a sizing method used in Software Project Management (SPM) to measure the functional size of a software system. CFFP is widely used in the industry as it provides a standardized approach to measure the size of a software system and enables the estimation of development effort and cost.

The CFFP method considers five functional user-related data types: inputs, outputs, inquiries, internal logical files, and external interface files. The size of each data type is determined by counting the number of data elements and the complexity of each data element. The complexity of a data element is based on the number of attributes associated with it, such as data type, length, and format.

The following are the steps to calculate CFFP:

1. Identify the functional user-related data types: inputs, outputs, inquiries, internal logical files, and external interface files.
2. Count the number of data elements and their complexity for each data type.
3. Calculate the unadjusted function point count (UFP) by summing up the weighted size of each data type.
4. Calculate the value adjustment factor (VAF) based on 14 general system characteristics, such as distributed data processing, performance, and ease of use.
5. Calculate the adjusted function point count (AFP) by multiplying the UFP with the VAF.

Mnemonics and Learning Tricks for CFFP in SPM:

- Remember the acronym "IOIEE" to recall the functional user-related data types: Inputs, Outputs, Inquiries, External Interface Files, and Internal Logical Files.
- Use the acronym "DIAL" to remember the 14 general system characteristics that determine the value adjustment factor: Data communications, Internal processing logic, Accuracy, Performance, Heavily used configuration, Transaction rate, Online data entry, End-user efficiency, Operational ease, Multiple sites, Facilitate change, Concurrent users, Security, and Ease of installation.

Advantages of CFFP in SPM:

- Provides a standardized approach to measure the functional size of a software system.
- Enables the estimation of development effort and cost based on the size of the software system.
- Considers the complexity of data elements, which reflects the effort required to implement them.
- Can be used in various software development models such as Waterfall, Agile, and DevOps.

Disadvantages of CFFP in SPM:

- Requires a significant effort to count the number of data elements and their complexity accurately.
- Does not consider the non-functional requirements of the software system.
- Not suitable for small software systems as the effort required to calculate CFFP may be more than the effort required to develop the software system.

Example of CFFP in SPM:

Suppose a software system has 50 inputs, 30 outputs, 20 inquiries, 5 internal logical files, and 10 external interface files. The complexity of the data elements for each data type is as follows:

- Inputs: 250 simple, 100 average, and 50 complex data elements
- Outputs: 100 simple, 60 average, and 30 complex data elements
- Inquiries: 50 simple, 30 average, and 10 complex data elements
- Internal logical files: 20 simple, 10 average, and 5 complex data elements
- External interface files: 15 simple, 5 average, and 5 complex data elements

The unadjusted function point count (UFP) can be calculated as follows:

UFP = (50 x 4) + (30 x 5) + (20 x 4) + (5 x 10) + (10 x 7) = 400

Assuming the value adjustment factor (VAF) is 1.15, the adjusted function point count (AFP) can be calculated as follows:

AFP = UFP x VAF = 400 x 1.15 = 460

Applications of CFFP in SPM:

- Can be used to estimate the development effort and cost of a software system.
- Can be used to compare the size of different software systems developed using different technologies or methodologies.
- Can be used to track the progress of a software development project by measuring the size of the software system at different stages of development.