 Here is the content in markdown format for the topic -

### Boundary Value Analysis for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

Boundary Value Analysis (BVA) is a software testing technique in which test cases are designed to include upper and lower boundary values of input domain of a software component.

The key advantages of BVA are:

- It helps identify errors at the boundaries of the input domain.
- It reduces the number of test cases required.
- It is an efficient way to test the input domain.

The steps to perform BVA are:

1. Identify the input variables of the component and their possible ranges.
2. Identify the logical boundaries of the input ranges. These include:
- Minimum values
- Maximum values
- Just inside/outside boundaries
- Error values
3. Generate test cases for each boundary value identified in step 2. This may require generating test cases for equivalence classes if the boundaries cut across these.
4. Execute the test cases and check for any errors.

For example, to test a discount calculation component with input price ranging from Rs. 100 to Rs. 1000 and discount percentage from 1% to 50%, the following boundary values can be identified:

Price: Rs. 100, Rs. 1000
Discount percentage: 1%, 50%

Test cases can be generated for each of these values and executed to identify any errors.

Some important points to keep in mind for BVA:

- Test at exact boundaries as well as just inside/outside boundaries if applicable.
- Error values or invalid inputs also need to be tested.
- Test cases may need to be combined to test interactions between variables and cover equivalence classes.
- The component under test should have definitive input and output domains for BVA to be applicable.