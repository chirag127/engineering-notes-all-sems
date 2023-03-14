### Modular arithmetic

Modular arithmetic is a system of arithmetic for integers, where values reset to zero and begin to increase again, after reaching a certain predefined value, called the modulus (modulo). Modular arithmetic is widely used in computer science and cryptography.

Some basic concepts of modular arithmetic are:

- Modulo operator: The modulo operator (abbreviated as mod) is used to find the remainder when one integer is divided by another. For example, 7 mod 3 = 1, because 7 divided by 3 gives a quotient of 2 and a remainder of 1.
- Congruence modulo: Two integers are said to be congruent modulo n if they have the same remainder when divided by n. For example, 15 and 27 are congruent modulo 3, because 15 mod 3 = 0 and 27 mod 3 = 0. We write this as 15 ≡ 27 (mod 3).
- Modular addition and subtraction: The addition and subtraction of two integers modulo n can be done by adding or subtracting their remainders modulo n, and then taking the remainder of the result modulo n. For example, (15 + 27) mod 3 = (0 + 0) mod 3 = 0, and (15 - 27) mod 3 = (0 - 0) mod 3 = 0.
- Modular multiplication and exponentiation: The multiplication and exponentiation of two integers modulo n can be done by multiplying or exponentiating their remainders modulo n, and then taking the remainder of the result modulo n. For example, (15 * 27) mod 3 = (0 * 0) mod 3 = 0, and (15^27) mod 3 = (0^0) mod 3 = 1.
- Modular inverse: The modular inverse of an integer a modulo n is an integer b such that (a * b) mod n = 1. For example, the modular inverse of 3 modulo 7 is 5, because (3 * 5) mod 7 = 1. Not every integer has a modular inverse modulo n. For example, 2 has no modular inverse modulo 4, because there is no integer b such that (2 * b) mod 4 = 1.

Modular arithmetic is useful for cryptography because it allows us to perform arithmetic operations on large numbers without worrying about overflow or loss of precision. It also allows us to create mathematical structures that have desirable properties for encryption and decryption, such as groups, fields, and finite fields. Some examples of cryptographic algorithms that use modular arithmetic are:

- RSA: RSA is a public-key cryptosystem that uses modular exponentiation and modular inverse to encrypt and decrypt messages. The security of RSA relies on the difficulty of factoring large numbers into primes.
- Diffie-Hellman: Diffie-Hellman is a key exchange protocol that uses modular exponentiation to generate a shared secret key between two parties. The security of Diffie-Hellman relies on the difficulty of solving the discrete logarithm problem.
- AES: AES is a symmetric-key cryptosystem that uses modular addition, subtraction, multiplication, and inverse to perform various transformations on blocks of data. The security of AES relies on the complexity and non-linearity of these transformations.