## Implementation of 4-bit parallel adder using 7483 IC

- A 4-bit parallel adder is a logic circuit that can perform the addition of two 4-bit binary numbers and produce a 4-bit sum and a carry output.
- A 7483 IC is a 16-pin integrated circuit that contains four full adders and a look-ahead carry circuit. It can be used to implement a 4-bit parallel adder by connecting the inputs and outputs as shown below :

![7483 IC pin diagram](https://eees.in/wp-content/uploads/2021/10/7483-pin-diagram.png)

- The inputs A3, A2, A1, A0 and B3, B2, B1, B0 are the 4-bit numbers to be added. The outputs S3, S2, S1, S0 are the 4-bit sum. The inputs C0 and C4 are the carry-in and carry-out respectively.
- The truth table for the 4-bit parallel adder using 7483 IC is given below:

![7483 IC truth table](https://eees.in/wp-content/uploads/2021/10/7483-truth-table.png)

- The 7483 IC can also be used to perform subtraction of two 4-bit numbers by using the 2's complement method. To do this, the B inputs are complemented and a 1 is added to the carry-in C0. The outputs S3, S2, S1, S0 are the 4-bit difference and C4 is the borrow-out .
- The 7483 IC can also be cascaded to perform addition or subtraction of larger numbers. For example, to add two 8-bit numbers, two 7483 ICs can be connected as shown below:

![7483 IC cascading](https://www.ques10.com/uploads/userfiles/images/2016/11/6212/6212_1.png)

- The 7483 IC can also be used to perform addition of BCD numbers by adding a correction factor of 6 (0110) to the sum if it is not a valid BCD digit or if a carry is generated.