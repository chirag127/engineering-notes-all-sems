
### Booths Algorithm

* Booth's algorithm is a multiplication algorithm used in computer arithmetic. 
* It was developed by Alan M. Booth in 1950 and is primarily used in the design of hardware multipliers. 
* The algorithm is based on the idea of breaking up an n-bit multiplication into a series of 2-bit multiplications. 
* It reduces the number of partial products that need to be added together from 2^n to n-1. 
* This makes it faster than the traditional multiplication algorithm, which requires 2^n partial products. 
* Booth's algorithm can be implemented in both signed and unsigned multiplications. 
* In signed multiplication, the algorithm takes into account the sign of the multiplicands and adjusts the result accordingly. 
* In unsigned multiplication, the algorithm simply multiplies the two numbers and produces the result.
* The algorithm works by shifting the multiplicand left by one bit and adding or subtracting it from the partial product depending on the value of the multiplier bit. 
* This process is repeated until all the bits of the multiplier have been processed. 
* Finally, the partial products are added together to produce the result.