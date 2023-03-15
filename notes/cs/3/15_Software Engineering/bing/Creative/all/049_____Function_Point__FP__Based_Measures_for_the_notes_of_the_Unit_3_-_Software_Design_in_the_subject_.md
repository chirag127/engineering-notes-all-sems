# Function Point (FP) Based Measures

- Function points are a measure of software size based on the functionality of the system from the user's point of view .
- Function points can be used to estimate the cost, effort and duration of software development projects .
- Function points can also be used to compare the productivity and quality of different software projects or processes .
- Function points are calculated by counting the number of inputs, outputs, inquiries, internal files and external files in the system and adjusting that total for the functional complexity of the system   .
- The steps for counting function points are :
  - Identify the type and number of each function in the system and assign a weight to each function based on its complexity (low, average or high).
  - Calculate the unadjusted function point (UFP) by multiplying the number and weight of each function and summing them up.
  - Calculate the complexity adjustment factor (CAF) by rating the system on 14 general system characteristics (GSCs) such as data communications, distributed functions, performance, etc. and summing them up.
  - Calculate the adjusted function point (AFP) by multiplying the UFP and the CAF.
- The formula for calculating function points is :

  - `FP = UFP * CAF`
  - `UFP = ∑(number of functions * weight of functions)`
  - `CAF = 0.65 + 0.01 * ∑(GSC ratings)`
- Function points can be converted to lines of code (LOC) by using a language-specific conversion factor .
- Function points have some advantages and disadvantages over LOC as a measure of software size :
  - Advantages:
    - Function points are independent of the programming language, tools and methods used for development.
    - Function points can be estimated early in the development process based on the user requirements.
    - Function points reflect the user's perspective of the system functionality and value.
  - Disadvantages:
    - Function points are subjective and may vary depending on the experience and judgment of the counter.
    - Function points are not suitable for measuring the size of low-level or non-functional software components such as algorithms, data structures, etc.
    - Function points require a standard and consistent counting method and a reliable database of historical data for comparison and estimation.