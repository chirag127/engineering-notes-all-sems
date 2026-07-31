### Lagrange's theorem for the notes of the Unit 2 - Algebraic Structures in the subject of Discrete Structures & Theory of Logic

- Lagrange's theorem is one of the central theorems of abstract algebra  .
- It states that in group theory, for any finite group say G, the order of subgroup H of group G divides the order of G  .
- The order of the group represents the number of elements .
- Mathematically, Lagrange's theorem can be written as:

```
|G| = n|H|
```

where |G| is the order of group G, |H| is the order of subgroup H, and n is a positive integer called the index of H in G .

- Lagrange's theorem implies that every element of the group G shows up in some coset of H.
- A coset of H in G is a subset of G that is obtained by multiplying all the elements of H by a fixed element of G .
- There are two types of cosets: left cosets and right cosets .
- A left coset of H in G is denoted by gH, where g is any element of G, and it is defined as:

```
gH = {gh : h ∈ H}
```

- A right coset of H in G is denoted by Hg, where g is any element of G, and it is defined as:

```
Hg = {hg : h ∈ H}
```

- Lagrange's theorem also implies that every coset of H in G has the same number of elements as H.
- Furthermore, the cosets of H in G form a partition of G, that is, they are disjoint and their union is G .
- For example, if G is the group of integers under addition, and H is the subgroup of even integers, then the cosets of H in G are:

```
0 + H = {0, 2, -2, 4, -4, ...}
1 + H = {1, 3, -1, 5, -3, ...}
```

- The order of G is infinite, but the order of H is countably infinite, so Lagrange's theorem does not apply in this case.
- However, if we consider a finite group, such as the group of integers modulo 6 under addition, denoted by Z6, and the subgroup of multiples of 3, denoted by 3Z6, then Lagrange's theorem applies and we have:

```
|Z6| = 6
|3Z6| = 2
n = 3
```

- The cosets of 3Z6 in Z6 are:

```
0 + 3Z6 = {0, 3}
1 + 3Z6 = {1, 4}
2 + 3Z6 = {2, 5}
```

- These cosets are also equal to the right cosets of 3Z6 in Z6, since the group operation is commutative.
- Lagrange's theorem has many applications and consequences in group theory, such as the Euler's theorem, Fermat's little theorem, and the Cauchy's theorem.