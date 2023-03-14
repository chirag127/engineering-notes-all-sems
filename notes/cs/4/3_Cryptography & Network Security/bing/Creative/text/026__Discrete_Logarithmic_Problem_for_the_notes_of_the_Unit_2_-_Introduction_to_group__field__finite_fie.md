### Discrete Logarithmic Problem

- The discrete logarithmic problem is the problem of finding an integer k such that b^k = a for given elements a and b of a group G. 
- The group G can be any group, but the problem is usually considered in the context of finite groups, such as the multiplicative group of integers modulo a prime p, denoted by Z_p^*.  
- The discrete logarithmic problem is considered to be computationally hard, meaning that no efficient algorithm is known for solving it in general.  
- The hardness of the problem depends on the choice of the group G and the generator b. Some groups have special properties that make the problem easier, such as cyclic groups or elliptic curve groups.  
- The discrete logarithmic problem is important for cryptography, as many public-key schemes are based on the assumption that it is hard to solve. For example, the Diffie-Hellman key exchange, the ElGamal encryption and signature schemes, and the Digital Signature Algorithm (DSA) rely on the hardness of the discrete logarithmic problem in Z_p^* or in elliptic curve groups.   

: https://en.wikipedia.org/wiki/Discrete_logarithm
: https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/discrete-logarithm-problem
: https://www.doc.ic.ac.uk/~mrh/330tutor/ch06s02.html
: https://www.sciencedirect.com/topics/computer-science/discrete-logarithm