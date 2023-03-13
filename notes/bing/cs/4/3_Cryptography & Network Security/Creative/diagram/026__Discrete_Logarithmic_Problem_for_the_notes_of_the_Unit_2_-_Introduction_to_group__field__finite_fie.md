The discrete logarithm problem is defined as: given a group G, a generator g of the group and an element h of G, to find the discrete logarithm to the base g of h in the group G. A possible ASCII diagram for the discrete logarithm problem is:

```
    h
    ^
    |
    | log_g
    |
    v
G <--- g
```

where G is the group, g is the generator, h is the element, and log_g is the discrete logarithm function. The diagram shows that h is the result of raising g to some power in the group G, and the problem is to find that power given g, h and G. The discrete logarithm problem is not always hard. The hardness of finding discrete logarithms depends on the groups. For example, in the group Z_p*, where p is a prime number, the discrete logarithm problem is hard if p is large, but easy if p is small. The discrete logarithm problem is considered to be computationally intractable, meaning that no efficient classical algorithm is known for computing discrete logarithms in general. However, there are some randomized algorithms that can achieve a better space complexity than deterministic algorithms. The discrete logarithm problem is important for cryptography, as it is the basis for many public-key cryptosystems, such as Diffie-Hellman key exchange and ElGamal encryption.