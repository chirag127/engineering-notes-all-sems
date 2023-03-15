# Array Multiplier

- An array multiplier is a digital combinational circuit used for multiplying two binary numbers by employing an array of full adders and half adders .
- This array is used for the nearly simultaneous addition of the various product terms involved.
- To form the various product terms, an array of AND gates is used before the Adder array.
- The main advantage of the array multiplier is its simple design and regular structure.
- The disadvantage of the array multiplier is the high delay and high power consumption.
- The array multiplier can be implemented using different logic styles, such as DPTL (Double Pass Transistor Logic), which can reduce the power and area.
- The array multiplier can be generalized for any n-bit inputs as follows:

![Array multiplier diagram](https://media.geeksforgeeks.org/wp-content/uploads/20191230155130/Array-Multiplier-in-Digital-Logic.png)

- The array multiplier consists of n rows and n+1 columns of full adders and half adders.
- The first row consists of n half adders, which generate the least significant bit (LSB) of the product and the carry bits for the next row.
- The remaining rows consist of n full adders, which add the carry bits from the previous row and the product bits from the AND array.
- The final row consists of n+1 full adders, which generate the most significant bit (MSB) of the product and the final carry bit.
- The array multiplier can be extended for signed multiplication by using the Booth algorithm or the Baugh-Wooley algorithm, which reduce the number of partial products and the adder array size.