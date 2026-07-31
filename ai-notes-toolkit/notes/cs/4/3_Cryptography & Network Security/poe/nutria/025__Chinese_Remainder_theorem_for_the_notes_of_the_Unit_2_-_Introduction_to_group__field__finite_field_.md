
### Chinese Remainder Theorem

The Chinese Remainder Theorem is an important theorem in the field of Cryptography & Network Security. It is used to solve systems of congruences in the form of:

* $$x \equiv a_1 \pmod {n_1}$$
* $$x \equiv a_2 \pmod {n_2}$$
* $$\vdots$$
* $$x \equiv a_k \pmod {n_k}$$

where $a_1, a_2, \ldots, a_k$ and $n_1, n_2, \ldots, n_k$ are given integers such that $n_1, n_2, \ldots, n_k$ are pairwise relatively prime.

The Chinese Remainder Theorem states that there is a unique solution modulo $N = n_1 \cdot n_2 \cdots n_k$ for the system of congruences, where $N$ is called the product of the moduli. The solution is given by:

$$x \equiv \sum_{i=1}^{k} a_i \cdot M_i \cdot y_i \pmod N$$

where $M_i = \frac{N}{n_i}$ and $y_i$ is the modular multiplicative inverse of $M_i$ modulo $n_i$.

The Chinese Remainder Theorem is used in the Advanced Encryption Standard (AES) encryption and decryption, Primarily testing, Discrete Logarithmic Problem and security of RSA algorithms. It is also used in the Extended Euclidean Algorithm and in the study of groups, fields, finite fields of the form GF(p), modular arithmetic, prime and relative prime numbers.