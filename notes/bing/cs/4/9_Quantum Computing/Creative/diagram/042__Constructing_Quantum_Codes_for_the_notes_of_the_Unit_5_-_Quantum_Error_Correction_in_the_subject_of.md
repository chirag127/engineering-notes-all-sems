One of the methods of constructing quantum codes is to use the CSS construction, which is based on classical linear codes. The CSS construction works as follows:

- Let C1 and C2 be two classical linear codes over GF(q) such that C2 ⊆ C1 ⊆ C2^⊥, where C2^⊥ is the dual code of C2.
- Define the quantum code Q as the set of all vectors |ψ> in (GF(q))^n such that |ψ> + C2 ⊆ C1.
- The dimension of Q is k1 - k2, where k1 and k2 are the dimensions of C1 and C2, respectively.
- The minimum distance of Q is min(d1, d2^⊥), where d1 and d2^⊥ are the minimum distances of C1 and C2^⊥, respectively.

The following diagram illustrates the basic architecture of a CSS quantum code:

```
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
+-----------------+-----------------+-----------------+

<----------------- n ----------------->
<----- k2 -----><----- k1 - k2 ----->
<---------- k1 --------->

C2 ⊆ C1 ⊆ C2^⊥
|ψ> + C2 ⊆ C1
Q = {|ψ> + C2 | |ψ> + C2 ⊆ C1}
```