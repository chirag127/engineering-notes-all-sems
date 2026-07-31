Hello, I am Sydney, your AI assistant. I can help you with your study material for Cryptography & Network Security. Here is the content for the topic of modular arithmetic for the notes of the Unit 2.

# Modular Arithmetic

- Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" when reaching a certain value, called the modulus.
- The modulus is denoted by a positive integer m, and the set of all integers that are congruent modulo m is denoted by Z_m.
- Two integers a and b are said to be congruent modulo m, written as a ≡ b (mod m), if they have the same remainder when divided by m, or equivalently, if m divides their difference, i.e., m | (a - b).
- Congruence modulo m is an equivalence relation, meaning that it satisfies the following properties:
  - Reflexive: a ≡ a (mod m) for any integer a.
  - Symmetric: if a ≡ b (mod m), then b ≡ a (mod m).
  - Transitive: if a ≡ b (mod m) and b ≡ c (mod m), then a ≡ c (mod m).
- Congruence modulo m also preserves the operations of addition, subtraction, and multiplication, meaning that the following properties hold:
  - Closure: if a ≡ b (mod m) and c ≡ d (mod m), then a + c ≡ b + d (mod m) and a - c ≡ b - d (mod m) and a * c ≡ b * d (mod m).
  - Associative: if a, b, and c are any integers, then (a + b) + c ≡ a + (b + c) (mod m) and (a - b) - c ≡ a - (b - c) (mod m) and (a * b) * c ≡ a * (b * c) (mod m).
  - Commutative: if a and b are any integers, then a + b ≡ b + a (mod m) and a - b ≡ -(b - a) (mod m) and a * b ≡ b * a (mod m).
  - Distributive: if a, b, and c are any integers, then a * (b + c) ≡ a * b + a * c (mod m) and a * (b - c) ≡ a * b - a * c (mod m).
- However, congruence modulo m does not preserve the operation of division, meaning that the following property does not hold in general:
  - Inverse: if a ≡ b (mod m) and c ≡ d (mod m), then a / c ≡ b / d (mod m).
- This is because division by c or d may not be well-defined in Z_m, i.e., there may not exist an integer x such that c * x ≡ 1 (mod m) or d * x ≡ 1 (mod m).
- Such an integer x is called a multiplicative inverse of c or d modulo m, and it exists if and only if c and m or d and m are coprime, i.e., their greatest common divisor (gcd) is 1.
- The gcd of two integers a and b can be computed using the Euclidean algorithm, which repeatedly applies the division algorithm until the remainder is zero, i.e.,

  - a = b * q_0 + r_0, where 0 ≤ r_0 < b
  - b = r_0 * q_1 + r_1, where 0 ≤ r_1 < r_0
  - r_0 = r_1 * q_2 + r_2, where 0 ≤ r_2 < r_1
  - ...
  - r_k-2 = r_k-1 * q_k + r_k, where 0 ≤ r_k < r_k-1
  - r_k-1 = r_k * q_k+1 + 0

  - The last nonzero remainder r_k is the gcd of a and b, denoted by gcd(a, b) = r_k.
- The multiplicative inverse of c modulo m can be computed using the extended Euclidean algorithm, which extends the Euclidean algorithm by keeping track of two auxiliary variables s and t, such that

  - a * s + b * t = r_k

  - If r_k = 1, then s is the multiplicative inverse of a modulo b, and t is the multiplicative inverse of b modulo