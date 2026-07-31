### Chinese Remainder Theorem

The Chinese Remainder Theorem is a mathematical theorem that allows us to solve a system of linear congruences. It states that if we have a set of equations of the form:

```
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
...
x ≡ aₙ (mod mₙ)
```

where `m₁, m₂, ..., mₙ` are pairwise relatively prime integers and `a₁, a₂, ..., aₙ` are arbitrary integers, then there exists a unique solution `x` modulo `M = m₁ ⋅ m₂ ⋅ ... ⋅ mₙ`.

#### Algorithm

The algorithm for finding the solution `x` involves finding the constants `Mᵢ`, `yᵢ`, and `zᵢ` for each equation in the system:

- `Mᵢ = M / mᵢ`
- `yᵢ` is the modular inverse of `Mᵢ` modulo `mᵢ`
- `zᵢ = yᵢ ⋅ Mᵢ`

Then the solution `x` is given by:

```
x = (a₁ ⋅ z₁ + a₂ ⋅ z₂ + ... + aₙ ⋅ zₙ) mod M
```

#### Example

Suppose we have the system of equations:

```
x ≡ 2 (mod 3)
x ≡ 3 (mod 5)
x ≡ 2 (mod 7)
```

We can find the solution using the following steps:

1. Compute `M = 3 ⋅ 5 ⋅ 7 = 105`.
2. Compute `M₁ = M / 3 = 35`, `M₂ = M / 5 = 21`, and `M₃ = M / 7 = 15`.
3. Compute the modular inverses: `y₁ = 2`, `y₂ = 1`, and `y₃ = 1`.
4. Compute the constants: `z₁ = 2 ⋅ 35 = 70`, `z₂ = 1 ⋅ 21 = 21`, and `z₃ = 1 ⋅ 15 = 15`.
5. Compute `x = (2 ⋅ 70 + 3 ⋅ 21 + 2 ⋅ 15) mod 105 = 23`.

Therefore, the solution to the system of equations is `x ≡ 23 (mod 105)`.

#### Applications

The Chinese Remainder Theorem has many applications in number theory, cryptography, and computer science. It is used in the RSA algorithm for public key cryptography, and in the construction of error-correcting codes. It can also be used to speed up some algorithms by breaking them down into smaller subproblems that can be solved independently.