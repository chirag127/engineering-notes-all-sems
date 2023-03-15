### COSMIC Full Function Points in SPM

COSMIC Full Function Points (CFFPs) is a software metric used to measure the functional size of a software system. It is a part of the Common Software Measurement International Consortium (COSMIC) method, which is a method for measuring software size that is widely used in the industry. In this section, we will discuss the details of CFFPs in SPM.

#### What are Function Points?

Before discussing CFFPs, it is important to understand the concept of Function Points (FPs). FPs are a unit of measure for software size. They are calculated based on the functionality provided by the software system. FPs are used to estimate the size of a software system, which in turn can be used to estimate the effort required to develop the software system.

#### What are COSMIC Full Function Points (CFFPs)?

CFFPs are a type of function point that is used to measure the functional size of a software system. They are based on the functional requirements of the software system, rather than the implementation details. CFFPs are used to measure the size of a software system in terms of the functionality it provides.

#### How do we calculate CFFPs?

The calculation of CFFPs involves the following steps:

1. Identify the types of functions provided by the software system. These functions are classified into four categories: External Inputs (EI), External Outputs (EO), External Inquiries (EQ), and Internal Logical Files (ILF).
2. Count the number of occurrences of each type of function in the software system. This count is known as the Unadjusted Function Point Count (UFP).
3. Apply complexity adjustments to the UFP to account for the complexity of the functions. This gives us the Adjusted Function Point Count (AFP).
4. Calculate the CFFP value using the following formula: CFFP = AFP / KLOC, where KLOC is the size of the software system in Kilo Lines of Code.

#### Advantages of CFFPs

- CFFPs provide a more accurate measure of software size than other metrics.
- CFFPs are based on functional requirements, which are more stable than implementation details.
- CFFPs can be used to estimate the effort required to develop a software system.

#### Disadvantages of CFFPs

- CFFPs can be difficult to calculate, especially for complex software systems.
- CFFPs do not take into account the quality of the software system.
- CFFPs may not be suitable for all types of software systems.

#### Mnemonics and Learning Tricks

There are no mnemonics or learning tricks for CFFPs that are widely used in the industry. However, it is important to understand the concept of FPs and the four categories of functions in order to calculate CFFPs accurately.

#### Examples

Let us consider an example to understand the calculation of CFFPs:

Suppose we have a software system that provides the following functions:

- 10 External Inputs
- 5 External Outputs
- 3 External Inquiries
- 2 Internal Logical Files

The Unadjusted Function Point Count (UFP) for this software system is:

UFP = 10 + 5 + 3 + (2 x 10) = 33

Suppose we apply the following complexity adjustments:

- External Inputs: Low Complexity
- External Outputs: Average Complexity
- External Inquiries: High Complexity
- Internal Logical Files: High Complexity

The Adjusted Function Point Count (AFP) for this software system is:

AFP = UFP x (0.65 + 0.01 x ΣFi) = 33 x (0.65 + 0.01 x (1 + 2 + 3 + 3)) = 36.96

Suppose the size of the software system is 20 KLOC. Then the CFFP value for this software system is:

CFFP = AFP / KLOC = 36.96 / 20 = 1.848

#### Applications

CFFPs are widely used in the industry to measure the functional size of software systems. They are used to estimate the effort required to develop a software system and to compare software systems of different sizes. CFFPs can be used in conjunction with other metrics to provide a more complete picture of the software system.