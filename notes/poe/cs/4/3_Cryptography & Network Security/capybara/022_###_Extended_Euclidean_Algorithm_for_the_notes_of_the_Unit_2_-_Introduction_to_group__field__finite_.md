### Extended Euclidean Algorithm

The Extended Euclidean Algorithm is a way to find the greatest common divisor (GCD) of two integers, as well as a way to find the coefficients that make up the GCD in terms of the original two integers. It is a useful tool in cryptography, particularly in the RSA algorithm.

Here are the steps to perform the Extended Euclidean Algorithm:

1. Write down the two numbers you want to find the GCD of, say a and b.
2. Divide a by b and write down the remainder, r1.
3. Divide b by r1 and write down the remainder, r2.
4. Continue this process until you get a remainder of 0.
5. Write the equation that relates the GCD to the remainders: GCD(a, b) = GCD(b, r1) = GCD(r1, r2) = ... = r_n, where r_n is the final remainder.
6. Work backwards to find the coefficients that make up the GCD: r_n = s_n * a + t_n * b, r_{n-1} = s_{n-1} * b + t_{n-1} * r_1, r_{n-2} = s_{n-2} * r_1 + t_{n-2} * r2, and so on.
7. The final coefficients are s_n and t_n, which can be used in the Euclidean Algorithm to find the modular inverse of a in the field GF(p), where p is a prime number.

Mnemonics and learning tricks for the Extended Euclidean Algorithm include:

- Remembering the phrase "reverse, divide, subtract, compare" to remember the steps of the algorithm.
- Using the acronym "E.E.A." to remember the name of the algorithm.
- Visualizing the remainders as steps on a staircase, with each step getting smaller until reaching 0.

Overall, the Extended Euclidean Algorithm is an important tool in cryptography, particularly for finding modular inverses in the RSA algorithm. Understanding the steps of the algorithm and using helpful mnemonics can aid in remembering and applying this concept on exams.