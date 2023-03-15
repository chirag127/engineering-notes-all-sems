### COSMIC Full Function Points in SPM

COSMIC Full Function Points (CFFP) is a software measurement technique used to measure the functional size of a software application or system. It is a widely used metric in software project management (SPM) and is used to estimate the size and complexity of software development projects. In this section, we will discuss CFFP in detail.

#### What are COSMIC Full Function Points?

CFFP is a method for measuring the functional size of a software application or system. It is based on the concept of the functional requirements of the software. The functional requirements are those requirements that describe what the software is supposed to do rather than how it does it. The CFFP method measures the functional size of the software by counting the number of functional requirements and their associated data elements.

#### How are COSMIC Full Function Points calculated?

The CFFP method consists of six steps, which are as follows:

1. Identify the function types: The first step is to identify the five function types that are used in the CFFP method. These function types include data functions, transactional functions, inquiry functions, internal logic files, and external interface files.

2. Identify the data elements: The second step is to identify the data elements that are associated with each function type. These data elements include inputs, outputs, inquiries, and files.

3. Count the data elements: The third step is to count the number of data elements associated with each function type.

4. Assign complexity values: The fourth step is to assign complexity values to each data element based on its complexity. The complexity values range from 1 to 15.

5. Calculate the unadjusted function points: The fifth step is to calculate the unadjusted function points by adding the complexity values of all the data elements.

6. Calculate the adjusted function points: The sixth and final step is to calculate the adjusted function points by multiplying the unadjusted function points by a set of complexity factors. These complexity factors take into account the complexity of the software application or system.

#### Advantages of COSMIC Full Function Points

- CFFP is a standardized and widely accepted metric for measuring the functional size of a software application or system.
- CFFP is more accurate and reliable than other software measurement techniques as it takes into account the complexity of the software application or system.
- CFFP is useful in estimating the effort and cost required for software development projects.

#### Disadvantages of COSMIC Full Function Points

- CFFP is a complex and time-consuming metric to calculate.
- CFFP requires a detailed understanding of the functional requirements of the software application or system.
- CFFP may not be suitable for all types of software applications or systems.

#### Mnemonics and Learning Tricks for COSMIC Full Function Points

Unfortunately, there are no easy-to-remember mnemonics or learning tricks for CFFP. However, it is important to understand the six steps of the CFFP method and practice calculating CFFP for different software development projects to become proficient in using this metric.

#### Example of COSMIC Full Function Points

Let's consider an example to understand how CFFP is calculated. Suppose we have a software application that has the following functional requirements:

- 10 data inputs
- 5 data outputs
- 3 inquiries
- 2 internal logic files
- 1 external interface file

The complexity values assigned to each data element are as follows:

- Data inputs: 5
- Data outputs: 4
- Inquiries: 3
- Internal logic files: 10
- External interface files: 7

Using the CFFP method, we can calculate the unadjusted function points as follows:

Unadjusted function points = (10 x 5) + (5 x 4) + (3 x 3) + (2 x 10) + (1 x 7) = 87

To calculate the adjusted function points, we need to use the complexity factors. The complexity factors for our software application are as follows:

- Data communication: 4
- Distributed functions: 1
- Performance: 1
- Heavily used configuration: 1
- Transaction rate: 3
- Online data entry: 1
- End-user efficiency: 3
- Online update: 1
- Complex processing: 1
- Reusability: 1

Using these complexity factors, we can calculate the adjusted function points as follows:

Adjusted function points = Unadjusted function points x complexity factors
= 87 x 4 x 1 x 1 x 1 x 3 x 1 x 3 x 1 x 1
= 1044

#### Applications of COSMIC Full Function Points

CFFP is widely used in software project management to estimate the size and complexity of software development projects. It is also used in software quality assurance to measure the functional size of software applications or systems. CFFP is particularly useful for