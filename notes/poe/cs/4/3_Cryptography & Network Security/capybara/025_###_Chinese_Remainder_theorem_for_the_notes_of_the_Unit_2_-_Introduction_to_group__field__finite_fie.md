### Chinese Remainder theorem

The Chinese Remainder theorem is a mathematical theorem that provides a solution to a system of linear congruences. It is a useful tool in many areas of mathematics and computer science, including cryptography.

#### Definition

Given a system of linear congruences 

```
x ≡ a1 (mod n1)
x ≡ a2 (mod n2)
...
x ≡ ak (mod nk)
```

where the moduli `n1, n2, ..., nk` are pairwise relatively prime, the Chinese Remainder theorem states that there exists a unique solution `x` modulo `n1n2...nk`.

#### Mnemonic

One useful mnemonic for remembering the Chinese Remainder theorem is "Chinese food doesn't mix." This refers to the fact that the moduli in the system of congruences must be pairwise relatively prime in order for the theorem to apply.

#### Example

Suppose we want to solve the system of congruences 

```
x ≡ 2 (mod 3)
x ≡ 3 (mod 5)
x ≡ 2 (mod 7)
```

The moduli 3, 5, and 7 are pairwise relatively prime, so we can apply the Chinese Remainder theorem. We first compute `N = 3 * 5 * 7 = 105`. Then we compute `Ni = N / ni` for each `ni` in the system:

```
N1 = 105 / 3 = 35
N2 = 105 / 5 = 21
N3 = 105 / 7 = 15
```

Next, we compute the inverses `yi` of each `Ni` modulo `ni`:

```
35 * 2 ≡ 1 (mod 3)   -> y1 = 2
21 * 1 ≡ 1 (mod 5)   -> y2 = 1
15 * 5 ≡ 1 (mod 7)   -> y3 = 5
```

Finally, we compute the solution `x` as 

```
x = a1N1y1 + a2N2y2 + a3N3y3
  = 2 * 35 * 2 + 3 * 21 * 1 + 2 * 15 * 5
  = 233
```

We can check that this solution satisfies all three congruences.

#### Applications

The Chinese Remainder theorem has many applications in mathematics and computer science, including:

- Error-correcting codes
- Cryptography, including the RSA algorithm
- Computer graphics and image processing
- Signal processing